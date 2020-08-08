from tkinter import *
from pytube import YouTube
from tkinter import ttk
import os
from PIL import Image,ImageTk
import time
import clipboard
window = Tk()
window.title('YouTube Downloader')
re = window.geometry('300x320+500+120')
window.resizable(False,False)
window.iconbitmap('icons/yt.ico')
im = ImageTk.PhotoImage(Image.open('icons/ytt.png').resize((300,150) , Image.ANTIALIAS  ))
la = Label(image=im)
la.grid(row=1,column=1,)
e = Entry(window)
e.grid(row=2,column=1,ipadx=35,ipady=5,pady=5)
def paste():
    e.delete(0,END)
    e.insert(0,clipboard.paste())
l = Button(text="Paste",command=paste,width=20,fg='red',bg='white').grid(row=3,column=1)
global deja
deja = False
lone = Label(text='Nothing is Compeleted')
lone.grid(row=12,column=1)
def Import():
    yt = YouTube(e.get())
    lab = Label(text=yt.title,width=30).grid(row=5,column=1)
    def mp4():
        wuba = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download()
        new = str(wuba.replace(' ','-'))
        os.rename(str(wuba),new)
        os.system(new)
        lone.config(text=yt.title+' is completed')
    Button(text="Download Mp4 !",command=mp4,bg='white',fg='red',width=20).grid(row=6,column=1)
b = Button(text='Import',command=Import,bg='red',fg='white',width=20).grid(row=4,column=1)
window.mainloop()
#made by Simo2304