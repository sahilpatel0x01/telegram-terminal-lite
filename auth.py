import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("TG_API_ID")
API_HASH = os.getenv("TG_API_HASH")

if API_ID is not None:
    API_ID = int(API_ID)

SESSION = "session/cli"

def get_client():
    if not API_ID or not API_HASH:
        raise ValueError("TG_API_ID and TG_API_HASH must be set in .env or environment variables.")
    # Ensure session directory exists
    os.makedirs(os.path.dirname(SESSION), exist_ok=True)
    
    return TelegramClient(
        SESSION, 
        API_ID, 
        API_HASH,
        
        # --- Android setup ---
        # device_model="Samsung Galaxy S21 FE 5G",
        # system_version="Android 14",
        # app_version="1.0"
        
        # --- macOS setup ---
        # device_model="MacBook Pro (M4 Max)",
        # system_version="macOS 15.1.1",
        # app_version="11.4.1"

        # --- iOS setup ---
        device_model="iPhone 15 Pro Max",
        system_version="iOS 17.4.1",
        app_version="11.4.1"
    )
