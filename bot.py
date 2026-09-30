import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 Welcome to Empire Rise!\n\n"
        "Your empire is ready to rise.\n\n"
        "Use /empire to view your empire."
    )


async def empire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 YOUR EMPIRE\n\n"
        "🏰 Castle: Level 1\n"
        "🪙 Gold: 1,000\n"
        "🪵 Wood: 500\n"
        "🪨 Stone: 250\n"
        "🌾 Food: 300\n\n"
        "⚔️ Power: 100"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("empire", empire))

    app.run_polling()


if __name__ == "__main__":
    main()
