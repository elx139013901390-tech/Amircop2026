from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters

WELCOME_TEXT = """
🎉 خوش آمدی {name}

👋 به گروه خوش اومدی.

قوانین گروه را رعایت کن.
"""

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.new_chat_members:
        return

    for user in update.message.new_chat_members:
        await update.message.reply_text(
            WELCOME_TEXT.format(name=user.first_name)
        )

welcome_handler = MessageHandler(
    filters.StatusUpdate.NEW_CHAT_MEMBERS,
    welcome
)
