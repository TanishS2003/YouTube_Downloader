import tkinter as tk
from pytube import YouTube
import customtkinter


def startDownload(option):
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "highQuality":
            video = ytObject.streams.get_highest_resolution()
        elif option == "lowQuality":
            video = ytObject.streams.get_lowest_resolution()
        elif option == "audio":
            video = ytObject.streams.get_audio_only()
        else:
            return

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!", text_color="green")

    except Exception as e:
        finishLabel.configure(text="Download Error!", text_color="red")


def on_progress(stream,  bytes_reamaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_reamaining
    percentage_of_completion = bytes_download / total_size * 100
    per = str(int(percentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()

    progressbar.set(float(percentage_of_completion) / 100)


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app_icon = "E:\\Projects\\Youtube Downloader\\logo.ico"

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

app.iconbitmap(app_icon)

title = customtkinter.CTkLabel(
    app, text="Insert a YouTube Link", width=200, height=50, font=("cursive", 28))
title.pack(padx=10, pady=10)

url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=50, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

download_hq = customtkinter.CTkButton(
    app, text="Download High Quality-Mp4", command=lambda: startDownload("highQuality"))
download_hq.pack(padx=10, pady=10)

download_lq = customtkinter.CTkButton(
    app, text="Download Low Quality-Mp4", command=lambda: startDownload("lowQuality"))
download_lq.pack(padx=10, pady=10)

download_audio = customtkinter.CTkButton(
    app, text="Download Mp3", command=lambda: startDownload("audio"))
download_audio.pack(padx=10, pady=10)


app.mainloop()
