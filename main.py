import tkinter 
import customtkinter
from pytube import YouTube

def dlaudio():
    try:
        ytlink= link.get()
        ytobj = YouTube(ytlink)
        audio = ytobj.streams.get_audio_only()
        audio.download('./dl/audio')
        print("Downloaded Audio")
    except:
        print("invalid")

def dlvideo():
    try:
        ytlink = link.get()
        ytobj = YouTube(ytlink)
        video = ytobj.streams.get_highest_resolution()
        video.download('./dl/video')
        print("Downloaded Video")
    except:
        print("Invalid")
    
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#app frame
app = tkinter.Tk()
app.geometry("720x480")
app.title("TattleTube")

#UI elem
title = customtkinter.CTkLabel(app, text="Link", width=100, height=20, text_color="black")
title.pack(padx=10, pady=10)

#input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40,textvariable=url_var)
link.pack()

#download
dl = customtkinter.CTkButton(app, text='Download Audio', command=dlaudio)
dl.pack(padx=10, pady=10)
dl = customtkinter.CTkButton(app, text='Download Video', command=dlvideo)
dl.pack(padx=10, pady=10)
#runs app
app.mainloop()