import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters


load_dotenv()

# ───── Basic Bot Configuration ───── #
API_ID = int(getenv("API_ID", "28795088"))
API_HASH = getenv("API_HASH", "6684413228de152cb7e93ec1e97cf737")
BOT_TOKEN = getenv("BOT_TOKEN", "7687591049:AAH-BMzGllHqeCkJ_oGkfXQGU8QQav0bCHM")

OWNER_ID = int(getenv("OWNER_ID", "1928612564"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "ofckelragtg")
BOT_USERNAME = getenv("BOT_USERNAME", "kelramusicbot")
BOT_NAME = getenv("BOT_NAME", "˹ᴋᴇʟʀᴀ ᴠɪᴀ ʙᴏᴛ˼")
ASSUSERNAME = getenv("ASSUSERNAME", "id6nich")
EVALOP = list(map(int, getenv("EVALOP", "1928612564").split()))

# ───── Mongo & Logging ───── #
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://zea:123@cluster0.wlpzmlz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOGGER_ID = getevn("LOGGER_ID", "-1002465368786")

# ───── Limits and Durations ───── #
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ───── Custom API Configs ───── #
COOKIE_URL = getenv("COOKIES_URL", "https://batbin.me/strobilomyces") #necessary
API_URL = getenv("API_URL") #optional
API_KEY = getenv("API_KEY") #optional

# ───── Heroku Configuration ───── #
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ───── Git & Updates ───── #
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/hokagejian/kelraxmusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN")

# ───── Support & Community ───── #
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.mekelrapillas")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/logskelra")

# ───── Assistant Auto Leave ───── #
AUTO_LEAVING_ASSISTANT = True
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

# ───── Error Handling ───── #
DEBUG_IGNORE_LOG =True

# ───── Spotify Credentials ───── #
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ───── Session Strings ───── #
STRING1 = getenv("STRING_SESSION1", "BQAP-GEASGlila1JolpIR0xuvBv_OB_BsI7aAsbIsVei1LP1nqm6nGmm22R8m6X6V_MHlpj24IwUMv5rWDyjmOJVkWUPgkSc_O3ckClE4gzDcoxikEzyGTRVMX7-VeEVjRS5YSFJoLK8JKGTS0KmW_5_DhiIg9NRj6JxRyidgCLKuEZtxIcwRHEa7z3rJfOp4ZrlgfyKGUQ3dFe7rZ3yK1Qobo8DNFc3Sd0NPUd-vJqMM9U06SpVLGg-qN1ibeDPFAGsk6V6v6dOz0IjIfJJC_ml-EyDF61ao6ePkt5_xBbKz92YtacttlLl0eag-Tvx3J_6iI06bYny_XL0tbb-mMTtO3t6-wAAAAGFt8EsAA")
STRING2 = getenv("STRING_SESSION3") 
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ───── Server Settings ───── #
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))

# ───── Bot Media Assets ───── #
START_VIDS = [
    "https://telegra.ph/file/9b7e1b820c72a14d90be7.mp4",
    "https://telegra.ph/file/72f349b1386d6d9374a38.mp4",
    "https://telegra.ph/file/a4d90b0cb759b67d68644.mp4"
]

STICKERS = [
    "CAACAgUAAx0Cd6nKUAACASBl_rnalOle6g7qS-ry-aZ1ZpVEnwACgg8AAizLEFfI5wfykoCR4h4E",
    "CAACAgUAAx0Cd6nKUAACATJl_rsEJOsaaPSYGhU7bo7iEwL8AAPMDgACu2PYV8Vb8aT4_HUPHgQ"
]
HELP_IMG_URL = "https://files.catbox.moe/h3jqa8.jpg"
PING_VID_URL = "https://files.catbox.moe/mi8nr0.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/t72ntd.jpg"
STATS_VID_URL = "https://files.catbox.moe/5vdaw5.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/90juvd.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/7qplwr.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/4roh51.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/wpkxzt.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/cq87ww.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/qp5aa5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/qp5aa5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/qp5aa5.jpg"
FAILED = "https://files.catbox.moe/cq87ww.jpg"


# ───── Utility & Functional ───── #
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")


# ───── Bot Introduction Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🌈", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌", "🧨"]


# ───── Runtime Structures ───── #
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ───── URL Validation ───── #
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
