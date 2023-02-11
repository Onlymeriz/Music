##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID", "22156937"))
API_HASH = getenv("API_HASH", "0f8f66b06b1c53b9263bcfb1123e9c85")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500000"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ . , : ; !").split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1054295664").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001836099748"))
ASS_ID = int(getenv("ASS_ID", "1054295664"))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
OWNER_ID.append(951454060)
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ҡʏɴλɴ ꭙ ꝛᴏʙᴏᴛ")
GROUP = getenv("GROUP", "kynansupport")
CHANNEL = getenv("CHANNEL", "kontenfilm")
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))
MUST_JOIN = getenv("MUST_JOIN", "kontenfilm")
