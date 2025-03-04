import yt_dlp
import os

class YouTubeDownloader:
    def __init__(self):
        self.output_dir = "downloads"
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def download_video(self, url, client, chat_id):
        ydl_opts = {
            'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'merge_output_format': 'mp4',
            'outtmpl': f'{self.output_dir}/%(title)s.%(ext)s',
            'postprocessors': [
                {'key': 'FFmpegMetadata'},
            ],
            'force_generic_extractor': True  # ✅ تم إضافة force-generic-extractor
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
