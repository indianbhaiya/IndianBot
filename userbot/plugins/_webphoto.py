# Imports
from os import system as cmd
from random import choice as c

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from userbot.utils import admin_cmd

# Important-vars
CHROME_DRIVER = "/app/.chromedriver/bin/chromedriver"
GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
download_path = "./"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
prefs = {"download.default_directory": "./"}
r = [
    "http://subbyhubby.com",
    "http://milehighmedia.com",
    "https://www.xempire.com/en",
    "https://www.sunnyleone.com/en/",
    "https://m.sweetheartvideo.com/",
    "http://famedigital.com",
    "http://assholefever.com",
]
# Logos
def success_lago():
    logo = (
        "███████▒███ █▒       █ ███▒████ ████████ ████▒▒███ ██████████ ██████████\n"
        "█▒          █▒       █ █        ▒        █         ▒▒         █▒\n"
        "█▒          █▒       █ ▒        █        █         ██         ▒█\n"
        "███████████ █▒       █ █        █        ███▒███   ███▒██████ ██████████\n"
        "         ▒█ █▒       █ █        ▒        █                 ██         ▒█\n"
        "         ▒█ █▒       █ ▒        █        █                 ██         █▒\n"
        "████▒██████ ██████████ ████████ ████████ ▒████████ ██▒███████ ███▒███▒██\n"
        "████████████████████████████████████████████████████████████████████████\n"
    )
    print(f"{logo}")


def done_lago():
    logo = (
        "█████████    █████████ ██      █ █▒███████\n"
        "█        █   █       █ ▒ █     ▒ █\n"
        "█         █  █       █ █  ▒    █ █\n"
        "█   ▒▒     █ █  ▒▒▒  █ █   █   █ ███▒▒██\n"
        "█         █  █       █ █    ▒  █ █\n"
        "█        █   █       █ ▒     █ █ █\n"
        "█████████    █████████ █      ▒▒ ███▒████▒\n"
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
    )
    print(f"{logo}")


# Main Commands
@borg.on(admin_cmd("web ?(.*)"))
async def WebData_By_Akash(webdata_credit_akash):
    link = webdata_credit_akash.pattern_match.group(1)
    await webdata_credit_akash.edit("**Deleting All** `.txt` **Files**")
    cmd("rm ./*.txt")  # Removing all Text Files
    await webdata_credit_akash.edit("**Deleting All** `.png` **Files**")
    cmd("rm ./*.png")  # Removing All Png Files
    await webdata_credit_akash.edit("**Deleting All** `.jpg` **Files**")
    cmd("rm ./*.jpg")  # Removing All jpg Files
    await webdata_credit_akash.edit("**Deleting All Files : Successful**")
    bot = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
    if link == "":
        bot.get(c(r))
        bot.get_screenshot_as_file(filename="NoWebsiteGiven.png")
        await webdata_credit_akash.client.send_file(
            webdata_credit_akash.chat_id,
            "NoWebsiteGiven.png",
            caption="<< **U Mentioned No Link** >>",
            force_document=True,
        )
        cmd("rm ./*.png")
        done_lago()
    elif link is not "":
        bot.get(link)
        bot.get_screenshot_as_file(filename="WebSite Data.png")
        await webdata_credit_akash.client.send_file(
            webdata_credit_akash.chat_id,
            "WebSite Data.png",
            caption="<< **The WebData Of Link U Gave** >>",
            force_document=True,
        )
        cmd("rm ./*.png")
        done_lago()
    await webdata_credit_akash.delete()


success_lago()
