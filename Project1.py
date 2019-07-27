import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk
from pygame import mixer


root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
statusbar = Label(root, text="TRUCODER'S MUSIC PLAYER",relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

#create the menubar
menubar = Menu(root)
root.config(menu=menubar)

def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1

#create the submenu
submenu = Menu(menubar, tearoff=0)

playlist = []
menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Open', command=browse_file)
submenu.add_command(label='Exit', command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('About Us', 'This is about us')

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=submenu)
submenu.add_command(label='About Us', command = about_us)


mixer.init()

root.title("Music Player")
root.iconbitmap(r'music.ico')

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30, pady=30)

playlistbox = Listbox(leftframe)
playlistbox.pack()

addBtn = ttk.Button(leftframe, text="+ Add", command=browse_file)
addBtn.pack(side=LEFT)

def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)

delBtn = ttk.Button(leftframe, text="- Del", command=del_song)
delBtn.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(pady=60)



text = Label(root, text='hello')
text.pack(pady=10, padx=10)


def play_music():
    try:
        selected_song = playlistbox.curselection()
        selected_song = int(selected_song[0])
        play_it = playlist[selected_song]
        mixer.music.load(play_it)
        mixer.music.play()
        statusbar['text'] = 'Playing Music' + '- ' + os.path.basename(filename_path)
    except:
        tkinter.messagebox.showerror('File not found','Please select a file')

def stop_music():
    mixer.music.stop()
    statusbar['text'] = 'Music Stopped'

def pause_music():
    mixer.music.pause()
    statusbar['text'] = 'Music Paused'

def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)

muted = FALSE

def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(1)
        volumeBtn.configure(image=volumePhoto)
        scale.set(100)
        muted = FALSE
    else:
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE


middleframe = ttk.Frame(rightframe)
middleframe.pack(pady=10)

playPhoto = PhotoImage(file='play.png')
playBtn = ttk.Button(middleframe, image=playPhoto, command=play_music)
playBtn.grid(row=0, column=0, padx=10)

stopPhoto = PhotoImage(file='stop.png')
stopBtn = ttk.Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = ttk.Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=10)

bottomframe = ttk.Frame(rightframe)
bottomframe.pack()

mutePhoto = PhotoImage(file='mute.png')
volumePhoto = PhotoImage(file='volume.png')
volumeBtn = ttk.Button(bottomframe, image=volumePhoto, command=mute_music)
volumeBtn.grid(row=0, column=1)

scale = ttk.Scale(bottomframe, from_=0, to_=100, orient=HORIZONTAL, command=set_vol)
scale.set(100)
scale.grid(row=0, column=2, pady=15, padx=30)


root.mainloop()