import yt_dlp
import os

class YouTubeDownloader:
    def __init__(self):
        self.output_dir = "downloads"
        self.cookies_file = os.path.join(os.path.dirname(__file__), "cookies.txt")  # ✅ تحديد المسار الصحيح للكوكيز
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def download_video(self, url, client, chat_id):
        if not os.path.exists(self.cookies_file):  # ✅ التأكد من وجود ملف الكوكيز
            raise FileNotFoundError(f"❌ ملف الكوكيز غير موجود: {self.cookies_file}")

        ydl_opts = {
            'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'merge_output_format': 'mp4',
            'outtmpl': f'{self.output_dir}/%(title)s.%(ext)s',
            'postprocessors': [
                {'key': 'FFmpegMetadata'},
            ],
            'cookies': self.cookies_file,  # ✅ تمرير ملف الكوكيز
            'verbose': True  # ✅ تمكين وضع Debug لمعرفة الأخطاء
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)

        if os.path.exists(file_path):  # التأكد من وجود الملف
            return file_path
        else:
            return None  # إرجاع None إذا لم يتم تحميل الفيديو

def download_youtube_video(url, client, chat_id):
    downloader = YouTubeDownloader()
    return downloader.download_video(url, client, chat_id)
