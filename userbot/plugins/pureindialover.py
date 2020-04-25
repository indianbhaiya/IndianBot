"""Emoji
Available Commands:
.pureindialover
Credits to @pureindialover
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("pureindialover"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "pureindialover":
    await event.edit("@pureindialover")
    animation_chars = [
            "@pureindialover tera baap",
            "@pureindialover is bot ka creator",
            "@pureindialover bot ko jaan dene wala",
            "@pureindialover owner of @IndianArMyGiveaway ",
            "tujhe aur kya chaiye vo hai mere sath",
            "tera baap",
            "@pureindialover"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
