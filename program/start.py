from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨𝐇𝐚𝐥𝐨!{message.from_user.mention()} !**\n
𝐍𝐚𝐦𝐚 𝐒𝐚𝐲𝐚 𝐀𝐝𝐚𝐥𝐚𝐡 𝐗𝐭𝐚𝐚𝐧𝐣𝐤𝐧𝐭𝐥 𝐁𝐨𝐭 , 𝐒𝐚𝐲𝐚 𝐀𝐝𝐚𝐥𝐚𝐡 𝐒𝐞𝐛𝐮𝐚𝐡 𝐁𝐨𝐭 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐘𝐚𝐧𝐠 𝐁𝐢𝐬𝐚 𝐀𝐧𝐝𝐚 𝐆𝐮𝐧𝐚𝐤𝐚𝐧 𝐃𝐢 𝐆𝐫𝐮𝐩 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐀𝐧𝐝𝐚
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
• 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐕𝐢𝐝𝐞𝐨 𝐀𝐧𝐝 𝐌𝐮𝐬𝐢𝐜 
• 𝐅𝐫𝐞𝐞 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬
• 𝐋𝐚𝐬𝐭 𝐯𝐞𝐫𝐬𝐢𝐨𝐧
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
❃ 𝐌𝐚𝐧𝐚𝐠𝐞 𝐁𝐲 [𝐗𝐓𝐀](t.me/xtaaaanj)
❃ 𝐓𝐡𝐚𝐧𝐤'𝐬 𝐓𝐨 [𝐋𝐄𝐕𝐈𝐍𝐀](t.me/dlwrml) 𝐚𝐧𝐝 𝐓𝐡𝐚𝐧𝐤'𝐬 𝐓𝐨 𝐌𝐲 𝐓𝐡𝐞𝐚𝐜𝐡𝐞𝐫 [𝐍𝐝𝐫𝐚𝐚𝐚](t.me/IamYourEnemy)

➥ 𝐓𝐞𝐤𝐚𝐧 𝐓𝐨𝐦𝐛𝐨𝐥 𝐃𝐢 𝐁𝐚𝐰𝐚𝐡 𝐔𝐧𝐭𝐮𝐤 𝐌𝐞𝐧𝐠𝐞𝐭𝐚𝐡𝐮𝐢 𝐅𝐢𝐭𝐮𝐫 𝐋𝐞𝐧𝐠𝐤𝐚𝐩 𝐃𝐚𝐫𝐢 𝐒𝐚𝐲𝐚
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Tambakan Kedalam Grup Anda ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Panduan Perintah", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Perintah", callback_data="cbcmds"),
                    InlineKeyboardButton("❤️ Donasi", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Source Code", url="https://github.com/levina-lab/video-stream"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Halo {message.from_user.mention()}, saya {BOT_NAME}**\n\n✨ Bot berfungsi normal\n🍀 Tuanku: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 PyTgCalls version: `{pytover.__version__}`\n✨ Uptime Status: `{uptime}`\n\n**Terima kasih telah Menambahkan saya di sini, untuk memutar video & musik di obrolan video Grup Anda** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
