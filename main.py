import p
import re
#from pytube import Playlist
from pytube import YouTube

def video(link):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download('./Downloads')
video(input("Enter the link>_ "))
#p.prin()
