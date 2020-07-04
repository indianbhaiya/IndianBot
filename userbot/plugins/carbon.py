# Copyright (C) 2019 The Raphielscape Company LLC.

#

# Licensed under the Raphielscape Public License, Version 1.b (the "License");

# you may not use this file except in compliance with the License.

#

""" Userbot module containing various scrapers. """

import os

import shutil

from bs4 import BeautifulSoup

import re

from time import sleep

from html import unescape

from re import findall

from datetime import datetime

from selenium import webdriver

from urllib.parse import quote_plus

from urllib.error import HTTPError

from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options

from wikipedia import summary

from wikipedia.exceptions import DisambiguationError, PageError

from urbandict import define

from requests import get

from google_images_download import google_images_download

from googleapiclient.discovery import build

from googleapiclient.errors import HttpError

from googletrans import LANGUAGES, Translator

from gtts import gTTS

from emoji import get_emoji_regexp

from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, CHROME_DRIVER, GOOGLE_CHROME_BIN

from userbot.utils import register

CARBONLANG = "auto"

LANG = "en"

@register(outgoing=True, pattern="^.carbon")

async def carbon_api(e):

 if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

   """ A Wrapper for carbon.now.sh """

   await e.edit("`Processing..`")

   CARBON = 'https://carbon.now.sh/?l={lang}&code={code}'

   global CARBONLANG

   textx = await e.get_reply_message()

   pcode = e.text

   if pcode[8:]:

         pcode = str(pcode[8:])

   elif textx:

         pcode = str(textx.message) # Importing message to module

   code = quote_plus(pcode) # Converting to urlencoded

   await e.edit("`Meking Carbon...\n25%`")

   url = CARBON.format(code=code, lang=CARBONLANG)

   chrome_options = Options()

   chrome_options.add_argument("--headless")

   chrome_options.binary_location = GOOGLE_CHROME_BIN

   chrome_options.add_argument("--window-size=1920x1080")

   chrome_options.add_argument("--disable-dev-shm-usage")

   chrome_options.add_argument("--no-sandbox")

   chrome_options.add_argument("--disable-gpu")

   prefs = {'download.default_directory' : './'}

   chrome_options.add_experimental_option('prefs', prefs)

   driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)

   driver.get(url)

   await e.edit("`Be Patient...\n50%`")

   download_path = './'

   driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}

   command_result = driver.execute("send_command", params)

   driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()

   #driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()

   #driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()

   await e.edit("`Processing..\n75%`")

   # Waiting for downloading

   sleep(2.5)

   await e.edit("`Done Dana Done...\n100%`")

   file = './carbon.png'

   await e.edit("`Uploading..`")

   await e.client.send_file(

         e.chat_id,

         file,

         caption="<< Here's your carbon, \n Carbonised by [IndianBot](https://www.github.com/indianbhaiya/IndianBot)>> ",

         force_document=True,

         reply_to=e.message.reply_to_msg_id,

         )

   os.remove('./IndianBot.png')

   driver.quit()

   # Removing carbon.png after uploading

   await e.delete() # Deleting msg
   
"""Carbon Scraper Plugin for Userbot. //text in creative way.
usage: .karb //as a reply to any text message

Thanks to @pureindialover for THIS PLUGIN"""

from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from telethon import events
from urllib.parse import quote_plus
from urllib.error import HTTPError
from time import sleep
import asyncio
import os
import random
from userbot.utils import admin_cmd
#@borg.on(events.NewMessage(pattern=r"\.karb ", outgoing=True))
@borg.on(admin_cmd(pattern="karb"))
async def carbon_api(e):
 RED = random.randint(0,256)
 GREEN = random.randint(0,256)
 BLUE = random.randint(0,256)
 THEME= [         "3024-night",
                  "a11y-dark",
                  "blackboard",
                  "base16-dark",
                  "base16-light",
                  "cobalt",
                  "dracula",
                  "duotone-dark",
                  "hopscotch",
                  "lucario",
                  "material",
                  "monokai",
                  "night-owl",
                  "nord",
                  "oceanic-next",
                  "one-light",
                  "one-dark",
                  "panda-syntax",
                  "paraiso-dark",
                  "seti",
                  "shades-of-purple",
                  "solarized",
                  "solarized%20light",
                  "synthwave-84",
                  "twilight",
                  "verminal",
                  "vscode",
                  "yeti",
                  "zenburn",
]

 CUNTHE = random.randint(0, len(THEME) - 1)
 The = THEME[CUNTHE]


 if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
   """ A Wrapper for carbon.now.sh """
   await e.edit("⬜⬜⬜⬜⬜")
   CARBON = 'https://carbon.now.sh/?bg=rgba({R}%2C{G}%2C.{B}%2C1)&t={T}&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}'
   CARBONLANG = "en"
   textx = await e.get_reply_message()
   pcode = e.text
   if pcode[6:]:
         pcode = str(pcode[6:])
   elif textx:
         pcode = str(textx.message) # Importing message to module
   code = quote_plus(pcode) # Converting to urlencoded
   url = CARBON.format(code=code, R=RED, G=GREEN, B=BLUE, T=The, lang=CARBONLANG)
   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
   chrome_options.add_argument("--window-size=1920x1080")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument('--disable-gpu')
   prefs = {'download.default_directory' : './'}
   chrome_options.add_experimental_option('prefs', prefs)
   await e.edit("⬛⬛⬜⬜⬜")

   driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER, options=chrome_options)
   driver.get(url)
   download_path = './'
   driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
   command_result = driver.execute("send_command", params)

   driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
   sleep(5) # this might take a bit.
   #driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   #sleep(5)
   await e.edit("⬛⬛⬛⬜⬜")
   #driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
   #sleep(5) #Waiting for downloading

   await e.edit("⬛⬛⬛⬛⬛")
   file = './carbon.png'
   await e.edit("✅RGB Karbon Completed, Uploading RGB Karbon✅")
   await e.client.send_file(
         e.chat_id,
         file,
         caption="Carbonised by [IndianBot](https://t.me/IndianArMyGiveaway)",
         force_document=False,
         reply_to=e.message.reply_to_msg_id,
         )

   os.remove('./carbon.png')
   # Removing carbon.png after uploading
   await e.delete() # Deleting msg
