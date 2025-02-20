from pyrogram import Client
from handlers import setup_handlers
from flask import Flask
import threading

# إعداد البوت
bot = Client(
    "Fer3on_Mod",
    api_id=28221983,  # استبدل بـ API ID الجديد
    api_hash="d4dde55766a34280ef19e22d5824308f",  # استبدل بـ API Hash الجديد
    bot_token="8040245197:AAHSUsYS_UYypD5dGiEqz-wW5rz_rwjB-yg"  # استبدل بـ Bot Token الجديد
)

# ضبط الهاندلرز
setup_handlers(bot)

# إعداد خادم ويب بسيط
app = Flask(__name__)

@app.route('/')
def home():
    return "The bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# تشغيل الخادم في خيط منفصل
threading.Thread(target=run_flask).start()

# تشغيل البوت
bot.run()