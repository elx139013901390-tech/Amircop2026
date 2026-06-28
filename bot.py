from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN, START_TEXT

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_TEXT)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")

    app.run_polling()

if __name__ == "__main__":
    main()
from telegram.ext import MessageHandler, filters

GIF_LOCK = True

async def block_gif(update, context):
    if not GIF_LOCK:
        return

    member = await context.bot.get_chat_member(
        update.effective_chat.id,
        update.effective_user.id
    )

    if member.status in ["administrator", "creator"]:
        return

    await update.message.delete()

app.add_handler(
    MessageHandler(filters.ANIMATION, block_gif)
)
from filters import link_handler

app.add_handler(link_handler)
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from locks import lock, unlock

async def lock_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = await context.bot.get_chat_member(
        update.effective_chat.id,
        update.effective_user.id
    )

    if member.status not in ["administrator", "creator"]:
        return

    if not context.args:
        await update.message.reply_text("مثال:\n/lock gif")
        return

    if lock(context.args[0]):
        await update.message.reply_text("🔒 قفل فعال شد.")
    else:
        await update.message.reply_text("❌ گزینه نامعتبر است.")

async def unlock_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = await context.bot.get_chat_member(
        update.effective_chat.id,
        update.effective_user.id
    )

    if member.status not in ["administrator", "creator"]:
        return

    if not context.args:
        await update.message.reply_text("مثال:\n/unlock gif")
        return

    if unlock(context.args[0]):
        await update.message.reply_text("🔓 قفل غیرفعال شد.")
    else:
        await update.message.reply_text("❌ گزینه نامعتبر است.")

app.add_handler(CommandHandler("lock", lock_cmd))
app.add_handler(CommandHandler("unlock", unlock_cmd))
