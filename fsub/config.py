from os import getenv
from dotenv import load_dotenv
from logging import basicConfig, INFO, WARNING, getLogger, Logger


load_dotenv("config.env")

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

CHANNEL_DB = int(getenv("CHANNEL_DB"))
DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://hbreaction1907:J7HqAC-r$4VZTQz@cluster0.8wjj7jp.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = getenv("DATABASE_NAME", "Cluster0")

RESTRICT = getenv("RESTRICT")

BUTTON_ROW = int(getenv("BUTTON_ROW", 2))
FORCE_SUB_ = {}
FSUB_TOTAL = 1
while True:
    key = f"FORCE_SUB_{FSUB_TOTAL}"
    value = getenv(key)
    if value is None:
        break
    FORCE_SUB_[FSUB_TOTAL] = int(value)
    FSUB_TOTAL += 1
‌‌‌‌

START_MESSAGE = getenv("START_MESSAGE", "Hello {first}\n\n<b>I can store private files in Specified Channel and other users can access it from special link.</b>")
FORCE_MESSAGE = getenv("FORCE_MESSAGE", "Hello {first}\n\n<b>You have to join my Channel to access the file </b>")


ADMINS = [int(x) for x in (getenv("ADMINS").split())]
    
CUSTOM_CAPTION = getenv("CUSTOM_CAPTION", None)
DISABLE_BUTTON = getenv("DISABLE_BUTTON")


basicConfig(level=INFO, format="[%(levelname)s] - %(message)s")
getLogger("hydrogram").setLevel(WARNING)
def LOGGER(name: str) -> Logger:
    return getLogger(name)
