import yt_dlp
import os

# تأكد من أن مجلد التحميل موجود
output_dir = "downloads"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def download_youtube_video(url, client, chat_id):
    ydl_opts = {
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'postprocessors': [
            {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'},
            {'key': 'FFmpegMetadata'},
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get("title", "video")
        file_path = info_dict['requested_downloads'][0]['filepath']

    # إرسال الفيديو إلى المستخدم مباشرة
    client.send_video(chat_id, file_path, caption=f"✅ **تم التحميل بنجاح!**\n🎬 {video_title}")

    return file_path