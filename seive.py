from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
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


async def handle_dice(client: Client, message: Message):
    await message.reply("充值")

async def handle_document(client: Client, message: Message):
    await bot.send_message(
                    chat_id=message.chat.id,
                    text="<b>🎉🎉🎉🎉🎉开始下注🎉🎉🎉🎉🎉</b>\n 60秒一局，买大小、单双数",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("余额", callback_data="balance"),
                                InlineKeyboardButton("玩法", callback_data="gameplay"),
                            ],
                            [
                                InlineKeyboardButton("充值", callback_data="recharge"),
                                InlineKeyboardButton("今日报表", callback_data="daily_report"),
                            ],
                            [
                                InlineKeyboardButton("推广查询", callback_data="promotion_query")
                            ]
                        ]
                    )
                )

# 创建一个回调函数，用于处理/start命令
def start_command_handler(client: Client, message: Message):
    # 发送一个包含"你好"的对话框
    client.send_message(
        chat_id=message.chat.id,
        text="<b>🎉🎉🎉🎉🎉开始下注🎉🎉🎉🎉🎉</b>\n 60秒一局，买大小、单双数",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("余额", callback_data="balance"),
                                InlineKeyboardButton("玩法", callback_data="gameplay"),
                            ],
                            [
                                InlineKeyboardButton("充值", callback_data="recharge"),
                                InlineKeyboardButton("今日报表", callback_data="daily_report"),
                            ],
                            [
                                InlineKeyboardButton("推广查询", callback_data="promotion_query")
                            ]
                        ]
                    )
                )
@bot.on_message()
async def echo(client: Client, message: Message):
    text = message.text.lower()
    if "玩" in text:
        await handle_document(client, message)
    elif "充值" in text:
        await handle_dice(client, message)
    elif "封单" in text:
        await bot.send_dice(chat_id=message.chat.id)

bot.start(start_command_handler)
bot.run()

