import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YinsRobot.events import register
from YinsRobot import telethn as tbot

yinzver = "2.0.22"
PHOTO = "https://telegra.ph/file/b852a056a0ee158d08efe.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}), ɪ'ᴀᴍ ɢꜱɪᴅ ✗ ᴍᴜꜱɪᴄ.** \n\n"
  TEXT += f"🐼 **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [ᴀɴᴏɴʏᴍ](https://t.me/AyiinXd)** \n\n"
  TEXT += f"🐼 **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ   :** `{telever}` \n\n"
  TEXT += f"🐼 **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ  :** `{tlhver}` \n\n"
  TEXT += f"🐼 **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ  :** `{pyrover}` \n\n"
  TEXT += f"🐼 **ɢꜱɪᴅ ✗ ᴍᴜꜱɪᴄ ᴠᴇʀsɪᴏɴ :** `{yinzver}` \n\n"
  BUTTON = [[Button.url("📚 ʜᴇʟᴘ", "https://t.me/Goldensid_bot?start=help"), Button.url("👨‍🔧 ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/+_BCbzO9Vt35iZGQ1")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
