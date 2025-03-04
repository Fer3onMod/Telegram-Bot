from pyrogram import filters, enums
from pyrogram.types import Message, CallbackQuery
from keyboards import language_selection, main_menu, download_menu
from youtube import download_youtube_video
import asyncio

user_data = {}
user_language = {}

# قواميس تحتوي على الترجمات لكل لغة
translations = {
    "English": {
        "selected": "✅ English selected successfully!",
        "menu": "📺 YouTube Menu",
        "choose_download": "📩 Choose what you want to download:",
        "send_link": "📥 Send the video link to download it: 📩",
        "downloading": "⏳ Preparing the download...",
        "download_success": "✅ Video downloaded successfully!",
        "download_error": "❌ An error occurred while downloading the video.",
        "what_next": "🔄 What do you want to do next?"
    },
    "Arabic": {
        "selected": "✅ تم اختيار اللغة العربية بنجاح!",
        "menu": "📺 قائمة يوتيوب",
        "choose_download": "📩 اختر ما تريد تحميله:",
        "send_link": "📥 أرسل رابط الفيديو ليتم تحميله: 📩",
        "downloading": "⏳ جارٍ تجهيز التحميل...",
        "download_success": "✅ تم تحميل الفيديو بنجاح!",
        "download_error": "❌ حدث خطأ أثناء تحميل الفيديو.",
        "what_next": "🔄 ماذا تريد أن تفعل بعد ذلك؟"
    },
    "French": {
        "selected": "✅ Français sélectionné avec succès!",
        "menu": "📺 Menu YouTube",
        "choose_download": "📩 Choisissez ce que vous voulez télécharger :",
        "send_link": "📥 Envoyez le lien de la vidéo pour la télécharger : 📩",
        "downloading": "⏳ Préparation du téléchargement...",
        "download_success": "✅ Vidéo téléchargée avec succès!",
        "download_error": "❌ Une erreur est survenue lors du téléchargement.",
        "what_next": "🔄 Que voulez-vous faire ensuite?"
    },
    "German": {
        "selected": "✅ Deutsch erfolgreich ausgewählt!",
        "menu": "📺 YouTube-Menü",
        "choose_download": "📩 Wählen Sie, was Sie herunterladen möchten:",
        "send_link": "📥 Senden Sie den Videolink, um ihn herunterzuladen: 📩",
        "downloading": "⏳ Download wird vorbereitet...",
        "download_success": "✅ Video erfolgreich heruntergeladen!",
        "download_error": "❌ Beim Herunterladen des Videos ist ein Fehler aufgetreten.",
        "what_next": "🔄 Was möchten Sie als nächstes tun?"
    },
    "Russian": {
        "selected": "✅ Русский успешно выбран!",
        "menu": "📺 Меню YouTube",
        "choose_download": "📩 Выберите, что хотите скачать:",
        "send_link": "📥 Отправьте ссылку на видео для загрузки: 📩",
        "downloading": "⏳ Подготовка к загрузке...",
        "download_success": "✅ Видео успешно загружено!",
        "download_error": "❌ Произошла ошибка при загрузке видео.",
        "what_next": "🔄 Что вы хотите сделать дальше?"
    }
}

def setup_handlers(app):
    @app.on_message(filters.command("start"))
    def start(client, message: Message):
        chat_id = message.chat.id
        user = message.from_user
        username = f"@{user.username}" if user.username else user.first_name

        user_language[chat_id] = None  # عدم تحديد اللغة حتى يختار المستخدم

        welcome_text = """
━━━━━━━━━━━━━━━━━━━━━━━━
👋 **{username}**  
🤖 أهلاً بك في البوت الخاص بتحميل الفيديوهات من يوتيوب بجودة عالية! 🎥✨  
🔹 يمكنك تحميل الفيديوهات بسهولة عن طريق إرسال الرابط.  
🔹 يدعم البوت اللغات العربية، الإنجليزية، الفرنسية، الألمانية، والروسية.

🌍 **اختر لغتك / Choose your language:**  
━━━━━━━━━━━━━━━━━━━━━━━━
""".format(username=username)

        message.reply_text(
            welcome_text,
            reply_markup=language_selection(),
            parse_mode=enums.ParseMode.MARKDOWN
        )

    @app.on_callback_query()
    def callback_query_handler(client, callback_query: CallbackQuery):
        data = callback_query.data
        chat_id = callback_query.message.chat.id

        # اختيار اللغة
        languages = {
            "lang_en": "English",
            "lang_ar": "Arabic",
            "lang_fr": "French",
            "lang_de": "German",
            "lang_ru": "Russian"
        }

        if data in languages:
            user_language[chat_id] = languages[data]
            callback_query.message.edit_text(
                translations[languages[data]]["selected"],
                reply_markup=main_menu(languages[data])
            )

        # إذا ضغط المستخدم على زر يوتيوب
        elif data == "youtube":
            lang = user_language.get(chat_id, "English")  # افتراضي إلى الإنجليزية
            callback_query.message.edit_text(
                translations[lang]["choose_download"],
                reply_markup=download_menu(lang)
            )

        # إذا ضغط المستخدم على تحميل الفيديو أو الريلز
        elif data in ["download_video", "download_reels"]:
            user_data[chat_id] = data  # حفظ نوع التحميل المطلوب
            lang = user_language.get(chat_id, "English")
            callback_query.message.edit_text(
                translations[lang]["send_link"]
            )

        # زر الرجوع لاختيار اللغة
        elif data == "back":
            callback_query.message.edit_text(
                "🌍 اختر لغتك / Choose your language",
                reply_markup=language_selection()
            )

    @app.on_message(filters.text)
    async def handle_video_url(client, message: Message):
        chat_id = message.chat.id
        url = message.text
        lang = user_language.get(chat_id, "English")

        if chat_id in user_data and user_data[chat_id] in ["download_video", "download_reels"]:
            progress_msg = await message.reply_text(translations[lang]["downloading"])
            try:
                file_path = download_youtube_video(url, client, chat_id)
                
                if file_path and isinstance(file_path, str):  # التحقق من صحة الملف
                    async def progress(current, total):
                        percent = (current / total) * 100
                        await progress_msg.edit_text(f"📥 {translations[lang]['downloading']} {percent:.1f}%")
                    
                    await client.send_video(
                        chat_id, 
                        file_path, 
                        caption=translations[lang]["download_success"], 
                        progress=progress
                    )
                    await progress_msg.delete()  # حذف رسالة التحميل بعد الانتهاء
                    
                    # عرض القائمة الرئيسية بعد التحميل
                    await message.reply_text(
                        translations[lang]["what_next"],
                        reply_markup=main_menu(lang)
                    )

                else:
                    await progress_msg.edit_text(translations[lang]["download_error"])

            except Exception as e:
                await progress_msg.edit_text(f"{translations[lang]['download_error']} {str(e)}")

            del user_data[chat_id]  # إزالة البيانات بعد إكمال التحميل