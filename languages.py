translations = {
    "English": {
        "language_set": "✅ Language set successfully!",
        "download_youtube": "▶️ YouTube",
        "choose_download": "📥 Choose what you want to download:",
        "download_video": "📹 Download Video",
        "download_shorts": "📱 Download Shorts",
        "send_youtube_link": "📥 Send the YouTube video link:",
        "send_youtube_shorts_link": "📱 Send the YouTube Shorts link:",
        "downloading": "⏳ Downloading...",
        "download_success": "✅ Download successful!",
        "back": "⬅️ Back",
        "main_menu": "🏠 Main Menu:"
    },
    "العربية": {
        "language_set": "✅ تم اختيار اللغة بنجاح!",
        "download_youtube": "▶️ يوتيوب",
        "choose_download": "📥 اختر ما تريد تحميله:",
        "download_video": "📹 تحميل الفيديو",
        "download_shorts": "📱 تحميل الريلز",
        "send_youtube_link": "📥 أرسل رابط الفيديو من يوتيوب:",
        "send_youtube_shorts_link": "📱 أرسل رابط الريلز من يوتيوب:",
        "downloading": "⏳ جاري التحميل...",
        "download_success": "✅ تم التحميل بنجاح!",
        "back": "⬅️ رجوع",
        "main_menu": "🏠 القائمة الرئيسية:"
    }
}

def get_language(lang, key):
    return translations.get(lang, translations["English"]).get(key, "Unknown")

