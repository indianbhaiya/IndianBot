import os

from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os

    class Config(object):
        LOGGER = True
        LOCATION = os.environ.get("LOCATION", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
            "SCREEN_SHOT_LAYER_ACCESS_KEY", None
        )
        TMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/"
        )
        IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
        IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
        HASH_TO_TORRENT_API = os.environ.get(
            "HASH_TO_TORRENT_API", "https://example.com/torrent/{}"
        )
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "IndianBot")
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001198699233))
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
        TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
        MAX_MESSAGE_SIZE_LIMIT = 4095
        UB_BLACK_LIST_CHAT = set(
            int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
        )
        MAX_ANTI_FLOOD_MESSAGES = 10
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None, view_messages=None, send_messages=True
        )
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", False))
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
        NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
        PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
        if PM_LOGGR_BOT_API_ID:
            PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
        DB_URI = os.environ.get("DATABASE_URL", None)
        NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 5)
        )
        COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
        SUDO_USERS = set(
            int(x) for x in os.environ.get("SUDO_USERS", "1097131648").split()
        )
        WHITELIST_USERS = set(
            int(x) for x in os.environ.get("WHITELIST_USERS", "832241419").split()
        )
        BLACKLIST_USERS = set(
            int(x) for x in os.environ.get("BLACKLIST_USERS", "").split()
        )
        DEVLOPERS = set(
            int(x) for x in os.environ.get("DEVLOPERS", "813878981").split()
        )
        OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "953414679").split())
        SUPPORT_USERS = set(
            int(x) for x in os.environ.get("SUPPORT_USERS", "719195224").split()
        )
        VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
        VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
        GROUP_REG_SED_EX_BOT_S = os.environ.get(
            "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
        )
        TEMP_DIR = os.environ.get("TEMP_DIR", None)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        CHROME_DRIVER = os.environ.get(
            "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
        )
        GOOGLE_CHROME_BIN = os.environ.get(
            "GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome"
        )
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
        if AUTH_TOKEN_DATA != None:
            os.makedirs(TMP_DOWNLOAD_DIRECTORY)
            t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
            t_file.write(AUTH_TOKEN_DATA)
            t_file.close()
        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        MONGO_URI = os.environ.get("MONGO_URI", None)
        LYDIA_API = os.environ.get("LYDIA_API", None)
        PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", False))


else:

    class Config(object):
        DB_URI = None
