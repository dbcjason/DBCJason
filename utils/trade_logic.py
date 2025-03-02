# 📌 utils/trade_logic.py
import hashlib
from datetime import datetime
from run_gpt import query_gemini, rate_limit

# ✅ Define Rookie Draft Years and Pick Ranges
rookie_draft_years = ["Select Year", "2025", "2026"]
rookie_draft_ranges = [
    "Projected Top 3", "Projected 4-7", "Projected 8-10", "Projected 11-12",
    "Projected 13-15", "Projected 16-20", "Projected 21-25", "Projected 26-30"
]
individual_picks = [str(i) for i in range(1, 31)]  # Picks 1-30

# ✅ Check if it's the offseason (April 15 - October 15)
today = datetime.today()
is_offseason = (today.month == 4 and today.day >= 15) or (5 <= today.month <= 9) or (today.month == 10 and today.day <= 15)

def get_user_id(request_ip):
    """Generate a consistent user ID from the request IP address."""
    if request_ip:
        return hashlib.sha256(request_ip.encode()).hexdigest()
    return "unknown_ip"

def add_pick_to_team(team, selected_year, selected_pick):
    """Adds a selected draft pick to the trade list."""
    if selected_pick:
        return f"{team}, {selected_year} {selected_pick}" if team else f"{selected_year} {selected_pick}"
    return team
