# Background Remover Telegram Bot

A Telegram bot that removes backgrounds from images using AI-powered background removal.

## Features

- 📸 Remove backgrounds from any image
- 🤖 Simple and easy to use
- ✨ High-quality background removal
- 📱 Works directly in Telegram

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables (SECURITY)

**⚠️ IMPORTANT: Never commit your API keys to version control!**

1. **Create a `.env` file** in the telegram-bot directory:

   ```bash
   cp env_example.txt .env
   ```

2. **Edit the `.env` file** with your actual API keys:

   ```env
   # Telegram Bot Token
   BOT_TOKEN=your_actual_telegram_bot_token

   # Remove.bg API Key
   REMOVE_BG_API_KEY=your_actual_remove_bg_api_key
   ```

3. **Get your API keys:**
   - **Telegram Bot Token**: Get from @BotFather on Telegram
   - **Remove.bg API Key**: Sign up at https://www.remove.bg/api (50 free calls/month)

### 3. Run the Bot

```bash
python sokSaoBot.py
```

## How to Use

1. Start the bot with `/start`
2. Send any photo to the bot
3. Wait for processing
4. Receive the image with background removed

## Commands

- `/start` - Welcome message and instructions
- `/help` - Show available commands
- `/about` - About the bot

## Technical Details

The bot uses two methods for background removal:

1. **remove.bg API** (Recommended): Professional AI-powered background removal
2. **Simple PIL method**: Basic background removal for white/light backgrounds

## Security Best Practices

### 🔐 API Key Security

1. **Never commit `.env` files** to version control
2. **Use environment variables** instead of hardcoding API keys
3. **Keep your API keys private** - don't share them publicly
4. **Rotate API keys regularly** if compromised
5. **Use different API keys** for development and production

### 🛡️ Additional Security Measures

- **Rate limiting**: Consider implementing rate limiting to prevent abuse
- **Input validation**: Validate image files before processing
- **Error handling**: Don't expose sensitive information in error messages
- **Logging**: Be careful not to log API keys or sensitive data

## Troubleshooting

- **"Error processing image"**: Make sure you have a valid API key or try a different image
- **"Couldn't process your image"**: The image might be too large or in an unsupported format
- **Bot not responding**: Check your internet connection and bot token
- **"No API key found"**: Make sure your `.env` file exists and contains the correct API keys

## File Structure

```
telegram-bot/
├── sokSaoBot.py      # Main bot code
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## License

This project is open source and available under the MIT License.
