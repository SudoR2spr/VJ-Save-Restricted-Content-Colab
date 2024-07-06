import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6865080558:AAG78HHqTGVoBkX1A4UWYnvUCJGfTZ0Hc")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22451323"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4783925ba83751dfadedcc961bf1275")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://heroku:heroku@cluster0.wamwxpr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
