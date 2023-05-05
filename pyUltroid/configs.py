# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", "13764765", cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", "0255274ce6771d5535c201dd05ce8d79")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", "1BVtsOKcBu6vOM1tt4H059yWn-ILuAjUknCP9THYLkzgTg0GrDyDXzCGwa6gN6yCr8wStYimenOUmYLISlnb_NX2LkPzVtIQGxMxmjPxbjL9wmgbVBnHkXy1XKzWS5oxSuZvBy6S7_c7-NLKaWzC2AOquWF2zLbGAVz-37RfsjxsXyx5t2zHxBhAY9ncf3trjOILKt8u5dykPQtkq08vEaOApVYSx2n-PA3ILYlKVFTqPNB58YEr9YMPrcXM-2zeJgZNa4t_0N1U2MgtSmWZIXkxbex-eDZ8xmNad44WTUTqfo-di2kq8XktYzvr3Zfa7Rx0GJ0cFA-FYf0PQawHazhfH_fER8GU=")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=None)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
