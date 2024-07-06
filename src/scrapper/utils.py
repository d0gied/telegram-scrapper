from pyrogram.client import Client
from pyrogram.raw.functions.messages.get_dialog_filters import GetDialogFilters
from pyrogram.raw.types.dialog_filter import DialogFilter
from pyrogram.raw.types.dialog_filter_default import DialogFilterDefault
from pyrogram.raw.types.input_peer_chat import InputPeerChat
from pyrogram.raw.types.input_peer_channel import InputPeerChannel
from pyrogram.raw.types.input_peer_user import InputPeerUser

from Levenshtein import distance

from ..config import Config

async def get_folder_chats(client: Client, folder_name: str = Config.FOLDER_NAME) -> list[int]:
    folders: list[dict] = await client.invoke(
        GetDialogFilters()
    )
    chat_ids = []
    for folder in folders:
        if isinstance(folder, DialogFilterDefault):
            continue
        if isinstance(folder, DialogFilter):
            if folder.title == folder_name:
                for peer in folder.include_peers:
                    if isinstance(peer, InputPeerUser):
                        chat_ids.append(peer.user_id)
                    elif isinstance(peer, InputPeerChat):
                        chat_ids.append(-peer.chat_id)
                    elif isinstance(peer, InputPeerChannel):
                        chat_ids.append(-peer.channel_id)
    return chat_ids

KEYWORDS =  [
    "привет",
    "hello",
    "hi",
    "hey",
    "пока",
    "bye",
    "goodbye",
]

import re

def match_message(message: str) -> bool:
    msg = message.lower()
    msg = re.sub(r"[^а-яa-z0-9 ]", "", msg) # Remove all non-alphanumeric characters
    msg = re.sub(r"\s+", " ", msg) # Remove extra spaces
    msg = msg.strip()
    msg = msg.split()

    for keyword in KEYWORDS:
        words = len(keyword.split())
        for i in range(len(msg) - words + 1):
            if distance(" ".join(msg[i:i + words]), keyword) <= 1:
                print(f"Matched: {msg[i:i + words]} -> {keyword} ({distance(' '.join(msg[i:i + words]), keyword)})")
                return True
    return False
