import os
import asyncio
import websockets
from pyrogram import Client, idle

proxy = {
    "scheme": "socks5", 
    "hostname": "127.0.0.1",
    "port": 1080,
}

bot = Client(
    "tubexerbot",
    api_id=os.environ.get("TELEGRAM_APP_ID"), 
    api_hash=os.environ.get("TELEGRAM_API_HASH"),
    bot_token=os.environ.get("TELEGRAM_BOT_TOKEN"),
    # 非中国区用户需要注释掉下面这行
    proxy= proxy
)

async def echo(websocket, path):
    async for message in websocket:
        await bot.send_message(chat_id=os.environ.get("TELEGRAM_BOT_TOKEN"),text=message)

bot.start()

start_server = websockets.serve(echo, "localhost", 8887)

asyncio.get_event_loop().run_until_complete(start_server)
idle()  

