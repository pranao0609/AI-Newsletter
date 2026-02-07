# AI News Aggregator

An end-to-end **AI-powered news aggregation platform** that collects, filters, and summarizes real-time news using intelligent processing and a scalable backend architecture.
The project demonstrates complete lifecycle development—from **local setup and core AI logic** to **deployment configuration and production optimization**.

---

##  Features

* Real-time **news data collection and preprocessing**
* **AI-based filtering and summarization** of articles
* Clean, modular **backend architecture for scalability**
* Environment-based **deployment configuration**
* **Production-ready optimizations** for performance and stability

---

##  Tech Stack

* **Python** – Core backend logic
* **AI/NLP Libraries** – News filtering and summarization
* **API Integration** – News data sourcing
* **Deployment Tools** – Environment configuration and hosting setup

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-news-aggregator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

---

##  Deployment

This application is ready to deploy on **Render** with PostgreSQL database support.

### Quick Deploy

1. Push to GitHub
2. Connect to Render
3. Use the included `render.yaml` for automatic setup

📖 **[Full Deployment Guide](DEPLOYMENT.md)** - Complete step-by-step instructions

### What Gets Deployed

- **PostgreSQL Database** - Stores articles, digests, and metadata
- **Cron Job Service** - Runs daily to aggregate and email AI news
- **Automatic Migrations** - Database tables created on first run

### Deployment Files

- `render.yaml` - Infrastructure as code configuration
- `Dockerfile` - Container configuration
- `DEPLOYMENT.md` - Detailed deployment guide
- `.env.example` - Environment variables template

---

##  Learning Outcomes

This project showcases the ability to:

* Build a **complete AI-powered application** from scratch
* Design **scalable backend architecture**
* Integrate **AI workflows into real-world systems**
* Prepare and optimize software for **production deployment**

---
