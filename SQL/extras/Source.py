import re
import time
from datetime import datetime
from IqArab import StartTime, iqthon
from IqArab.Config import Config
from IqArab.plugins import mention
help1 = ("**⁂ ⦙ كيفيه التنصيب :**")
help2 = ("**⁂ ⦙ قـائمـه الاوامـر :**\n**⁂ ⦙ قنـاه السـورس :** @IQTHON\n**⁂ ⦙ شـرح اوامـر السـورس : @L3LL3**\n**⁂ ⦙ شـرح فـارات السـورس : @TEAMTELETHON** \n - اوامر الاونلاين تشتغل فقط في المجموعات ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**‎⿻┊My ⁂ {mention} ٫ **\n‌‎**⿻┊BoT ⁂ {TG_BOT} ٫**\n**‌‎⿻┊TimE ⁂ {TM} ٫**\n**‌‎⿻┊‌‎VeRsIoN ⁂ (8.3) ,** \n**⿻┊‌‎TeLeThoN AraB ⁂** @IQTHON"
