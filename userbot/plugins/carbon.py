# sed lyf
import os
import re
import shutil
from datetime import datetime
from html import unescape
from re import findall
from time import sleep
from urllib.error import HTTPError
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from emoji import get_emoji_regexp
from google_images_download import google_images_download
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googletrans import LANGUAGES
from googletrans import Translator
from gtts import gTTS
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from urbandict import define
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError
from wikipedia.exceptions import PageError
from userbot import BOTLOG
from userbot import BOTLOG_CHATID
from userbot import CHROME_DRIVER
from userbot import CMD_HELP
from userbot import GOOGLE_CHROME_BIN
from userbot import YOUTUBE_API_KEY
from userbot.utils import register
CARBONLANG = "auto"
LANG = "en"
@register(outgoing=True, pattern="^.carbon")
async def carbon_api(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        """ A Wrapper for carbon.now.sh """
        await e.edit("`Processing..`")
        CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
        global CARBONLANG
        textx = await e.get_reply_message()
        pcode = e.text
        if pcode[8:]:
            pcode = str(pcode[8:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        await e.edit("`Meking Carbon...\n25%`")
        url = CARBON.format(code=code, lang=CARBONLANG)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = GOOGLE_CHROME_BIN
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        prefs = {"download.default_directory": "./"}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                                  options=chrome_options)
        driver.get(url)
        await e.edit("`Be Patient...\n50%`")
        download_path = "./"
        driver.command_executor._commands["send_command"] = (
            "POST",
            "/session/$sessionId/chromium/send_command",
        )
        params = {
            "cmd": "Page.setDownloadBehavior",
            "params": {
                "behavior": "allow",
                "downloadPath": download_path
            },
        }
        command_result = driver.execute("send_command", params)
        driver.find_element_by_xpath(
            "//button[contains(text(),'Export')]").click()
        await e.edit("`Processing..\n75%`")
        # Waiting for downloading
        sleep(2.5)
        await e.edit("`Done Dana Done...\n100%`")
        file = "./carbon.png"
        await e.edit("`Uploading..`")
        await e.client.send_file(
            e.chat_id,
            file,
            caption=
            "<< Here's your carbon, \n Carbonised by [IndianBot](https://www.github.com/indianbhaiya/IndianBot)>> ",
            force_document=True,
            reply_to=e.message.reply_to_msg_id,
        )
        os.remove("./carbon.png")
        driver.quit()
        # Removing carbon.png after uploading
        await e.delete()  # Deleting msg
