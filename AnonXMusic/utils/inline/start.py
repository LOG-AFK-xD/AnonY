

from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ✚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 Hᴇʟᴘ 🔧", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="📨 Cʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Mᴀɪɴᴛᴀɪɴᴇʀ 👤", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="💁‍♀ Cʜᴀᴛᴛɪɴɢ Hᴜʙ 👨‍🎨", url=config.SUPPORT_GROUP
            )
        ],
     ]
    return buttons
