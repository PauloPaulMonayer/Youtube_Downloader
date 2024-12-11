import yt_dlp
import os

def list_formats(video_url):
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get('formats', [])
            print("Available formats:")
            for f in formats:
                audio_video = "Video + Audio" if f.get('acodec', 'none') != 'none' and f.get('vcodec', 'none') != 'none' else \
                              "Audio only" if f.get('acodec', 'none') != 'none' and f.get('vcodec', 'none') == 'none' else \
                              "Video only"
                print(f"{f['format_id']}: {f['ext']} - {f['resolution'] or 'audio only'} ({audio_video})")
    except Exception as e:
        print(f"An error occurred while listing formats: {e}")


def download_youtube_video(video_url, save_path, format_id='best'):
    try:
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': format_id
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Download completed! Video saved to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    
    print("\nFetching available formats...")
    list_formats(video_url)
    
    format_id = input("\nEnter the format ID to download (or press Enter for 'best'): ") or 'best'
    save_path = input("Enter the directory where you want to save the video: ")

    # Ensure the save path exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    download_youtube_video(video_url, save_path, format_id)
