from random import choice as c
from time import sleep as s

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

bot = "@MissElisaBot"
start = "Hi Boss "
ERRORS = ["**sed**", "U Are Not A Valid Human", "U Are Not Permiteed", "Chal Phut"]
end = "....\nThis Is Ur Personal Assistant : Jarvis....I am Here To Help U With Ur Daily Works.."
Vid = [
    "/videos__page1",
    "/videos__page2",
    "/videos__page3",
    "/videos__page4",
    "/videos__page5",
    "/videos__page6",
    "/videos__page7",
    "/videos__page8",
    "/videos__page10",
]


@borg.on(admin_cmd("jav ?(.*)"))
async def blue_devil_jarvis(cmd):
    sysarg = cmd.pattern_match.group(1)
    if "hi" in sysarg or "hel" in sysarg:
        async with borg.conversation(bot) as x:
            try:
                await x.send_message(f"/tts {start} {str(ALIVE_NAME)} {end}")
                h_audio = await x.get_response()
                await borg.send_message(cmd.chat_id, h_audio)
                await cmd.delete()
            except YouBlockedUserError:
                await cmd.edit(f"**Error:** `unblock` {bot} `and retry!`")
    elif "me" in sysarg:
        async with borg.conversation("@Cryptowhalebot") as y:
            try:
                await y.send_message(f"/start")
                s(1)
                await y.send_message(f"/meme")
                meme = await y.get_response()
                await cmd.client.send_file(
                    cmd.chat_id,
                    meme,
                    caption="<< Here's Your Carbon Boi,\nCarbonised By [IndianBot](https://www.github.com/indianbhaiya/IndianBot)>> ",
                    force_document=True,
                )
                await cmd.delete()
            except YouBlockedUserError:
                await cmd.edit(c(ERRORS))
    elif "porn" in sysarg:
        async with borg.conversation("@Maal_Supplier_Robot") as z:
            try:
                await cmd.delete()
                await z.send_message(f"/start")
                s(1)
                await z.send_message(c(Vid))
                await z.get_response()
                await z.get_response()
                await z.get_response()
                p_vid = await z.get_response()
                await borg.send_message(cmd.chat_id, p_vid)
                await cmd.delete()
            except YouBlockedUserError:
                await cmd.edit(c(ERRORS))
    else:
        await cmd.edit(c(ERRORS))
