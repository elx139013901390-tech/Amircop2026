from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from telegram.constants import ChatMemberStatus

async def kick(update: Update, context: ContextTypes.DEFAULT_TYPE):

    member = await context.bot.get_chat_member(
        update.effective_chat.id,
        update.effective_user.id
    )

    if member.status not in (
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER,
    ):
        return

    if not update.message.reply_to_message:
        await update.message.reply_text(
            "روی پیام کاربر ریپلای کن."
        )
        return

    user = update.message.reply_to_message.from_user

    await context.bot.ban_chat_member(
        update.effective_chat.id,
        user.id
    )

    await context.bot.unban_chat_member(
        update.effective_chat.id,
        user.id
    )

    await update.message.reply_text(
        f"👢 {user.first_name} از گروه اخراج شد."
    )

kick_handler = CommandHandler("kick", kick)
