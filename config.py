import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # استدعاء توكن البوت
API_ID = int(os.getenv("API_ID"))   # تحويل API_ID إلى رقم صحيح
API_HASH = os.getenv("API_HASH")    # استدعاء API_HASH

if not all([BOT_TOKEN, API_ID, API_HASH]):
    raise ValueError("⚠️ تأكد من ضبط جميع المتغيرات في GitHub Secrets!")
