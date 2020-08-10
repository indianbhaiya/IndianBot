<p align="center">
<img src="https://github.com/indianbhaiya/IndianBot/blob/master/.github/newlogo.png" alt="indian Bot">
# IndianBot The UserBot 🇮🇳
# Will Re-Start Again In 1 Week!!

Best User Bot To Manage Your Telegram Account 😉
## Most PowerFul And Better And Secure !

## By Team IndianBot 🇮🇳

For any query or want to know how it works join 👇👇
### <a href="https://t.me/indianbot_official"><img src="https://raw.githubusercontent.com/indianbhaiya/IndianBot/master/.github/button%20(7).png"></a>



## FORK AT YOUR OWN RISK !
## Don't Forget To Give A Star ⭐

# For Regular Users
### <a href="https://heroku.com/deploy?template=https://github.com/indianbhaiya/IndianBot"><img src="https://raw.githubusercontent.com/indianbhaiya/IndianBot/master/.github/button%20(8).png"></a>


## GET STRING SESSION FROM REPL RUN 
### <a href="https://indianbotstringsetup.pureindialover.repl.run"><img src="https://raw.githubusercontent.com/indianbhaiya/IndianBot/master/.github/button%20(9).png"></a>


<p align="center">
<img src="https://github.com/indianbhaiya/IndianBot/blob/master/.github/devsec.png">

Simply clone the repository and run the main file:
```bash
git clone https://github.com/indianbhaiya/IndianBot
cd Indianbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6 
  # 6 is the length of api id
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e" 
  # Use Your Own Api Hash
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
