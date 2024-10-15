from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Define a start command handler to greet the user
async def start(update: Update, context) -> None:
    await update.message.reply_text("Hello! I am a simple bot. Send me any message and I'll reply!")

# Define a message handler to reply to any text message
async def echo(update: Update, context) -> None:
    await update.message.reply_text(f'You said: {update.message.text}')

# Main function to start the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
    application = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()

    # Add handlers for start command and message handling
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
