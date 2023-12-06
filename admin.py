from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from dotenv import load_dotenv
import os

load_dotenv()

# Configure proxy if needed
proxy = {
    "scheme": "socks5",
    "hostname": "127.0.0.1",
    "port": 1080,
}

# Initialize bot with your credentials
bot = Client(
    "casino6888bot",
    api_id=os.environ.get("TELEGRAM_APP_ID"),
    api_hash=os.environ.get("TELEGRAM_API_HASH"),
    bot_token=os.environ.get("TELEGRAM_BOT_TOKEN2"),
    proxy=proxy
)

# Function to create a simple inline keyboard button for verification
def verification_keyboard():
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("点击这里证明我不是机器人", callback_data="verify_human")]
        ]
    )
    return keyboard

# New member handler
@bot.on_message(filters.new_chat_members)
async def welcome_new_members(client, message: Message):
    chat_id = message.chat.id
    new_members = message.new_chat_members
    for member in new_members:
        # Send a message with a button for verification
        await bot.send_message(
            chat_id,
            f"欢迎 {member.first_name} 加入卡星诺博彩天堂！请完成下面的验证：",
            reply_markup=verification_keyboard()
        )

@bot.on_callback_query(filters.regex("enterGames"))
async def game_selection(client, callback_query: CallbackQuery):
    await bot.send_message(
        chat_id=callback_query.message.chat.id,
        text="游戏列表",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Goal", callback_data="game_Goal")],
                [InlineKeyboardButton("Head or Tail", callback_data="game_HeadOrTail")],
                [InlineKeyboardButton("FSC", callback_data="game_FSC")],
                [InlineKeyboardButton("Sci-bo", callback_data="game_Scibo")],
                [InlineKeyboardButton("Bingo", callback_data="game_Bingo")],
                # 可以在这里添加更多的游戏按钮
            ]
        )
    )

@bot.on_callback_query(filters.regex(r'^enterMain$'))
async def enter_main(client, callback_query: CallbackQuery):
    # 这里可以编写您希望执行的操作
    # 例如，根据用户选择的语言发送一个新的消息
    language = callback_query.message.reply_markup.inline_keyboard[0][0].text
    if "简体中文" in language:
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="开启您的娱乐之旅吧:",
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("游戏", callback_data="enterGames"),
                                InlineKeyboardButton("充值", callback_data="..."),
                            ],
                             [
                                InlineKeyboardButton("推荐", callback_data="..."),
                                InlineKeyboardButton("设置", callback_data="..."),
                            ],
                             [
                                InlineKeyboardButton("频道", callback_data="..."),
                                InlineKeyboardButton("客服", callback_data="..."),
                            ]
                        ]
            )
        )
    elif "English" in language:
         await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Start your travel:",
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Games", callback_data="enterGames"),
                                InlineKeyboardButton("Recharge", callback_data="..."),
                            ],
                             [
                                InlineKeyboardButton("Recommend", callback_data="..."),
                                InlineKeyboardButton("Settings", callback_data="..."),
                            ],
                             [
                                InlineKeyboardButton("Channel", callback_data="..."),
                                InlineKeyboardButton("Support", callback_data="..."),
                            ]
                        ]
            )
        )
  

# Callback query handler for verification
@bot.on_callback_query(filters.regex("verify_human"))
async def verify_human_callback(client, callback_query: CallbackQuery):
    message = callback_query.message
    from_user = callback_query.from_user
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"谢谢 {from_user.first_name}，您已通过验证！",
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text="Please select your language:",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("简体中文 🇨🇳", callback_data="enterMain"),
                                InlineKeyboardButton("English 🇬🇧", callback_data="enterMain"),
                            ]
                        ]
                    )
        )



# Run the bot
bot.run()
