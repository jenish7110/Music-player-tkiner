from tkinter import filedialog
from tkinter import messagebox
import time
global tag
def createwidgis():
    Trackl1 = Label(root, text="SELECT-AUDIO ", bg="#ffb88c", font=("arial 13 bold"),)
    Trackl1.grid(row=0, column=0, padx=0, pady=20)

    select_entrybox = Entry(root, width=35, font=("arial 13 bold"), textvariable=audiotrack )
    select_entrybox.grid(row=0, column=1, padx=0, pady=20)

    searchbtn = Button(text="Search", bg="#ffb88c", font=("arial 13 bold"), width=10, command=musicurl)
    searchbtn.grid(row=0, column=2, padx=50, pady=0)

    # playbtn = Button(text="Play", bg="#ffb88c", font=("arial 13 bold"), width=10)
    # playbtn.grid(row=1, column=0, padx=100, pady=20)
    playbtn = Button(image=p1, border=0,command=playsong)

    playbtn.grid(row=4, column=0)

    # pausebtn= Button(text="Pause", bg="#ffb88c", font=("arial 13 bold"), width=10)
    # pausebtn.grid(row=1, column=1, padx=100, pady=20)
    root.pausebtn = Button(image=p0, border=0,command=pause)
    root.pausebtn.grid(row=4, column=1)



    root.resumebtn = Button(image=p6, border=0, command=playresume)
    root.resumebtn.grid(row=4, column=1)
    root.resumebtn.grid_remove()


    vibtn = Button(image=p2, border=0,command=volup)
    vibtn.grid(row=5, column=0, padx=100, pady=20)

    stopbtn = Button(image=p3, border=0,command=stopsong)
    stopbtn.grid(row=4, column=2, padx=25, pady=20)

    vdbtn = Button(image=p4, border=0,command=voldown)
    vdbtn.grid(row=5, column=2, padx=25, pady=20)

    root.mu = Button(image=p5,border=0,command=soundoff)
    root.mu.grid(row=5, column=1, pady=100)

    root.unmu = Button(image=p7, border=0, command=soundon)
    root.unmu.grid(row=5, column=1, pady=100)
    root.unmu.grid_remove()

    root.img=Label(image=p8)
    root.img.grid(row=0, column=4, pady=10)




def soundoff():
    global cv
    cv=mixer.music.get_volume()
    print(cv)
    mixer.music.set_volume(0)
    root.mu.grid_remove()
    root.unmu.grid()
    taglabel.configure(text='Muted...')

def soundon():
    global cv
    root.mu.grid()
    root.unmu.grid_remove()
    mixer.music.set_volume(cv)
    taglabel.configure(text='')

def volup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
    volbar1['value']=vol*100

def voldown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)
    volbar1['value'] = vol * 100

def stopsong():
    mixer.music.stop()
    taglabel.configure(text='Stopped')


def playresume():
    root.pausebtn.grid()
    root.resumebtn.grid_remove()
    mixer.music.unpause()
    taglabel.configure(text='Playing...')




def pause():
    mixer.music.pause()
    root.pausebtn.grid_remove()
    root.resumebtn.grid()
    taglabel.configure(text='Pause')


def playsong():
    global taglabel
    tmp=audiotrack.get()
    try:
    	mixer.music.load(tmp)
    	mixer.music.play()
    	taglabel.configure(text='Playing...')
    except Exception as e:
    	messagebox.showerror("waring","Please select the song!!")
    
    
        



def musicurl():
    dir = filedialog.askopenfilename(title="Select Song")
    audiotrack.set(dir)










from tkinter import *
from pygame import mixer
from  tkinter.ttk import Progressbar


root = Tk()
root.geometry("900x500+200+50")
root.title("MUSIC PLAYER")
root.iconbitmap('music-512.ico')
#root.resizable(False, False)
#root.config(bg="#42275a")
p0 = PhotoImage(file="p.png")
p1 = PhotoImage(file="group(1).png")
p2 = PhotoImage(file="plus_50x50.png")
p3 = PhotoImage(file="stp.png")
p4 = PhotoImage(file="minus_50x50.png")
p5 = PhotoImage(file="sp1.png")
p6= PhotoImage(file="ress.png")
p7 = PhotoImage(file="27150_50x50.png")
p8 = PhotoImage(file="1871.png")

labstr = "MADE-BY-JENISH\n\t"
count = 0
cv=3
text = ''
audiotrack = StringVar()
SliderLabel = Label(root, text=labstr, font=("arial 13 bold"))
SliderLabel.grid(row=7, column=1, padx=0, pady=0, )

taglabel = Label(root, text='MUSIC-PlAYER', font=("arial 13 bold"))
taglabel.grid(row=1, column=1, padx=0, pady=0, )

volbarlabel = Label(root, text="", bg="red")
volbarlabel.grid(row=5, column=3, pady=40)

volbar1 = Progressbar(volbarlabel, orient=VERTICAL, mode="determinate", value=10000, length=110, )
volbar1.grid(row=5, column=30)


##################################################################
'''
Progressbarlabel=Label(root,text="",bg="red")
Progressbarlabel.grid(row=1,column=1,pady=40)

progressbarvol=Progressbar(Progressbarlabel,orient=HORIZONTAL,mode="determinate",value=0,length=400)
progressbarvol.grid(row=1,column=1)
'''
##############################################################
def nameslide():
    global count, text
    if count >= len(labstr):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text + labstr[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(100, nameslide)


mixer.init()
nameslide()
createwidgis()
root.mainloop()
