from pytube import YouTube
import os

def yt_dowloader(url: str):
    """
    This function accepts an url as an argument to download
    a youtube video. (url: it must be a youtube video url)
    """

    # Creating a directory to save the downloaded videos
    if os.path.exists("Download videos"):
        pass
    else:
        os.mkdir("Download videos")

    # Downloading the video
    video = YouTube(url)
    download_video = video.streams.get_highest_resolution()
    download_video.download(r"Download videos")

    print("The video was download succesfully.")