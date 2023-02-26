from pytube import YouTube
import os

def yt_dowloader(url):
    # This function recievs an url as argument to download
    # a youtube video. (url: ir must be a youtube video url)

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
    


# yt_dowloader("https://youtu.be/W9DAKRu8nBU")