import asyncio
from asyncio.exceptions import CancelledError
from datetime import timedelta
from pathlib import Path
from telethon import Button, functions, types, utils
from IqArab import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from ..Config import Config
from ..core.logger import logging
from ..core.session import iqthon
from ..helpers.utils import install_pip
from ..sql_helper.global_collection import del_keyword_collectionlist, get_item_collectionlist
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .klanr import load_module
from .tools import create_supergroup
LOGS = logging.getLogger("تليثون العرب \n ")
cmdhr = Config.COMMAND_HAND_LER
TG_BOT = Config.TG_BOT_USERNAME
async def load_plugins(folder):
    path = f"IqArab/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(shortname.replace(".py", ""),  plugin_path=f"IqArab/{folder}")
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"IqArab/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"IqArab/{folder}/{shortname}.py"))
                LOGS.info(f"🝳 ︙غير قادر على التحميل {shortname} يوجد هناك خطا بسبب : {e}"                )
async def startupmessage():
    try:
        if BOTLOG:
            Config.CATUBLOGO = await iqthon.tgbot.send_file(BOTLOG_CHATID, "https://telegra.ph/file/388e81c2cdc1664ccb652.jpg",
                                                            caption= """**⁂ - تـمّ  اعـادة تشـغيل .
⁂ - تليثـون العـرب ( 8.3 ) .

⁂ - اوامر السورس : ( .الاوامر  ) 

⁂ - لمـعرفة كيفية تغير بعض كلايش
او صور السـورس  أرسـل  : (  .مساعده  )

⁂ - القناة تليثون العرب : @IQTHON

❕- يتم اعادة التشغيل كل 24 ساعة ⁂**""" ,                buttons=[(Button.url("مطور تليثون الرسمي", "https://t.me/GGGKG"),)],            )
    except Exception as e:
        LOGS.error(e)
        return None

async def setinlinemybot():
    try:
        inlinestarbot = await iqthon.tgbot.get_me()
        bot_name = inlinestarbot.first_name
        botname = f"@{inlinestarbot.username}"
        Arab = "IQTHON ARAB"
        if bot_name.endswith("Assistant"):
            print("تم تشغيل البوت")
        if inlinestarbot.bot_inline_placeholder:
            print("Arab 🟢")
        else:
            try:
                await iqthon.send_message("@BotFather", "/setinline")
                await asyncio.sleep(1)
                await iqthon.send_message("@BotFather", botname)
                await asyncio.sleep(1)
                await iqthon.send_message("@BotFather", Arab)
                await asyncio.sleep(2)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

async def add_bot_to_logger_group(chat_id):
    bot_details = await iqthon.tgbot.get_me()
    try:
        await iqthon(            functions.messages.AddChatUserRequest(                chat_id=chat_id,                user_id=bot_details.username,                fwd_limit=1000000            )        )
    except BaseException:
        try:
            await iqthon(
