"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@EYEGANG_XD @NETFLIX_NETHAX "

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`JINDA HU EYE GANG MEMBERS`**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nFork by:` @EYEGANG_XD\n"
                     "`My creater is:` [EYE GANG XD](tg://user?id=1036393307)\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, My master!\n`"
                     f"`My sir`: {DEFAULTUSER} \n"
                     "[JOIN OUR CHANNEL](https://t.me/netflix_nethax)")
