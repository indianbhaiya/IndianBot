import userbot.plugins.sql_helper.pmpermit_sql as status
from telethon import functions
from time import sleep as s
from userbot import ALIVE_NAME
@command(pattern=r"\/start", incoming=True)
async def pmpermit_ka_menu(event):
    chat_id = event.from_id
    if not status.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if not event.is_private:
            return
        PM = (f'**@       Hi**\nThis Is Dr.India,\nI Figured Out Ur Way Till Here!!\nU Wanna Talk With : {str(ALIVE_NAME)}\n'
              f'`1`. **For A Chat**\n'
              f'`2`. **To Spam.**\n'
              f'`3`. **For Enquiry.**\n'
              f'`4`. **For A Request**\n'
              f'`5`. **To Contribute**\n')
        ONE = (
            '__Okay. Your Request Has Been **Registered.**\nDo Not Spam This Place. You Can Expect A Reply Within Next 3_Hours__\n\n'
            '**⚠You Will Be Blocked and Reported If U Think Of Spamming⚠**\n\n'
            'Use [/start](t.me//start) To Start From Beginning')
        TWO = (
            '███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀\n\nSry But Due To Ur Bakchodi I Have To **Block** U')
        THREE = (
            '__Okay. \n\nWait For A While He Will Respond Soon Today!!')
        FOUR = (
            'Requests Are **Basically Not Seen** By Him But Still He `May` See')
        FIVE = ('▬▬▬.◙.▬▬▬\n'
                ' ═▂▄▄▓▄▄▂\n'
                '◢◤ █▀▀████▄▄▄▄◢◤\n'
                '█▄ █ █▄ ███▀▀▀▀▀▀▀╬\n'
                '◥█████◤\n'
                '══╩══╩══\n'
                'Hiya Boi! THANKS 😃\n Contribute Whatever U Want! \n I Am Glad For u Boi🔜\n. ◌⑅⃝●♡⋆♡LOVE♡⋆♡●⑅◌')
        LWARN = (
            "**U Are Exceeding Ur Limit Of Messages!!\n\nOnly One Last Chance Is Left With U**")
        async with borg.conversation(chat) as conv:
            await borg.send_message(chat, PM)
            chat_id = event.from_id
            s(7)
            r = await conv.get_response(chat)
            y = r.text
            if '1' in y:
                await borg.send_message(chat, ONE)
                q = await conv.get_response(chat)
                await event.delete()
                if not q.text == "/start":
                    await q.delete()
                    await borg.send_message(chat, LWARN)
                    response = await conv.get_response(chat)
                    await event.delete()
                    await response.delete()
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            elif "2" in y:
                await borg.send_message(chat, TWO)
                async with borg.conversation('@chalhatibhenkilodibot') as n:
                    await n.send_message('/start')
                    s(1)
                    await n.send_message('/sendmethesong')
                    a = await n.get_response()
                    await borg.send_message(chat , a)
                await event.client(functions.contacts.BlockRequest(chat_id))
            elif "3" in y:
                await borg.send_message(chat, THREE)
                q = await conv.get_response(chat)
                await event.delete()
                await q.delete()
                if '/start' not in q.text:
                    await borg.send_message(chat, LWARN)
                    await event.delete()
                    response = await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            elif "4" in y:
                await borg.send_message(chat, FOUR)
                q = await conv.get_response(chat)
                if '/start' not in q.text:
                    await borg.send_message(chat, LWARN)
                    r2 = await conv.get_response(chat)
                    if '/start' not in r2.text:
                        await borg.send_message(chat, TWO)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            elif "5" in y:
                await borg.send_message(chat, FIVE)
                q = await conv.get_response(chat)
                if '/start' not in q.text:
                    await borg.send_message(chat, LWARN)
                    r2 = await conv.get_response(chat)
                    if '/start' not in r2.text:
                        await borg.send_message(chat, TWO)
                        await event.client(functions.contacts.BlockRequest(chat_id))
            else:
                await borg.send_message(chat , 'This Is Ur **Final** Entry')
                q = await conv.get_response(chat)
                z = q.text
                if '/start' not in z:
                    await borg.send_message(chat, LWARN)
                    await conv.get_response(chat)
                    if not response.text == "/start":
                        await borg.send_message(chat, TWO)
                        await event.client(functions.contacts.BlockRequest(chat_id))
