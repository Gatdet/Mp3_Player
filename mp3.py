from tkinter import *
import pygame, os
from pygame import mixer

window = Tk()
window.geometry("500x500")
window.config(bg="#ffde05")
window.title("Mp3 Player")
mixer.init()

dir_path = r"C:\Users\gatde\OneDrive\Documents\mp3_Player"

playlist = [] 

#LISTBOX
listbox = Listbox(window,  height = 500, width = 15, bg = "grey", activestyle = 'dotbox', font = "Helvetica", fg = "yellow", borderwidth=2, relief="solid",)

listbox_index= 0
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)) and path!="mp3.py":
        listbox_index+=1
        playlist.append(path)
        listbox.insert(listbox_index, f"{path}")

song_chosen = 0 #INDEX FOR THE PLAYLIST
song_file = playlist[song_chosen]
song = pygame.mixer.Sound(song_file)
song_playing = False


def play():
    global song_playing

    if song_playing == False: #IF THE SONG ISNT ALRREADY PLAYING
        song.play()
        song_playing=True
    else:
        pass
 
    if pause(): #IF THE MUSIC IS PAUSED
        pygame.mixer.unpause()
   

        
def pause():
    pygame.mixer.pause()
    return True

def next_song():
    global song_file, song_chosen, song
    if song_chosen<=len(playlist):
        pygame.mixer.stop()
        song_chosen+=1
        song_file=playlist[song_chosen]
        song = pygame.mixer.Sound(song_file)
        song.play()

def prev_song():
    global song_file, song_chosen, song
    if song_chosen>0:
        pygame.mixer.stop()
        song_chosen-=1
        song_file=playlist[song_chosen]
        song = pygame.mixer.Sound(song_file)
        song.play()


def display():
    Label(window, font=("arial", 10, "bold"), text="Playlist", bg="#ffbc05", borderwidth=2, relief="solid").place(x=0, y=0, height=30, width=140)

    play_button = Button(window, font=("arial", 14), text="PLAY", command=play, bg= "#ff9f05")
    pause_button = Button(window, font=("arial", 14), text="PAUSE", command=pause, bg="#ff9f05")
    next_button = Button(window, font=("arial", 14), text="NEXT", command=next_song, bg="#ff9f05")
    prev_button = Button(window, font=("arial", 14), text="PREVIOUS", command=prev_song, bg="#ff9f05")

    play_button.place(x=350, y=200)
    pause_button.place(x= 340, y = 240)
    next_button.place(x= 422, y= 240)
    prev_button.place(x= 225, y = 240)
    listbox.place(x=0, y=30)

display()
print(playlist)
window.mainloop()
