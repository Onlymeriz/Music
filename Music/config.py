##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA5XvWImRMu4-CrSWf8fWwlFqREj6mJhvIIc1BV9cePAfnp6y60ub-G-gcEr9Tvcgcz4xBq-cu-Uk4ZB9niFhL7gLEf6SYg5oZzf3KHh-gytdcaRAY6vjoz1xjspYqRLW8DqPyYIj96X-b8jHoGjev1mh3jJ-FOeQ1PWy7KMjdx964PtKFjVyCMvpg0f_m8TQ4LMBse944VPN9YuKtw1MefNb8fBcFVQ7DwU5yq0GBD0c-ogK8qHdfNUy0H4UHlIrOXPEiRfF-oTBg-cm6iMTCG9olu8oaE4K3lFzMFl80TquEosok8Q3YSDgbYCYIJlYiEs9SGHra8WIiXW8Uno3tZPtdGcAA")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID", "22156937"))
API_HASH = getenv("API_HASH", "0f8f66b06b1c53b9263bcfb1123e9c85")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500000"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ . , : ; !").split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1054295664").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001812143750"))
ASS_ID = int(getenv("ASS_ID", "1054295664"))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
OWNER_ID.append(951454060)
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ҡʏɴλɴ ꭙ ꝛᴏʙᴏᴛ")
GROUP = getenv("GROUP", "AyaMusicLog")
CHANNEL = getenv("CHANNEL", "kontenfilm")
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))
MUST_JOIN = getenv("MUST_JOIN", "kontenfilm")
