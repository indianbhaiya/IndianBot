from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="test ?(.*)", allow_sudo=True))
async def test(event):
    chat = await event.get_chat()
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await borg.send_message(chat, "Test Successfull. Ja Ja Gand mara")
