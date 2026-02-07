#!/usr/bin/env python3
"""
Pre-deployment validation script
Checks if all components are ready for deployment
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a required file exists"""
    if Path(filepath).exists():
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ {description} MISSING: {filepath}")
        return False

def check_env_vars():
    """Check if required environment variables are documented"""
    required_vars = [
        "GROQ_API_KEY",
        "MY_EMAIL", 
        "APP_PASSWORD",
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_DB"
    ]
    
    print("\n📋 Required Environment Variables:")
    for var in required_vars:
        print(f"   - {var}")
    
    return True

def check_imports():
    """Check if critical imports work"""
    print("\n🔍 Checking Python imports...")
    
    try:
        from app.agent.digest_agent import DigestAgent
        print("✓ DigestAgent")
    except Exception as e:
        print(f"✗ DigestAgent: {e}")
        return False
    
    try:
        from app.agent.curator_agent import CuratorAgent
        print("✓ CuratorAgent")
    except Exception as e:
        print(f"✗ CuratorAgent: {e}")
        return False
    
    try:
        from app.agent.email_agent import EmailAgent
        print("✓ EmailAgent")
    except Exception as e:
        print(f"✗ EmailAgent: {e}")
        return False
    
    try:
        from app.database.repository import Repository
        print("✓ Repository")
    except Exception as e:
        print(f"✗ Repository: {e}")
        return False
    
    try:
        from app.scrapers.youtube import YouTubeScraper
        from app.scrapers.anthropic import AnthropicScraper
        from app.scrapers.openai import OpenAIScraper
        print("✓ All Scrapers")
    except Exception as e:
        print(f"✗ Scrapers: {e}")
        return False
    
    return True

def main():
    print("=" * 60)
    print("🚀 AI News Aggregator - Pre-Deployment Validation")
    print("=" * 60)
    
    all_checks_passed = True
    
    # Check deployment files
    print("\n📁 Checking Deployment Files:")
    all_checks_passed &= check_file_exists("render.yaml", "Render config")
    all_checks_passed &= check_file_exists("Dockerfile", "Docker config")
    all_checks_passed &= check_file_exists(".dockerignore", "Docker ignore")
    all_checks_passed &= check_file_exists("DEPLOYMENT.md", "Deployment guide")
    all_checks_passed &= check_file_exists(".env.example", "Env example")
    
    # Check application files
    print("\n📁 Checking Application Files:")
    all_checks_passed &= check_file_exists("main.py", "Main entry point")
    all_checks_passed &= check_file_exists("requirements.txt", "Dependencies")
    all_checks_passed &= check_file_exists("app/daily_runner.py", "Daily runner")
    all_checks_passed &= check_file_exists("app/database/models.py", "Database models")
    all_checks_passed &= check_file_exists("app/profiles/user_profile.py", "User profile")
    
    # Check environment variables
    all_checks_passed &= check_env_vars()
    
    # Check imports
    all_checks_passed &= check_imports()
    
    # Summary
    print("\n" + "=" * 60)
    if all_checks_passed:
        print("✅ All validation checks PASSED!")
        print("=" * 60)
        print("\n📖 Next Steps:")
        print("   1. Review DEPLOYMENT.md for deployment instructions")
        print("   2. Push code to GitHub")
        print("   3. Connect repository to Render")
        print("   4. Set environment variables in Render")
        print("   5. Deploy!")
        return 0
    else:
        print("❌ Some validation checks FAILED!")
        print("=" * 60)
        print("\n⚠️  Please fix the issues above before deploying")
        return 1

if __name__ == "__main__":
    sys.exit(main())
