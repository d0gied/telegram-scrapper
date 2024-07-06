from pyrogram import filters
from pyrogram.client import Client
from pyrogram import types
from pyrogram.enums import ParseMode
from ..config import Config
from .utils import get_folder_chats, match_message

api_id = 993165
api_hash = "7063053ef3e442ebcbae764e70841481"

app = Client(
    "my_account",
    api_id=Config.Pyrogram.API_ID,
    api_hash=Config.Pyrogram.API_HASH
)

@app.on_message(filters.all)
async def scrap(client: Client, message: types.Message):
    chat_id = message.chat.id
    if chat_id not in await get_folder_chats(client):
        return

    user = message.from_user
    chat = message.chat
    text = message.text

    if not match_message(text):
        return

    msg_text = ""
    if chat and chat.title != None:
        msg_text += f"Chat: [{chat.title}](tg://chat?id={chat.id})\n"
    msg_text += f"User: [{user.username}](tg://user?id={user.id})\n"
    msg_text += f"\nText: {text}"
    for admin in Config.ADMINS:
        await client.send_message(
            chat_id=admin,
            text=msg_text,
            parse_mode=ParseMode.MARKDOWN
        )
        try:
            await message.forward(admin)
        except Exception as e:
            print(e)
