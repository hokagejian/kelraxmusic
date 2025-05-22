from pyrogram import filters
from pyrogram.types import Message
from Tune import app
import re

ANKES_STATE = {}
BLACKLIST = {}
FREE_USERS = {}

# Helper untuk admin group
async def is_admin(client, message: Message):
    if not message.from_user:
        return False
    user_id = message.from_user.id
    chat_member = await app.get_chat_member(message.chat.id, user_id)
    return chat_member.status in ("administrator", "creator")
admin_filter = filters.create(is_admin)

def is_ankes_on(chat_id):
    return ANKES_STATE.get(chat_id, False)

def add_to_blacklist(chat_id, word):
    BLACKLIST.setdefault(chat_id, set()).add(word.lower())

def remove_from_blacklist(chat_id, word):
    BLACKLIST.setdefault(chat_id, set()).discard(word.lower())

def get_blacklist(chat_id):
    return BLACKLIST.get(chat_id, set())

def add_free_user(chat_id, user_id):
    FREE_USERS.setdefault(chat_id, set()).add(user_id)

def remove_free_user(chat_id, user_id):
    FREE_USERS.setdefault(chat_id, set()).discard(user_id)

def is_free_user(chat_id, user_id):
    return user_id in FREE_USERS.get(chat_id, set())

@app.on_message(filters.command(["ankes"]) & admin_filter & filters.group)
async def ankes_switch(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("💡 Usage: `/ankes on` atau `/ankes off`")
    arg = message.command[1].lower()
    if arg == "on":
        ANKES_STATE[message.chat.id] = True
        await message.reply_text("✅ Mode ANKES ON, blacklist aktif!")
    elif arg == "off":
        ANKES_STATE[message.chat.id] = False
        await message.reply_text("❌ Mode ANKES OFF, blacklist tidak aktif!")
    else:
        await message.reply_text("❌ Pilihan tidak valid. Gunakan `/ankes on` atau `/ankes off`.")

@app.on_message(filters.command(["blacklist", "bl"]) & admin_filter & filters.group)
async def show_blacklist(client, message: Message):
    chat_id = message.chat.id
    bl = get_blacklist(chat_id)
    if not bl:
        await message.reply_text("Tidak ada kata dalam blacklist.")
    else:
        await message.reply_text("Kata blacklist:\n" + "\n".join(f"- {w}" for w in bl))

@app.on_message(filters.command(["addblacklist", "adbl"]) & admin_filter & filters.group)
async def add_blacklist_cmd(client, message: Message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply_text("💡 Contoh: `/addblacklist kata1 kata2` atau `/adbl kata1 kata2`")
    for w in message.command[1:]:
        add_to_blacklist(chat_id, w)
    await message.reply_text("✅ Kata berhasil masuk blacklist!")

@app.on_message(filters.command(["unblacklist", "unbl"]) & admin_filter & filters.group)
async def remove_blacklist_cmd(client, message: Message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply_text("💡 Contoh: `/unblacklist kata1 kata2` atau `/unbl kata1 kata2`")
    for w in message.command[1:]:
        remove_from_blacklist(chat_id, w)
    await message.reply_text("✅ Kata berhasil dihapus dari blacklist!")

@app.on_message(filters.command(["free", "fre"]) & admin_filter & filters.group)
async def free_user_cmd(client, message: Message):
    chat_id = message.chat.id
    user_id = None

    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        arg = message.command[1]
        if arg.isdigit():
            user_id = int(arg)
        else:
            try:
                user = await app.get_users(arg)
                user_id = user.id
            except Exception:
                return await message.reply_text("Username atau ID tidak valid.")
    if not user_id:
        return await message.reply_text("Reply ke pesan user atau kirim id/username setelah /free atau /fre.")
    add_free_user(chat_id, user_id)
    await message.reply_text("User telah dibebaskan dari blacklist.")

@app.on_message(filters.command(["unfree", "unfre"]) & admin_filter & filters.group)
async def unfree_user_cmd(client, message: Message):
    chat_id = message.chat.id
    user_id = None

    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        arg = message.command[1]
        if arg.isdigit():
            user_id = int(arg)
        else:
            try:
                user = await app.get_users(arg)
                user_id = user.id
            except Exception:
                return await message.reply_text("Username atau ID tidak valid.")
    if not user_id:
        return await message.reply_text("Reply ke pesan user atau kirim id/username setelah /unfree atau /unfre.")
    remove_free_user(chat_id, user_id)
    await message.reply_text("User sudah tidak bebas dari blacklist.")

@app.on_message(filters.text & filters.group)
async def auto_delete_blacklist(client, message: Message):
    chat_id = message.chat.id
    if not message.from_user:
        return
    user_id = message.from_user.id

    if not is_ankes_on(chat_id):
        return

    if await is_admin(client, message) or is_free_user(chat_id, user_id):
        return

    bl = get_blacklist(chat_id)
    text = message.text or ""
    for word in bl:
        # Gunakan regex agar hanya match kata utuh
        if re.search(rf"\b{re.escape(word)}\b", text, re.IGNORECASE):
            await message.delete()
            return
