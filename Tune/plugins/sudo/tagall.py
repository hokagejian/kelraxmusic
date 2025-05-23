import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
from Tune import app

SPAM_CHATS = []

WATERMARK = (
    "𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄂\n"
    "ᴄᴏᴘʏʀɪɢʜᴛ ᴋᴇʟʀᴀᴄᴏᴅᴇʀ"
)

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
    if not message.from_user:
        return
    admin = await is_admin(message.chat.id, message.from_user.id)
    if not admin:
        return

    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "Tag all sedang berjalan der, ketik /cancel untuk membatalkan der"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "Kasih teks nya der\n/tagall Hi Kelra Music"
        )
        return
    if replied:
        usernum = 0
        usertxt = ""
        try:
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})  "
                if usernum == 7:
                    sent = await replied.reply_text(
                        usertxt,
                        disable_web_page_preview=True,
                    )
                    await app.send_message(message.chat.id, WATERMARK, reply_to_message_id=sent.id)
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                sent = await replied.reply_text(
                    usertxt,
                    disable_web_page_preview=True,
                )
                await app.send_message(message.chat.id, WATERMARK, reply_to_message_id=sent.id)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        try:
            usernum = 0
            usertxt = ""
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})  "
                if usernum == 7:
                    sent = await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await app.send_message(message.chat.id, WATERMARK, reply_to_message_id=sent.id)
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                sent = await app.send_message(
                    message.chat.id,
                    f"{text}\n{usertxt}",
                    disable_web_page_preview=True,
                )
                await app.send_message(message.chat.id, WATERMARK, reply_to_message_id=sent.id)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass

async def tag_all_admins(_, message):
    if not message.from_user:
        return
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "Tag all sedang berjalan der\nKetik /cancel untuk membatalkan der"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "Kasih teks nya der\n/admins min lapor min"
        )
        return
    if replied:
        usernum = 0
        usertxt = ""
        try:
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})  "
                if usernum == 7:
                    sent = await replied.reply_text(
                        usertxt,
                        disable_web_page_preview=True,
                    )
                    await app.send_message(message.chat.id, WATERMARK, reply_to_message_id=sent.id)
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                sent = await replied.reply_text(
                    usertxt,
                    disable_web_page_preview=True,
                )
                await app.send_message(message.chat.id, WATERMARK, reply_to_message_id=sent.id)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        usernum = 0
        usertxt = ""
        try:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})  "
                if usernum == 7:
                    sent = await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await app.send_message(message.chat.id, WATERMARK, reply_to_message_id=sent.id)
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                sent = await app.send_message(
                    message.chat.id,
                    f"{text}\n{usertxt}",
                    disable_web_page_preview=True,
                )
                await app.send_message(message.chat.id, WATERMARK, reply_to_message_id=sent.id)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass

@app.on_message(
    filters.command(["admin", "admins", "report"], prefixes=["/"]) & filters.group
)
async def admintag_with_reporting(client, message):
    if not message.from_user:
        return
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    admins = [
        admin.user.id
        async for admin in client.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        )
    ]
    if message.command[0] == "report":
        if from_user_id in admins:
            return await message.reply_text(
                "Lu itu admin der ngapain report\nTindak aja langsung der"
            )

    if from_user_id in admins:
        return await tag_all_admins(client, message)

    if len(message.text.split()) <= 1 and not message.reply_to_message:
        return await message.reply_text(
            "Reply ke pesan untuk report user tersebut."
        )

    reply = message.reply_to_message or message
    reply_user_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
    linked_chat = (await client.get_chat(chat_id)).linked_chat
    if reply_user_id == app.id:
        return await message.reply_text(
            "Lu report siapa der?, angin?"
        )
    if (
        reply_user_id in admins
        or reply_user_id == chat_id
        or (linked_chat and reply_user_id == linked_chat.id)
    ):
        return await message.reply_text(
            "Lu tau yang lu report admin der?"
        )

    user_mention = reply.from_user.mention if reply.from_user else "the user"
    text = f"Bocah ini : {user_mention}\nDilaporkan ke admin."

    for admin in admins:
        admin_member = await client.get_chat_member(chat_id, admin)
        if not admin_member.user.is_bot and not admin_member.user.is_deleted:
            text += f" [\u2063](tg://user?id={admin})"

    await reply.reply_text(text)

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
        return await message.reply_text(
            "Tag all sukses dihentikan der"
        )
    else:
        await message.reply_text(
            "Gak ada proses berjalan der"
        )
        return

__MODULE__ = "Tagall"
__HELP__ = """
Admin Only
/tagall - Tag all semua member grup lu der
/admins - Tag all semua admin grup der
/report - Report member tengil der [khusus member] 
/cancel - Cancel tag all yang sedang berjalan der
"""
