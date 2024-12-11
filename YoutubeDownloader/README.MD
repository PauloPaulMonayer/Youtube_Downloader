# YouTube Downloader

This is a Python-based application for downloading YouTube videos. The application uses the `yt-dlp` library to fetch available video formats and download the video of your choice.

## Features

- List available video and audio formats for a YouTube video.
- Download videos or audio in the format of your choice.
- Save downloaded files to a directory specified by the user.

---

## Prerequisites

1. **Python 3.9 or above**:
   - Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **yt-dlp**:
   - Install the `yt-dlp` library by running:
     ```bash
     pip install yt-dlp
     ```

---

## How to Run the Application

1. Clone or download the script to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:
   ```bash
   python youtube_downloader.py
   ```

---

## Usage Instructions

1. **Enter the YouTube video URL:**

   - When prompted, paste the URL of the YouTube video you want to download.

2. **View Available Formats:**

   - The application will display all available formats for the video (e.g., resolution, audio-only options).

3. **Select a Format ID:**

   - Enter the `format ID` corresponding to the desired format (e.g., 18 for 360p, 22 for 720p).
   - Press `Enter` to select the default format (`best`).

4. **Specify a Save Path:**

   - Provide the directory path where you want to save the downloaded file.

5. **Download Progress:**
   - The application will download the video and notify you upon completion.

---

## Example Run

```plaintext
Enter the YouTube video URL: https://www.youtube.com/watch?v=EXAMPLE

Fetching available formats...
Available formats:
18: mp4 - 360p
22: mp4 - 720p
140: m4a - audio only

Enter the format ID to download (or press Enter for 'best'): 22
Enter the directory where you want to save the video: C:\Downloads

Download completed! Video saved to C:\Downloads
```

---

## Troubleshooting

- **`yt-dlp` not found:** Ensure you have installed `yt-dlp` using the command `pip install yt-dlp`.
- **Format not available:** Verify the selected format ID is listed in the available formats.
- **Permission issues:** Run the script with appropriate permissions or change the save path to a writable directory.
- **Python version deprecated:** Ensure you are running Python 3.9 or higher.

---

## License

This project is open-source and available under the MIT License.
