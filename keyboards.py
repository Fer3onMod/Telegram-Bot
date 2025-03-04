from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_selection():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
         InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar")],
        [InlineKeyboardButton("🇫🇷 Français", callback_data="lang_fr"),
         InlineKeyboardButton("🇩🇪 Deutsch", callback_data="lang_de")],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")]
    ])

def main_menu(language):
    labels = {
        "English": ("📺 YouTube Menu", "youtube"),
        "Arabic": ("📺 قائمة يوتيوب", "youtube"),
        "French": ("📺 Menu YouTube", "youtube"),
        "German": ("📺 YouTube-Menü", "youtube"),
        "Russian": ("📺 Меню YouTube", "youtube")
    }
    text, callback = labels.get(language, labels["English"])
    
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text, callback_data=callback)]
    ])

def download_menu(language):
    labels = {
        "English": [
            ("📱 Download Reels", "download_reels"),
            ("📼 Download Video", "download_video"),
            ("⬅️ Back", "back")
        ],
        "Arabic": [
            ("📱 تحميل الريلز", "download_reels"),
            ("📼 تحميل الفيديو", "download_video"),
            ("⬅️ رجوع", "back")
        ],
        "French": [
            ("📱 Télécharger Reels", "download_reels"),
            ("📼 Télécharger la vidéo", "download_video"),
            ("⬅️ Retour", "back")
        ],
        "German": [
            ("📱 Reels herunterladen", "download_reels"),
            ("📼 Video herunterladen", "download_video"),
            ("⬅️ Zurück", "back")
        ],
        "Russian": [
            ("📱 Скачать Reels", "download_reels"),
            ("📼 Скачать видео", "download_video"),
            ("⬅️ Назад", "back")
        ]
    }
    
    buttons = labels.get(language, labels["English"])
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(text, callback_data=callback) for text, callback in buttons[:2]],
        [InlineKeyboardButton(buttons[2][0], callback_data=buttons[2][1])]
    ])