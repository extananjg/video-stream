import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "dlwrml", "xtaaaanj")
ALIVE_NAME = getenv("ALIVE_NAME", "Levina", "Xta")
BOT_USERNAME = getenv("BOT_USERNAME", "veezvideobot", "xtaanjnkntl_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida", "xtaanjkntlasisten")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup", "XtaanjkntlReborn")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel", "ikylvyuuu")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", ""https://telegra.ph/file/174a79fdbac79fd065082.png)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a44a2ce25ce6ac0d2997a.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/feb34e45aae49f617b442.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/a159a3e1cea9a5c1f42d0.png")
