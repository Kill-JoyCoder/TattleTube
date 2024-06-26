import tkinter 
import customtkinter
# import pytube
from pytube import YouTube
import time
#from moviepy.editor import VideoFileClip

def dlaudio():
    try:
        tic = time.perf_counter()
        ytlink= link.get()
        ytobj = YouTube(ytlink)
        audio = ytobj.streams.get_audio_only()
        text = ytobj.title
        #textlabel.configure(text, text_color = 'dark')
        audio.download('./dl/audio')
        toc = time.perf_counter()
        
        print("Downloaded Audio\nTook ",toc-tic, " seconds")
      # print(text)
    except KeyError as ke:
        print("Invalid link", ke)
    # except Exeption as e:
    #     print("invalid", e)

def dlvideo():
    try:
        tic = time.perf_counter()
        ytlink = link.get()
        ytobj = YouTube(ytlink)
        video = ytobj.streams.get_highest_resolution()
        video.download('./dl/video')
        toc = time.perf_counter()
        print("Downloaded Video.\nTook",toc-tic," seconds")
    except:
        print("Invalid")

    # except KeyboardInterrupt as k:
        # print("")    
    
'''def progress(stream, chunk, bytes_remaining):
    #print("JJ") func is werking :D
    total_size = stream.filesize
    bytes_done = total_size - bytes_remaining
    p = bytes_done/total_size *100
    percentage = str(int(p))
    perc.configure(text = percentage + '%')
    perc.update()
'''    
customtkinter.set_appearance_mode("System")
#grey = #53565c
customtkinter.set_default_color_theme("blue")

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
dl = customtkinter.CTkButton(app, text='Download Audio', fg_color="#47484a", hover_color = "#2a4782", command=dlaudio)
dl.place(x=200, y=150)
dl = customtkinter.CTkButton(app, text='Download Video', fg_color="#47484a", hover_color = "#2a4782", command=dlvideo)
dl.place(x=380, y=150)

#progress bar 
'''perc = customtkinter.CTkLabel(app, text = '0%', text_color = 'black')
perc.pack()
pb = customtkinter.CTkProgressBar(app, width = 200)
pb.set(0)
pb.pack(padx=10, pady=10)'''
#progress bar not working nor is the percentage completion

app.mainloop()