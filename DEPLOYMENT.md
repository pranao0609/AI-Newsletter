# Deployment Guide for Render

This guide will help you deploy the AI News Aggregator to Render with a PostgreSQL database.

## Prerequisites

1. A [Render account](https://render.com) (free tier works)
2. Your GitHub repository connected to Render
3. Required API keys:
   - Groq API Key
   - Gmail credentials (email and app password)

## Deployment Steps

### Option 1: Using render.yaml (Recommended - Infrastructure as Code)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Add Render deployment configuration"
   git push origin main
   ```

2. **Create a new Blueprint on Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New" → "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml`

3. **Set Environment Variables**
   
   You'll need to set these **secret** environment variables in Render:
   
   - `GROQ_API_KEY` - Your Groq API key
   - `MY_EMAIL` - Your Gmail address
   - `APP_PASSWORD` - Your Gmail app password
   
   The database credentials will be automatically populated from the PostgreSQL service.

4. **Deploy**
   - Click "Apply" to create all services
   - Render will create:
     - PostgreSQL database (`ai-news-db`)
     - Cron job service (`ai-news-aggregator`) that runs daily at 9 AM UTC

### Option 2: Manual Setup

#### Step 1: Create PostgreSQL Database

1. Go to Render Dashboard → "New" → "PostgreSQL"
2. Configure:
   - **Name**: `ai-news-db`
   - **Database**: `ai_news_aggregator`
   - **User**: `ai_news_user`
   - **Region**: Oregon (or your preferred region)
   - **Plan**: Free
3. Click "Create Database"
4. **Save the connection details** (Internal Database URL)

#### Step 2: Create Cron Job Service

1. Go to Render Dashboard → "New" → "Cron Job"
2. Configure:
   - **Name**: `ai-news-aggregator`
   - **Environment**: Docker
   - **Region**: Oregon (same as database)
   - **Schedule**: `0 9 * * *` (daily at 9 AM UTC)
   - **Docker Context**: `.`
   - **Dockerfile Path**: `./Dockerfile`

3. **Add Environment Variables**:
   
   Click "Environment" and add:
   
   ```
   GROQ_API_KEY=<your-groq-api-key>
   MY_EMAIL=<your-gmail-address>
   APP_PASSWORD=<your-gmail-app-password>
   POSTGRES_USER=<from-database-internal-url>
   POSTGRES_PASSWORD=<from-database-internal-url>
   POSTGRES_HOST=<from-database-internal-url>
   POSTGRES_PORT=5432
   POSTGRES_DB=ai_news_aggregator
   ```
   
   **To get database credentials:**
   - Go to your PostgreSQL service
   - Copy the "Internal Database URL"
   - Format: `postgresql://USER:PASSWORD@HOST:PORT/DATABASE`
   - Extract each component

4. Click "Create Cron Job"

## Cron Schedule Options

The default schedule is `0 9 * * *` (9 AM UTC daily). You can customize:

- `0 9 * * *` - Daily at 9 AM UTC
- `0 */6 * * *` - Every 6 hours
- `0 0,12 * * *` - Twice daily (midnight and noon UTC)
- `0 9 * * 1-5` - Weekdays only at 9 AM UTC

## Testing the Deployment

### Manual Trigger (First Time)

1. Go to your Cron Job service in Render
2. Click "Manual Trigger" to run immediately
3. Check the logs to verify:
   - Database connection successful
   - Articles scraped
   - Digests created
   - Email sent

### Check Logs

```
Render Dashboard → Your Cron Job → Logs
```

Look for:
```
✓ Scraped X YouTube videos, Y OpenAI articles, Z Anthropic articles
✓ Processed X Anthropic articles
✓ Processed X transcripts
✓ Created X digests
✓ Email sent successfully with X articles
```

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `GROQ_API_KEY` | Groq API key for AI processing | `gsk_...` |
| `MY_EMAIL` | Gmail address to send digests to | `your@gmail.com` |
| `APP_PASSWORD` | Gmail app-specific password | `abcd efgh ijkl mnop` |
| `POSTGRES_USER` | Database username | `ai_news_user` |
| `POSTGRES_PASSWORD` | Database password | Auto-generated |
| `POSTGRES_HOST` | Database host | `dpg-xxx.oregon-postgres.render.com` |
| `POSTGRES_PORT` | Database port | `5432` |
| `POSTGRES_DB` | Database name | `ai_news_aggregator` |

## Getting Gmail App Password

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable 2-Step Verification (if not already enabled)
3. Go to "App passwords"
4. Generate a new app password for "Mail"
5. Copy the 16-character password (remove spaces)
6. Use this as `APP_PASSWORD`

## Monitoring

### Database

- Go to your PostgreSQL service in Render
- Click "Connect" to access the database
- Use the provided connection string with a PostgreSQL client

### Logs

- Cron job logs are available in Render Dashboard
- Each run creates a new log entry
- Logs are retained for 7 days on free tier

## Troubleshooting

### Database Connection Issues

```bash
# Check if database is accessible
psql <INTERNAL_DATABASE_URL>
```

### Missing Environment Variables

Check logs for errors like:
```
ValueError: GROQ_API_KEY environment variable is not set
```

Solution: Add the missing variable in Render Dashboard

### Email Not Sending

1. Verify `MY_EMAIL` and `APP_PASSWORD` are correct
2. Check Gmail app password is valid
3. Ensure 2-Step Verification is enabled on Google Account

### Build Failures

1. Check Dockerfile syntax
2. Verify all dependencies in `requirements.txt`
3. Check build logs for specific errors

## Updating the Application

1. Push changes to GitHub:
   ```bash
   git add .
   git commit -m "Update application"
   git push origin main
   ```

2. Render will automatically:
   - Detect the changes
   - Rebuild the Docker image
   - Deploy on next scheduled run

## Cost Optimization

**Free Tier Limits:**
- PostgreSQL: 1 GB storage, 97 hours/month
- Cron Job: 400 hours/month (more than enough for daily runs)

**Tips:**
- Use the free tier for personal use
- Upgrade to paid plans for production use
- Monitor database size regularly

## Next Steps

1. ✅ Deploy to Render
2. ✅ Verify first run
3. ✅ Check email digest
4. ✅ Monitor logs
5. 🎯 Customize user profile in `app/profiles/user_profile.py`
6. 🎯 Adjust cron schedule as needed
7. 🎯 Add more news sources if desired

## Support

- [Render Documentation](https://render.com/docs)
- [Render Community](https://community.render.com)
- Check application logs for debugging

---

**Happy Deploying! 🚀**
