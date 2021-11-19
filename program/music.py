# Copyright (C) 2021 By Veez Music-Project
# Commit Start Date 20/10/2021
# Finished On 28/10/2021

import asyncio
import re

from config import ASSISTANT_NAME, BOT_USERNAME, IMG_1, IMG_2
from driver.filters import command, other_filters
from driver.queues import QUEUE, add_to_queue
from driver.veez import call_py, user
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:70]
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(command(["play", f"play@{BOT_USERNAME}"]) & other_filters)
async def play(c: Client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data="cbmenu"),
                InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data="cls"),
            ]
        ]
    )
    if m.sender_chat:
        return await m.reply_text("Anda adalah __Admin Anonim__ !\n\n» kembali ke akun pengguna dari hak admin.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 Untuk menggunakan saya, saya harus menjadi **Admin** dengan **izin** berikut:\n\n» ❌ __Menghapus pesan__\n» ❌ __Membatasi pengguna__\n» ❌ __Tambahkan pengguna__\n» ❌ __Kelola obrolan vidio__\n\nData **diperbarui** secara otomatis setalah anda **menjadikan saya Admin**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "Tidak ada izin :" + "\n\n» ❌ __Kelola obrolan vidio__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "Tidak ada izin:" + "\n\n» ❌ __Menghapus pesan__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("Tidak ada izin:" + "\n\n» ❌ __Menambahkan pengguna__")
        return
    if not a.can_restrict_members:
        await m.reply_text("Tidak ada izin:" + "\n\n» ❌ __Membatasi pengguna__")
        return
    try:
        ubot = await user.get_me()
        b = await c.get_chat_member(chat_id, ubot.id)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **terkena banned dari grup ini** {m.chat.title}\n\n» **unban userbot jika kamu ingin menggunakan saya.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **userbot gagal masuk**\n\n**reason**: `{e}`")
                return
        else:
            try:
                pope = await c.export_chat_invite_link(chat_id)
                pepo = await c.revoke_chat_invite_link(chat_id, pope)
                await user.join_chat(pepo.invite_link)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **userbot gagal masuk**\n\n**reason**: `{e}`"
                )

    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **mengunduh suara...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **Telah ditambahkan ke antrean »** `{pos}`\n\n🏷 **Nama Judul:** [{songname}]({link})\n💭 **Chat:** `{chat_id}`\n🎧 **Permintaan dari:** {m.from_user.mention()}",
                    reply_markup=keyboard,
                )
            else:
             try:
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().local_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_2}",
                    caption=f"💡 **Musik dimulai.**\n\n🏷 **Nama Judul:** [{songname}]({link})\n💭 **Chat:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Permintaan dari:** {requester}",
                    reply_markup=keyboard,
                )
             except Exception as e:
                await suhu.delete()
                await m.reply_text(f"🚫 error:\n\n» {e}")
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» membalas **file audio** atau **memberikan sesuatu untuk dicari.**"
                )
            else:
                suhu = await m.reply("🔎 **Mencari...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **Tidak ada hasil yang ditemukan.**")
                else:
                    songname = search[0]
                    url = search[1]
                    veez, ytlink = await ytdl(url)
                    if veez == 0:
                        await suhu.edit(f"❌ yt-dl masalah terdeteksi\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Audio", 0
                            )
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_1}",
                                caption=f"💡 **Telah ditambakan ke antrian »** `{pos}`\n\n🏷 **Nama Judul:** [{songname}]({url})\n💭 **Chat:** `{chat_id}`\n🎧 **Permintaan dari:** {requester}",
                                reply_markup=keyboard,
                            )
                        else:
                            try:
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                                await suhu.delete()
                                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                await m.reply_photo(
                                    photo=f"{IMG_2}",
                                    caption=f"💡 **Musik dimulai.**\n\n🏷 **Nama Judul:** [{songname}]({url})\n💭 **Chat:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Permintaan dari:** {requester}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await suhu.delete()
                                await m.reply_text(f"🚫 error: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "» membalas **file audio** atau **memberikan sesuatu untuk dicari.**"
            )
        else:
            suhu = await m.reply("🔎 **Mencari...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("❌ **Tidak ada hasil yang ditemukan.**")
            else:
                songname = search[0]
                url = search[1]
                veez, ytlink = await ytdl(url)
                if veez == 0:
                    await suhu.edit(f"❌ yt-dl masalah terdeteksi\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=f"{IMG_1}",
                            caption=f"💡 **Telah ditambakan kedalam antrian »** `{pos}`\n\n🏷 **Nama Judul:** [{songname}]({url})\n💭 **Chat:** `{chat_id}`\n🎧 **Permintaan dari:** {requester}",
                            reply_markup=keyboard,
                        )
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_2}",
                                caption=f"💡 **Musik dimulai.**\n\n🏷 **Nama judul:** [{songname}]({url})\n💭 **Chat:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Permintaan dari:** {requester}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await suhu.delete()
                            await m.reply_text(f"🚫 error: `{ep}`")


# stream is used for live streaming only


@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(c: Client, m: Message):
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data="cbmenu"),
                InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data="cls"),
            ]
        ]
    )
    if m.sender_chat:
        return await m.reply_text("Anda adalah __Admin Anonim__ !\n\n» kembali ke akun pengguna dari hak admin.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 Untuk menggunakan saya, saya harus menjadi **Admin** dengan **izin** berikut:\n\n» ❌ __Menghapus pesan__\n» ❌ __Membatasi pengguna__\n» ❌ __Menambahkan pengguna__\n» ❌ __Kelola obrolan vidio__\n\nData **diperbarui** Secara otomatis setelah anda **menjadikan saya Admin**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "Tidak ada izin:" + "\n\n» ❌ __Kelola obrolan vidio__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "Tidak ada izin:" + "\n\n» ❌ __Menghapus pesan__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("Tidak ada izin:" + "\n\n» ❌ __Menambahkan pengguna__")
        return
    if not a.can_restrict_members:
        await m.reply_text("Tidak ada izin:" + "\n\n» ❌ __Membatasi pengguna__")
        return
    try:
        ubot = await user.get_me()
        b = await c.get_chat_member(chat_id, ubot.id)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **terkena banned dari grup ini** {m.chat.title}\n\n» **unban userbot jika kamu ingin menggunakan saya.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **userbot gagal masuk**\n\n**reason**: `{e}`")
                return
        else:
            try:
                pope = await c.export_chat_invite_link(chat_id)
                pepo = await c.revoke_chat_invite_link(chat_id, pope)
                await user.join_chat(pepo.invite_link)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **userbot gagal masuk**\n\n**reason**: `{e}`"
                )

    if len(m.command) < 2:
        await m.reply("» beri saya live-link/m3u8 url/youtube link untuk stream.")
    else:
        link = m.text.split(None, 1)[1]
        suhu = await m.reply("🔄 **proses stream...**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            veez, livelink = await ytdl(link)
        else:
            livelink = link
            veez = 1

        if veez == 0:
            await suhu.edit(f"❌ yt-dl masalah terdeteksi\n\n» `{ytlink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **Telah di tambahkan ke antrian»** `{pos}`\n\n💭 **Chat:** `{chat_id}`\n🎧 **Permintaan dari:** {requester}",
                    reply_markup=keyboard,
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            livelink,
                        ),
                        stream_type=StreamType().live_stream,
                    )
                    add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                    await suhu.delete()
                    requester = (
                        f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                    )
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        caption=f"💡 **[Music live]({link}) stream dimulai.**\n\n💭 **Chat:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Permintaan dari:** {requester}",
                        reply_markup=keyboard,
                    )
                except Exception as ep:
                    await suhu.delete()
                    await m.reply_text(f"🚫 error: `{ep}`")
