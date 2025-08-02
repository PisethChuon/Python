from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
REMOVE_BG_API_KEY = os.getenv("REMOVE_BG_API_KEY")

# Validate required environment variables
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required")
if not REMOVE_BG_API_KEY:
    print("Warning: REMOVE_BG_API_KEY not found. Will use simple background removal.")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f'Hello, {user.first_name}! 👋\n'
        'I am Background Remover Bot! 📸\n'
        'Just send me a photo and I\'ll remove the background for you!\n'
        'Type /help to see what I can do!'
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are my commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help message\n"
        "/about - About this bot\n\n"
        "📸 **How to use:**\n"
        "Simply send me any photo and I'll remove the background for you!"
    )

# /about command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Background Remover Bot v2.0\n"
        "Created to help you remove backgrounds from images easily!\n"
        "Just upload a photo and get a clean image with no background."
    )

# /test command to check if bot is working
async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot is working! Send me a photo to remove its background.\n\n"
        "📸 **How to test:**\n"
        "1. Send any photo to this chat\n"
        "2. Wait for processing\n"
        "3. Get your image with background removed!"
    )

# Handle photo messages
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Send a processing message
        processing_msg = await update.message.reply_text("🔄 Processing your image... Please wait.")
        
        # Get the largest photo size
        photo = update.message.photo[-1]
        
        # Download the photo
        file = await context.bot.get_file(photo.file_id)
        photo_data = await file.download_as_bytearray()
        
        # Remove background using remove.bg API (free tier available)
        # You'll need to sign up at https://www.remove.bg/api
        removed_bg_image = await remove_background(photo_data)
        
        if removed_bg_image:
            # Send the processed image
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=removed_bg_image,
                caption="✨ Background removed successfully!"
            )
            await processing_msg.delete()
        else:
            await processing_msg.edit_text("❌ Sorry, I couldn't process your image. Please try again with a different photo.")
            
    except Exception as e:
        await update.message.reply_text(f"❌ Error processing image: {str(e)}")

async def remove_background(image_data: bytes) -> io.BytesIO:
    """
    Remove background from image using remove.bg API.
    Falls back to simple removal if API is unavailable.
    
    Args:
        image_data: Raw image bytes
        
    Returns:
        BytesIO object containing processed image, or None if failed
    """
    try:
        # Use the API key from environment variables
        api_key = REMOVE_BG_API_KEY
        
        # Check if API key is available
        if not api_key:
            print("No remove.bg API key found. Using simple background removal instead.")
            return await simple_background_removal(image_data)
        
        url = "https://api.remove.bg/v1.0/removebg"
        
        headers = {
            'X-Api-Key': api_key,
        }
        
        files = {
            'image_file': ('image.jpg', image_data, 'image/jpeg')
        }
        
        print("Calling remove.bg API...")
        response = requests.post(url, headers=headers, files=files)
        
        if response.status_code == 200:
            print("Background removal successful!")
            return io.BytesIO(response.content)
        else:
            print(f"API Error: {response.status_code}, {response.text}")
            # Fallback to simple method if API fails
            print("Falling back to simple background removal...")
            return await simple_background_removal(image_data)
            
    except Exception as e:
        print(f"Error removing background: {e}")
        # Fallback to simple method if any error occurs
        print("Falling back to simple background removal...")
        return await simple_background_removal(image_data)

async def simple_background_removal(image_data: bytes) -> io.BytesIO:
    """
    Simple background removal using PIL (basic implementation).
    Removes white/light colored backgrounds by making them transparent.
    
    Args:
        image_data: Raw image bytes
        
    Returns:
        BytesIO object containing processed image, or None if failed
    """
    try:
        print("Using simple background removal method...")
        # Open the image
        image = Image.open(io.BytesIO(image_data))
        
        # Convert to RGBA if not already
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        # Get image data
        data = image.getdata()
        
        # Create new image data with transparent background for light pixels
        new_data = []
        for pixel in data:
            # Make white/light pixels transparent
            is_light = (pixel[0] > 220 and pixel[1] > 220 and pixel[2] > 220)
            is_similar_colors = (abs(pixel[0] - pixel[1]) < 10 and 
                               abs(pixel[1] - pixel[2]) < 10 and 
                               abs(pixel[0] - pixel[2]) < 10)
            
            if is_light or is_similar_colors:
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(pixel)
        
        # Create new image
        new_image = Image.new('RGBA', image.size)
        new_image.putdata(new_data)
        
        # Save to bytes
        output = io.BytesIO()
        new_image.save(output, format='PNG')
        output.seek(0)
        
        print("Simple background removal completed!")
        return output
        
    except Exception as e:
        print(f"Error in simple background removal: {e}")
        return None

def main():
    """Main function to start the bot."""
    if not BOT_TOKEN:
        print("❌ Error: BOT_TOKEN not found in environment variables")
        return
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("test", test))
    
    # Add photo handler
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    print("🤖 Background Remover Bot is starting...")
    print("📸 Send photos to remove backgrounds!")
    app.run_polling()

if __name__ == '__main__':
    main()
