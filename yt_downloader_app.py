import os
import sys
import tkinter.font
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Combobox
from pytube import YouTube


# Colors
color_1 = "#083358"
color_2 = "#ff5722"
color_3 = "#0f4471"
color_4 = "#f6f6f6"


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# GUI
app = Tk()
app.title("Youtube Downloader App")
app.geometry("800x500")
app.resizable(height=False, 
              width=False)
app.config(bg=color_3)
path = resource_path("images\\youtube-logo.ico")
app.iconbitmap(path)


# Setting the font
bold_font = tkinter.font.Font(family="Ubuntu", 
                              size=20, 
                              weight="bold")
normal_font = tkinter.font.Font(family="Ubuntu", 
                                size=16)


# App title and logo
frame_0 = Frame(app, 
                width="700", 
                height="300", 
                bg=color_3)
frame_0.pack(pady=30)

label_0 = Label(frame_0, 
                text="YouTube Downloader App", 
                bg=color_3, 
                fg=color_4, 
                font=bold_font)
label_0.grid(row=0, 
             column=0, 
             padx=30)

path = resource_path("images\\youtube-logo.png")
img = PhotoImage(file=path)

label_1 = Label(frame_0, 
                image=img,
                bg=color_3)
label_1.grid(row=0, 
             column=1)


# Frame 1
frame_1 = Frame(app, 
                width="700", 
                height="200", 
                bg=color_3)
frame_1.pack(pady=20)

# Choosing format to download
label_2 = Label(frame_1, 
                text="Format:", 
                bg=color_3, 
                fg=color_4,
                font=normal_font) 
label_2.grid(row=0, 
             column=0, 
             padx=30,
             pady=20)

combo = Combobox(frame_1, 
                 width="48",
                 justify="center",
                 font=normal_font)
combo["values"] = ("mp3", 
                   "mp4")
combo.current(0)
combo.grid(row=0, 
           column=1, 
           padx=30)


# Getting url
label_3 = Label(frame_1, 
                text="URL:", 
                bg=color_3, 
                fg=color_4,
                font=normal_font) 
label_3.grid(row=1, 
             column=0, 
             padx=30)

entry_0 = Entry(frame_1,
                width="50", 
                bg=color_4, 
                fg=color_1, 
                font=normal_font)
entry_0.grid(row=1, 
             column=1)


# Downloading the video
def yt_downloader():
    """This function accepts an url as an argument to download a 
    youtube video or audio. (url: it must be a youtube video url)"""

    # Getting the format
    output_format = combo.get()
    
    
    # Downloading on dependance of format
    if output_format == "mp3":
        
        # Creating a directory to save the downloaded audios
        if os.path.exists("Download audios"):
            pass
        else:
            os.mkdir("Download audios")

        # Downloading the audio
        audio = YouTube(entry_0.get())
        download_audio = audio.streams.filter(only_audio=True).first()
        out_file = download_audio.download(r"Download audios")
        
        # Saving the file with mp3 format
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        tkinter.messagebox.showinfo("Succes!", 
                                    "The audio was downloaded succesfully.")
        
        
    elif output_format == "mp4":   
           
        # Creating a directory to save the downloaded videos
        if os.path.exists("Download videos"):
            pass
        else:
            os.mkdir("Download videos")

        # Downloading the video
        video = YouTube(entry_0.get())
        download_video = video.streams.get_highest_resolution()
        download_video.download(r"Download videos")

        tkinter.messagebox.showinfo("Succes!", 
                                    "The video was downloaded succesfully.")


# Button to start downloading the video
button = Button(app, 
                text="Download", 
                bg=color_2, 
                fg=color_1, 
                font=bold_font, 
                command=yt_downloader)
button.pack()


app.mainloop()