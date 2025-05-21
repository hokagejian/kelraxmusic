import asyncio
import random
import re
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait

from Tune import app

SPAM_CHATS = []

RANDOM_SYMBOLS = [
    "⭐", "🔥", "🍀", "🍕", "🎉", "🌟", "🎵", "😎", "🍔", "⚡", "💎", "🎲", "🍩", "🦄", "🌈",
    "🎈", "🎸", "🥇", "💡", "🚀", "🕹️", "🐧", "🐲", "🍉", "🍟", "🥑", "🧊", "🍿", "🥤"
]

def get_random_symbol():
    return random.choice(RANDOM_SYMBOLS)

def htmlify_links(text):
    # Otomatis jadikan link HTML agar klik-able
    url_pattern = r'(https?://[^\s<]+)'
    return re.sub(url_pattern, r'<a href="\1">\1</a>', text)

async def is_admin(chat_id, user_id):
    admin_ids = [
        admin.user.id
        async for admin in app.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        )
    ]
    return user_id in admin_ids

@app.on_message(
    filters.command(["all", "allmention", "mentionall", "tagall"], prefixes=["/", "@"])
)
async def tag_all_users(_, message):
    """Tag all dengan caption+link dalam <blockquote>, mention+emoji random juga <blockquote>."""
    if not message.from_user:
        return
    admin = await is_admin(message.chat.id, message.from_user.id)
    if not admin:
        return

    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "<blockquote><b>Tag all sedang berjalan der, ketik /cancel untuk membatalkan der</b></blockquote>"
        )

    replied = message.reply_to_message
    # Ambil caption dari command atau reply
    if replied and replied.text:
        raw_caption = replied.text
    elif len(message.command) > 1:
        raw_caption = message.text.split(None, 1)[1]
    else:
        raw_caption = ""

    if not raw_caption:
        return await message.reply_text(
            "<blockquote><b>Kasih teksnya der\n/tagall Yuk cek info lengkap di https://contoh.link/baru</b></blockquote>"
        )

    # Bikin link dalam caption jadi klik-able HTML
    caption_html = htmlify_links(raw_caption)
    caption_block = f"<blockquote>{caption_html}</blockquote>"

    usernum = 0
    usertxt = ""
    try:
        SPAM_CHATS.append(message.chat.id)
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            if m.user.is_deleted or m.user.is_bot:
                continue
            symbol = get_random_symbol()
            usernum += 1
            usertxt += f"<blockquote>{symbol} <a href='tg://user?id={m.user.id}'>{m.user.first_name}</a></blockquote>\n"
            if usernum == 7:
                text_to_send = f"{caption_block}\n{usertxt}"
                await (replied.reply_text if replied else app.send_message)(
                    message.chat.id,
                    text_to_send,
                    parse_mode="html",
                    disable_web_page_preview=False,
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        if usernum != 0:
            text_to_send = f"{caption_block}\n{usertxt}"
            await (replied.reply_text if replied else app.send_message)(
                message.chat.id,
                text_to_send,
                parse_mode="html",
                disable_web_page_preview=False,
            )
    except FloodWait as e:
        await asyncio.sleep(e.value)
    try:
        SPAM_CHATS.remove(message.chat.id)
    except Exception:
        pass

@app.on_message(
    filters.command(
        [
            "stopmention",
            "cancel",
            "cancelmention",
            "offmention",
            "mentionoff",
            "cancelall",
        ],
        prefixes=["/", "@"],
    )
)
async def cancelcmd(_, message):
    """Cancel tagging berjalan (Admin only)."""
    if not message.from_user:
        return
    chat_id = message.chat.id
    admin = await is_admin(chat_id, message.from_user.id)
    if not admin:
        return
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("<blockquote><b>Tag all sukses dihentikan der</b></blockquote>")
    else:
        await message.reply_text("<blockquote><b>Gak ada proses berjalan der</b></blockquote>")
        return

__MODULE__ = "Tagall"
__HELP__ = """
<blockquote><b>Admin Only
/tagall [caption+link] - Tag all semua member (caption/link tetap di dalam kutipan, mention dengan emoji random)
/cancel - Cancel tag all yang sedang berjalan der</b></blockquote>
"""
