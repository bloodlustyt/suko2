#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 4796990
API_HASH = "32b6f41a4bf740efed2d4ce911f145c7"
BOT_TOKEN = "5677533386:AAG0fSL7e2bonE1IhKTtIY3bY3hzvDstPl0"
SESSION = "AQBTMDYE5w6yxKcKgAJTgotMEgFUlKoe6k_5FVuOh330m39DT0QZYvIwiXFYz_FHkCEZ-e3GY9emkvuUFJIWPb9Nex8vZ48qLa2fURJSE4YXuWZBXEwzRZ_E3Hqt_QncRTeugE51C4PgzXCFc1fvdXxwa-HcBzdqqIEiEmEZEg_9CgyuloDrl8gcijakXxeKLVLJqnRr4THI09lcVGF2Yk9ldVNb7Wy0h9ctg6wiPP-e4OXD9a963TleCegr4Q_PrAXDeRxxuyv1oyIZx4iTQIyIf7Z0MZ3WjfV0dyjZW4k_qq5_1awHyz3uQWYjiqi4C6a9xWiXbGbyQH6D-_Xo7rM5Uuuy0AA"
FORCESUB = "loltestingbikni"
AUTH = 5351121397

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
