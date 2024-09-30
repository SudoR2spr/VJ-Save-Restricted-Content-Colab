import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21727017"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8c9ff17d8d1f6fbe228e5133b011fa99")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://dexmoer:dex23@dex.nm2sl.mongodb.net/?retryWrites=true&w=majority&appName=dex")
