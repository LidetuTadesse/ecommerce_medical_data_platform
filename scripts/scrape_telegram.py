import os
import json
from datetime import datetime
from telethon import TelegramClient
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

# Channels to scrape
channels = [
    'lobelia4cosmetics',
    'tikvahpharma',
    # add more channels as needed
]

# Directory to save raw JSON data
BASE_DIR = 'data/raw/telegram_messages'

client = TelegramClient('session_name', api_id, api_hash)

async def scrape_channel(channel):
    logger.info(f"Starting scrape for {channel}")
    await client.start()
    messages = []
    async for message in client.iter_messages(channel, limit=None):
        # Convert message to dict (some fields might not be JSON serializable, handle carefully)
        msg_dict = {
            "id": message.id,
            "date": message.date.isoformat(),
            "message": message.message,
            "media": str(message.media) if message.media else None,
            # add other fields as necessary
        }
        messages.append(msg_dict)
    
    # Prepare save path
    today = datetime.utcnow().strftime('%Y-%m-%d')
    os.makedirs(f"{BASE_DIR}/{today}", exist_ok=True)
    file_path = f"{BASE_DIR}/{today}/{channel}.json"

    # Save JSON
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)
    
    logger.info(f"Saved {len(messages)} messages from {channel} to {file_path}")

async def main():
    await client.start()
    for channel in channels:
        try:
            await scrape_channel(channel)
        except Exception as e:
            logger.error(f"Error scraping {channel}: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
