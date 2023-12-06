from pyrogram import Client
from pyrogram.types import Message
from dotenv import load_dotenv
import os
load_dotenv()
# 这是一个常规机器人，机器人启动后会监听聊天框的消息
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
    proxy=proxy
) 

@bot.on_message()
async def echo(client: Client, message: Message):
    
    await message.reply("message.text")

bot.run()

