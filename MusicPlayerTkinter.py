from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init()
music_file = None


def add_music():
    global music_file
    music_file = askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3")])
    if music_file != "":
        songs_list.insert(END, os.path.basename(music_file))


def delete_music():
    current_selection = songs_list.curselection()
    if current_selection:
        songs_list.delete(current_selection)
    else:
        songs_list.delete(1)


def callback(event):
    global music_file
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)

    if music_file is not None:
        a = music_file.split(os.path.basename(music_file))[0]
        pygame.mixer.music.load(os.path.join(str(a), value))
        pygame.mixer.music.play()


def play_music():
    global music_file

    if music_file is not None:
        a = music_file.split(os.path.basename(music_file))[0]
        pygame.mixer.music.load(os.path.join(str(a), os.path.basename(music_file) ))
        pygame.mixer.music.play()


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500")
    root.minsize(500, 400)
    root.maxsize(700, 700)
    root.title("Music Player")
    root.wm_iconbitmap("MusicPlayerIcon.ico")

    # Add ScrollBar to ListBox
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    Label(root, text="Songs List", font="lucida 15", bg="grey", fg="white").pack(fill=X, pady=5, padx=15)

    # ListBox
    songs_list = Listbox(root, name='songs_list', yscrollcommand=scrollbar.set)
    songs_list.pack(fill=BOTH, padx=15)
    songs_list.insert(END, "Add Some Music Files To Play")
    songs_list.bind("<<ListboxSelect>>", callback)
    scrollbar.config(command=songs_list.yview)

    # Add & Delete Button
    frame = Frame(root)
    Button(frame, text="Add", pady=8, padx=20, font="lucida 10", command=add_music).pack(side=LEFT, padx=20)
    Button(frame, text="Delete", pady=8, padx=16, font="lucida 10", command=delete_music).pack(side=LEFT)
    frame.pack(padx=20, pady=20)

    # Play, Stop, Pause, Resume Button
    frame2 = Frame(root)
    Button(frame2, text="Play", pady=8, padx=20, bg="grey", fg="white", font="lucida 10", command=play_music).pack(side=LEFT, padx=10)
    Button(frame2, text="Stop", pady=8, padx=20, bg="grey", fg="white", font="lucida 10", command=mixer.music.stop).pack(side=LEFT, padx=10)
    Button(frame2, text="Pause", pady=8, padx=20, bg="grey", fg="white", font="lucida 10", command=mixer.music.pause).pack(side=LEFT, padx=10)
    Button(frame2, text="Resume", pady=8, padx=20, bg="grey", fg="white", font="lucida 10", command=mixer.music.unpause).pack(side=LEFT, padx=10)
    frame2.pack(padx=20, pady=10)

    Label(root, text="TKinter Music Player", font="lucida 10", bg="black", fg="white").pack(side=BOTTOM, fill=X)

    root.mainloop()
