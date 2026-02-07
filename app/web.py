from fastapi import FastAPI, BackgroundTasks, HTTPException, Header
from app.daily_runner import run_daily_pipeline
from app.database.models import Base
from app.database.connection import engine
import uvicorn
import os

# Create tables on startup
# This ensures tables exist before we try to use them
Base.metadata.create_all(engine)

app = FastAPI()

def run_pipeline_task(hours: int, top_n: int):
    print("Starting periodic pipeline...")
    try:
        run_daily_pipeline(hours=hours, top_n=top_n)
    except Exception as e:
        print(f"Error in pipeline task: {e}")

@app.get("/")
def health_check():
    return {"status": "ok", "service": "AI News Aggregator"}

@app.post("/run-pipeline")
def run_pipeline(
    background_tasks: BackgroundTasks,
    hours: int = 24,
    top_n: int = 10,
    authorization: str = Header(None)
):
    # check for CRON_SECRET if set
    expected_secret = os.getenv("CRON_SECRET")
    if expected_secret:
        if authorization != f"Bearer {expected_secret}":
             raise HTTPException(status_code=401, detail="Unauthorized")
    
    background_tasks.add_task(run_pipeline_task, hours, top_n)
    return {"message": "Pipeline triggered", "hours": hours, "top_n": top_n}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
