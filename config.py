
import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "29895250"))
API_HASH = os.environ.get("API_HASH", "29ca1e2311efdf950eea03a6ae2bc8ee")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "Bot Token")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "").split(",")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Dpcinema")
DATABASE_URL = os.getenv("DATABASE_URL", "Mongo url")
OWNER_ID = int(os.environ.get("OWNER_ID", "2017335429"))

# Add OWNER_ID to ADMINS if not already present
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Optional variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002386866175"))
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "JACK_DADDY")  # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") == "True"  # Convert to boolean
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')  # image when someone hit /start
LINK_BYPASS = os.environ.get("LINK_BYPASS", "False") == "True"  # Convert to boolean
