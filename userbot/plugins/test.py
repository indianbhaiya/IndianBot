from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="test ?(.*)", allow_sudo=True))
async def test(event):
    if event.fwd_from:
        return 
    await event.reply("Test Successfull. Ja Ja Gand mara")
