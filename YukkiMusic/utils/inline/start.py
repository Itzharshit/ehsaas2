#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        

                [InlineKeyboardButton("β°πΎπ€π’π’ππ£ππ¨β±", url=f"https://telegra.ph/Ehsaas-Music-commands-03-17")],

                







                [

                    InlineKeyboardButton(

                        "β°ππΏπΌππ½β±", url=f"https://t.me/World_friends_chatting_group"

                    ),

                    InlineKeyboardButton(

                        "β°π’ππ»π²πΏβ±", url=f"https://t.me/ARMY0071"

                    ),

                ],
    ]
    
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
       [

                    InlineKeyboardButton(

                        "β°β πΌπΏπΏ ππ ππ ππππ πππππ ββ±",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("β°πΎπ€π’π’ππ£ππ¨β±", url=f"https://telegra.ph/Ehsaas-Music-commands-03-17")],

                







                [

                    InlineKeyboardButton(

                        "β°ππΏπΌππ½β±", url=f"https://t.me/World_friends_chatting_group"

                    ),

                    InlineKeyboardButton(

                        "β°π’ππ»π²πΏβ±", url=f"https://t.me/ARMY0071"

                    ),

                ],
        [InlineKeyboardButton("β°π³οΈβπ πππ£ππͺπππβ±", callback_data="LG")],
    ]
  
    return buttons
