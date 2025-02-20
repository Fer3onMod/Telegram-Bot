from pyrogram import filters
from pyrogram.types import ReplyKeyboardMarkup
from languages import get_language
from youtube import download_youtube_video

user_languages = {}
def create_menus(lang):
    return {
        "main_menu": ReplyKeyboardMarkup([
            [get_language(lang, "download_youtube")]
        ], resize_keyboard=True),
        "youtube_menu": ReplyKeyboardMarkup([
            [get_language(lang, "download_video"), get_language(lang, "download_shorts")],
            [get_language(lang, "back")]
        ], resize_keyboard=True)
    }

def setup_handlers(bot):
    @bot.on_message(filters.command("start"))
    def start(client, message):
        client.send_message(
            message.chat.id,
            "🌍 Please choose your language / الرجاء اختيار لغتك:",
            reply_markup=ReplyKeyboardMarkup([
                ["🇺🇸 English", "🇸🇦 العربية"]
            ], resize_keyboard=True)
        )

    @bot.on_message(filters.text & filters.regex("🇺🇸 English|🇸🇦 العربية"))
    def set_language(client, message):
        lang = "English" if "English" in message.text else "العربية"
        user_languages[message.chat.id] = lang
        menus = create_menus(lang)
        client.send_message(message.chat.id, get_language(lang, "language_set"), reply_markup=menus["main_menu"])

    @bot.on_message(filters.text & filters.regex("▶️ YouTube|▶️ يوتيوب"))
    def youtube_option(client, message):
        lang = user_languages.get(message.chat.id, "English")
        menus = create_menus(lang)
        client.send_message(message.chat.id, get_language(lang, "choose_download"), reply_markup=menus["youtube_menu"])

    @bot.on_message(filters.text & filters.regex("⬅️ Back|⬅️ رجوع"))
    def back_to_main(client, message):
        lang = user_languages.get(message.chat.id, "English")
        menus = create_menus(lang)
        client.send_message(message.chat.id, get_language(lang, "main_menu"), reply_markup=menus["main_menu"])

    @bot.on_message(filters.text & filters.regex("📹 Download Video|📹 تحميل الفيديو"))
    def request_youtube_video(client, message):
        lang = user_languages.get(message.chat.id, "English")
        client.send_message(message.chat.id, get_language(lang, "send_youtube_link"))

    @bot.on_message(filters.text & filters.regex("📱 Download Shorts|📱 تحميل الريلز"))
    def request_youtube_shorts(client, message):
        lang = user_languages.get(message.chat.id, "English")
        client.send_message(message.chat.id, get_language(lang, "send_youtube_shorts_link"))

    @bot.on_message(filters.text & filters.regex(r'https?://(www\.)?(youtube\.com|youtu\.be)/\S+'))
    def handle_youtube(client, message):
        lang = user_languages.get(message.chat.id, "English")
        client.send_message(message.chat.id, get_language(lang, "downloading"))
        url = message.text.strip()
        download_youtube_video(url, client, message.chat.id)
