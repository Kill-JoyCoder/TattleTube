from moviepy.editor import *
import pygame

l = input("Enter the .mp4 name>_ ")
video = VideoFileClip(l)
l.split(".")
l += ".mp3"
video.audio.write_audiofile(l)
pygame.mixer.music.load("l")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(loops=1,fade_ms=5000)
