# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨𝐇𝐚𝐥𝐨!, [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
𝐒𝐚𝐲𝐚 𝐀𝐝𝐚𝐥𝐚𝐡 𝐁𝐨𝐭 𝐗𝐭𝐚𝐚𝐧𝐣𝐤𝐧𝐭𝐥 𝐘𝐚𝐧𝐠 𝐋𝐚𝐦𝐚 𝐒𝐮𝐝𝐚𝐡 𝐑𝐞𝐡𝐚𝐭 𝐃𝐚𝐧 𝐒𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐁𝐚𝐫𝐮 𝐁𝐢𝐬𝐚 𝐊𝐞𝐦𝐛𝐚𝐥𝐢 𝐃𝐞𝐧𝐠𝐚𝐧 𝐍𝐚𝐦𝐚 𝐁𝐚𝐫𝐮 ( xᴛᴀᴀɴᴊᴋɴᴛʟ ʀᴇʙᴏʀɴ ) , 𝐃𝐞𝐧𝐠𝐚𝐧 𝐅𝐢𝐭𝐮𝐫 𝐃𝐚𝐧 𝐕𝐞𝐫𝐬𝐢 𝐓𝐞𝐫𝐛𝐚𝐫𝐮 𝐉𝐮𝐠𝐚.
➖➖➖➖➖➖➖➖➖➖➖➖➖
• 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐕𝐢𝐝𝐞𝐨 𝐀𝐧𝐝 𝐌𝐮𝐬𝐢𝐜
• 𝐋𝐚𝐬𝐭 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 
• 𝐅𝐫𝐞𝐞 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 
➖➖➖➖➖➖➖➖➖➖➖➖➖

❃ 𝐌𝐚𝐧𝐚𝐠𝐞𝐝 𝐖𝐢𝐭𝐡 𝐁𝐲 [𝐗𝐓𝐀](t.me/xtaaaanj)
❃ 𝐓𝐡𝐚𝐧𝐤'𝐬 𝐓𝐨 [ʟᴇᴠɪɴᴀ-x](t.me/dlwrml)

➥ 𝐓𝐞𝐤𝐚𝐧 𝐓𝐨𝐦𝐛𝐨𝐥 𝐃𝐢 𝐁𝐚𝐰𝐚𝐡 𝐔𝐧𝐭𝐮𝐤 𝐌𝐞𝐧𝐠𝐞𝐭𝐚𝐡𝐮𝐢 𝐅𝐢𝐭𝐮𝐫 𝐋𝐞𝐧𝐠𝐤𝐚𝐩 𝐃𝐚𝐫𝐢 𝐗𝐭𝐚𝐚𝐧𝐣𝐤𝐧𝐭𝐥 𝐑𝐞𝐛𝐨𝐫𝐧 𝐁𝐨𝐭""",
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
                    InlineKeyboardButton("❤ Donasi", url=f"https://t.me/{OWNER_NAME}"),
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


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ Panduan Dasar untuk menggunakan bot ini:

1.) Pertama, tambahkan saya ke grup Anda.
2.) Kemudian, promosikan saya sebagai administrator dan berikan semua izin kecuali Admin Anonim.
3.) Setelah mempromosikan saya, ketik /reload di grup untuk menyegarkan data admin.
3.) Tambahkan @xtaanjkntlasisten ke grup Anda atau ketik /userbotjoin untuk mengundangnya.
4.) Nyalakan obrolan video terlebih dahulu sebelum mulai memutar video/musik.
5.) Terkadang, memuat ulang bot dengan menggunakan perintah /reload dapat membantu Anda memperbaiki beberapa masalah.

📌: Jika userbot tidak bergabung ke video chat, pastikan jika video chat sudah aktif, atau ketik /userbotleave lalu ketik /userbotjoin lagi.

💡: Jika Anda memiliki pertanyaan lanjutan tentang bot ini, Anda dapat menceritakannya di obrolan dukungan saya di sini: @XtaanjkntlReborn

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hallo [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **tekan tombol di bawah untuk membaca penjelasan dan melihat daftar perintah yang tersedia!**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Perintah Admin", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Perintah Sudo", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Perintah Dasar", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 : berikut adalah perintah dasarnya:

» /mplay (nama lagu/tautan) - putar musik di obrolan video
» /stream (query/link) - streaming yt live/radio live music
» /vplay (nama video/tautan) - putar video di obrolan video
» /vstream - putar video langsung dari yt live/m3u8
» /playlist - menampilkan daftar putar
» /video (permintaan) - unduh video dari youtube
» /song (query) - download lagu dari youtube
» /lyric (query) - memo lirik lagu
» /search (query) - cari link video youtube

» /ping - tampilkan status bot ping
» /uptime - tampilkan status uptime bot
» /alive - tampilkan info bot hidup (dalam grup)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮: berikut adalah perintah admin:

» /pause - jeda streaming
» /resume - lanjutkan streaming
» /skip - beralih ke aliran berikutnya
» /stop - hentikan streaming
» /vmute - bisukan bot pengguna di obrolan suara
» /vunmute - mengaktifkan suara bot pengguna di obrolan suara
» /volume 1-200 - mengatur volume musik (userbot harus admin)
» /reload - reload bot dan refresh data admin
» /userbotjoin - undang userbot untuk bergabung dengan grup
» /userbotleave - perintahkan userbot keluar dari grup

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮: ini perintah sudo:

» /rmw - bersihkan semua file mentah
» /rmd - bersihkan semua file yang diunduh
» /sysinfo - menampilkan informasi sistem
» /update - perbarui bot Anda ke versi terbaru
» /restart - mulai ulang bot Anda
» /leaveall - perintahkan userbot keluar dari semua grup

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
