from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

BOT_TOKEN = ''

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f'Hello, {user.first_name}! 👋\n'
        'I am SokSaoBot. Type /help to see what I can do!'
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are my commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help message\n"
        "/about - About this bot\n"
        "/joke - Get a random joke"
    )

# /about command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 SokSaoBot v1.0\n"
        "Created to make your day better with jokes and info!"
    )

# /joke command
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Why did the Python programmer go broke? Because he couldn't C#!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer show up at work late? It had a hard drive!",
        "Why do Java developers wear glasses? Because they don't see sharp."
    ]
    await update.message.reply_text(random.choice(jokes))

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("joke", joke))
    app.run_polling()
