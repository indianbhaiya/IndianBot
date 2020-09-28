import glob
import os

from userbot.utils import admin_cmd

try:
    pass
except ImportError:
    os.system("pip install instantmusic")
    import subprocess
os.system("rm -rf *.mp3")


def bruh(name):
    os.system("instantmusic -q -s " + name)


@borg.on(admin_cmd(pattern="song ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit("ok finding the song")
    bruh(str(cmd))
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("sending song")
    await borg.send_file(
        event.chat_id,
        loa,
        force_document=True,
        allow_cache=False,
        caption=cmd,
        reply_to=reply_to_id,
    )
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3", shell=True)
