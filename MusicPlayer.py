from tkinter import *
import tkinter as tk
from pygame import mixer
from tkinter import filedialog ,ttk
import os
from PIL import Image, ImageTk

r=Tk()
r.title('Music Player')
r.geometry('850x670+290+258')
r.configure(bg='#0f1a2b')
r.resizable(False,False)

mixer.init()

def openf():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for s in songs:
            if s.endswith(".mp3"):
                playlist.insert(END,s)
        

def playSong():
    MName=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    
    








icon=PhotoImage(file='D://python//imagesforprojects//Logoformusicplayer.png')
r.iconphoto(False,icon)

t=Image.open("D://python//imagesforprojects//z.png")


re = t.resize((850,280))

size_image=ImageTk.PhotoImage(re)

Label(r,image=size_image,bg='#0f1a2b').pack()


play=Image.open("D://python//imagesforprojects//play.jpg")
res = play.resize((60,60))
si=ImageTk.PhotoImage(res)
#resume
Button(r,image=si,bg='#0f1a2b',command=mixer.music.unpause).place(x=200,y=480)




pau=Image.open("D://python//imagesforprojects//pauses.jpg")
paus = pau.resize((60,60))
pause=ImageTk.PhotoImage(paus)
#pause
Button(r,image=pause,bg='#0f1a2b',command=mixer.music.pause).place(x=115,y=480)

st=Image.open("D://python//imagesforprojects//stop.jpg")
sto = st.resize((60,60))
stop=ImageTk.PhotoImage(sto)
#stop
Button(r,image=stop,bg='#0f1a2b',command=mixer.music.stop).place(x=30,y=480)


pl=Image.open("D://python//imagesforprojects//plays.jpg")
pla = pl.resize((60,60))
plays=ImageTk.PhotoImage(pla)
#play
Button(r,image=plays,bg='#0f1a2b',command=playSong).place(x=115,y=380)


Me=Image.open('D://python//imagesforprojects//meus.png')
Men=Me.resize((570,700))
Menu=ImageTk.PhotoImage(Men)
Label(r,image=Menu,bg="#0f1a2b").pack(padx=10,pady=30,sid=RIGHT)



fra=tk.Frame(r,bd=2,relief=RIDGE,bg="#0f1a2b")

fra.place(x=285,y=370,width=540,height=250)

Button(r,text="Open Folder", width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",command=openf).place(x=300,y=318)

scroll=Scrollbar(fra)
playlist=Listbox(fra,width=100,font=("arial",10),bg="#333333",fg="yellow",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)






r.mainloop()
    