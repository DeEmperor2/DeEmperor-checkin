import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 Welcome to DeEmperor Checkin!\n\nI'll help you stay on track daily with check-ins and reminders.")

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Today's Schedule:\n"
        "- 6:30 AM: Workout\n"
        "- 7:00 AM: Duolingo (5 mins)\n"
        "- 7:10 AM: Get ready for work\n"
        "- 9:00 AM – 5:00 PM: Work\n"
        "- 5:30 PM: Chess lesson\n"
        "- 6:30 PM: Break\n"
        "- 7:00 PM: Coding\n"
        "- 9:00 PM: Movie\n"
        "- 11:00 PM: Sleep 💤"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("schedule", schedule))

if __name__ == "__main__":
    app.run_polling()
# Redeploy trigger
