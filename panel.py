from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes
from locks import LOCKS

def menu():
    keyboard = [
        [
            InlineKeyboardButton("🔒 گیف", callback_data="gif"),
            InlineKeyboardButton("🖼 عکس", callback_data="photo"),
        ],
        [
            InlineKeyboardButton("🎥 ویدیو", callback_data="video"),
            InlineKeyboardButton("📄 فایل", callback_data="document"),
        ],
        [
            InlineKeyboardButton("🎙 ویس", callback_data="voice"),
            InlineKeyboardButton("😀 استیکر", callback_data="sticker"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = await context.bot.get_chat_member(
        update.effective_chat.id,
        update.effective_user.id
    )

    if member.status not in ["administrator", "creator"]:
        return

    await update.message.reply_text(
        "⚙️ پنل مدیریت",
        reply_markup=menu()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    name = query.data

    LOCKS[name] = not LOCKS[name]

    if LOCKS[name]:
        text = f"🔒 قفل {name} فعال شد."
    else:
        text = f"🔓 قفل {name} غیرفعال شد."

    await query.edit_message_text(
        text,
        reply_markup=menu()
    )


panel_handler = CommandHandler("panel", panel)
button_handler = CallbackQueryHandler(buttons)
