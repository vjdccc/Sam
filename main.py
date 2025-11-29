# main.py
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import RPCError, FloodWaitError
import asyncio

# === الإعدادات ===
APP_ID = 9398423  # يجب أن يكون رقمًا (int)، وليس نصًا
API_HASH = "f059e61617b899e13ebcaceabcb58545"
STRING = "1ApWapzMBu1fL-C89UusDXJVlzvpOpRPaKUoDO3GIJqROVzohlDGb4s31F4mYSDPGHG-0FLbG6buFLtyOeCNwbwJ1yGS17EYQygjMORXCuyy7YLMgMp9oIuwu6yaJEswLcPgjaUjhkeeRVH0KJO_1O1X1mmvZEXuLJh2pk-XSllyKePl8XEuviqGXm3SBPrV27YU5V7tRIfGPKktHoUxQUa0GjBwi0K8HGEk4KMi9uClefmjfv6j73xPQwzmjtsTY5DyWEE7PNAZmtYW_2XrKKJE5ge1-NRp41kP5WCjpX9sJSUib_O1TNb4cAtw2SfSR1G9N1umv09vJClkJGyuhcwhaQ_a-LZQ="

# إنشاء العميل باستخدام Session String
client = TelegramClient(StringSession(STRING), APP_ID, API_HASH)

# --- أمر الإذاعة ---
@client.on(events.NewMessage(outgoing=True, pattern=r".للكروبات(?: |$)(.*)"))
async def gcast(event):
    msg_content = event.pattern_match.group(1)
    if msg_content:
        msg = msg_content
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await event.edit("**⌔∮ يجب الرد على رسالة أو كتابة نص مع الأمر.**")

    status = await event.edit("**⌔∮ بدء الإذاعة إلى المجموعات...**")

    # جمع جميع المجموعات (بدون قائمة سوداء)
    groups = []
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            groups.append(dialog.id)

    total = len(groups)
    if total == 0:
        return await status.edit("**⌔∮ لا توجد مجموعات متاحة!**")

    done = failed = 0
    for i, chat_id in enumerate(groups, start=1):
        try:
            await client.send_message(chat_id, msg)
            done += 1
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
            try:
                await client.send_message(chat_id, msg)
                done += 1
            except Exception:
                failed += 1
        except RPCError:
            failed += 1
        except Exception:
            failed += 1

        # تحديث العداد كل 5 مجموعات أو عند الانتهاء
        if i % 5 == 0 or i == total:
            try:
                await status.edit(
                    f"**⌔∮ جاري الإذاعة...**\n"
                    f"**✅ نجاح:** `{done}`\n"
                    f"**❌ فشل:** `{failed}`\n"
                    f"**📊 التقدم:** `{i}/{total}`"
                )
            except Exception:
                pass  # تجاهل إذا فشل التعديل (مثل حذف الرسالة)

        await asyncio.sleep(0.3)  # تأخير لتجنب التقييد

    await status.edit(
        f"**⌔∮ اكتملت الإذاعة!**\n"
        f"**✅ نجاح:** `{done}` مجموعة\n"
        f"**❌ فشل:** `{failed}` مجموعة\n"
        f"**📊 المجموع:** `{total}`"
    )

# --- تشغيل العميل ---
print("🚀 جاري تشغيل السورس...")
client.start()
print("✅ ALPHΑ = تم تشغيل السورس")
client.run_until_disconnected()
