from telegram.ext import MessageHandler, filters

LOCKS = {
    "gif": True,
    "sticker": True,
    "photo": True,
    "video": True,
    "document": True,
    "voice": True,
}

async def media_filter(update, context):
    if not update.message:
        return

    member = await context.bot.get_chat_member(
        update.effective_chat.id,
        update.effective_user.id
    )

    if member.status in ["administrator", "creator"]:
        return

    msg = update.message

    if msg.animation and LOCKS["gif"]:
        await msg.delete()

    elif msg.sticker and LOCKS["sticker"]:
        await msg.delete()

    elif msg.photo and LOCKS["photo"]:
        await msg.delete()

    elif msg.video and LOCKS["video"]:
        await msg.delete()

    elif msg.document and LOCKS["document"]:
        await msg.delete()

    elif msg.voice and LOCKS["voice"]:
        await msg.delete()


handlers = [
    MessageHandler(filters.ALL, media_filter)
]
import re
from telegram.ext import MessageHandler, filters

LINK_REGEX = re.compile(
    r"(https?://\S+|t\.me/\S+|telegram\.me/\S+|@\w+)",
    re.IGNORECASE,
)

async def anti_link(update, context):
    if not update.message or not update.message.text:
        return

    member = await context.bot.get_chat_member(
        update.effective_chat.id,
        update.effective_user.id
    )

    if member.status in ["administrator", "creator"]:
        return

    if LINK_REGEX.search(update.message.text):
        await update.message.delete()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"🚫 {update.effective_user.first_name} ارسال لینک در این گروه ممنوع است."
        )

link_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, anti_link)
