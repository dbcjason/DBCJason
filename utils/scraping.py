# 📌 utils/scraping.py
import os
import requests
import pandas as pd
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ✅ Path to store cached data
CACHE_FILE = "data/basketball_monster_cache.csv"
TRADE_CACHE_FILE = "data/trade_cache.json"

# ✅ Scraping Function for Google Sheets
def fetch_google_sheets_data():
    SHEET_URL = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/export?format=csv"
    try:
        df = pd.read_csv(SHEET_URL)
        df["Rank"] = pd.to_numeric(df["Rank"], errors="coerce").fillna(float("inf"))
        return df.set_index("Name")["Rank"].to_dict()
    except Exception as e:
        print(f"⚠️ ERROR: {e}")
        return {}

# ✅ Scrape Basketball Monster
def check_scrape_schedule():
    if os.path.exists(CACHE_FILE):
        return pd.read_csv(CACHE_FILE).set_index("Name")["Adjusted Rank"].to_dict()
    return {}

# ✅ Scrape NBA Injuries
def check_injury_cache():
    INJURY_CACHE_FILE = "data/nba_injury_cache.csv"
    if os.path.exists(INJURY_CACHE_FILE):
        return pd.read_csv(INJURY_CACHE_FILE).set_index("Player")["Return Date"].to_dict()
    return {}
