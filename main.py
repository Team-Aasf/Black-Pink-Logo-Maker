import os
import logging

from pyrogram import *
from pyrogram.types import *
from blackpink import blackpink

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# For Local Deploy:
"""
API_ID = "14676558"
API_HASH = "b3c4bc0ba6a4fc123f4d748a8cc39981"
TOKEN = "5934089414:AAEdFcMJCvm7Xba6Pa9j8pBZ-3qsYWXFno0"
"""
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("TOKEN", None)

app = Client(
    "Blink" ,
    api_id = API_ID ,
    api_hash = API_HASH ,
    bot_token = TOKEN
)
me = app.get_me()
BOT_USERNAME = me.username

textt = """
**Welcome {}**

`I Am A Telegram Bot, Created Using Python Language`

**What Can This Bot Do ?**

• `I Can Convert Text Into BlackPink's Logo`

**How To Do It ?**

• `Just Send Me The Text & Wait For Some Seconds And Your Logo Will Be Ready !`

**Who Is Your Creator ?**

`My Creator Is M.Kishore/AasfCyberKing` [\u2060]({})
"""

@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    buttons = [[
        InlineKeyboardButton("Developer 👨‍💻", url="https://telegram.me/Aasf_CyberKing"),
    ]]
    await message.reply_text(textt.format(message.from_user.mention, "https://graph.org/file/5b5b8ca1f681bb8b7f6ba.jpg"), reply_markup=InlineKeyboardMarkup(buttons))

@app.on_message(filters.private)
async def logo(_, message):
    if not message.text:
        await message.reply_text("`Please Send A Text To Create Logo.`")
    if message.text and not message.text == "/start":
        filename = f"{message.text}.png"
        blackpink(message.text).save(filename)
        await app.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)
        await message.reply_photo(filename, caption=f"`Preview Of {filename}`")
        await app.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)
        await message.reply_document(filename, caption=f"**{filename}**")
        os.remove(filename)

app.run()
# Credits Logger
print(
    f"[{BOT_USERNAME}] Black Pink Logo Maker Is Starting. | Aasf • Cyber • King • Project | Licensed Under GPLv3."
)
print(f"[{BOT_USERNAME}] Project Maintained By: github.com/AasfCyberKing (t.me/Aasf_CyberKing)")

print(f"[{BOT_USERNAME}] Is Alive")
