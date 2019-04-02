# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:12:12 2019

@author: DELL
"""

import pygame
from tkinter import *
from tkinter import filedialog
import nk_package

def mClose():
    pygame.mixer.music.pause()
    mywindow.destroy()
    return

def mPlay(mytext):   
    global paused
    paused=False
    pygame.init()
    pygame.mixer.music.load(mytext)
    pygame.mixer.music.play()

def mPause():
    global paused
    if(paused is True ):
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

class getaudio:
    mytext=""
    def getmyfile(self):
        mywindow.filename= filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("wav files","*.wav"),("all files","*.*")))
        self.mytext=str(mywindow.filename)
        print("In class name is ",self.mytext)
        displaypath.set(self.mytext)
    def getmytext(self):
        print("Return mytext called")
        return self.mytext

def Compress():
    nk_package.lowpass=int(lpass.get())
    print(nk_package.lowpass,type(nk_package.lowpass))
    nk_package.highpass=int(hpass.get())
    print(nk_package.highpass,type(nk_package.highpass))
    nk_package.fname=audio.mytext
    nk_package.fft_dis(nk_package.fname)
    print("In Compress()")

def Extract():
    nk_package.band_pass()

mywindow=Tk()
audio=getaudio()
mywindow.title("\tAudio Compression")
mywindow.geometry("1000x600")
mywindow.resizable(0,0)
mywindow.configure(background="#FFCF4B")
frame0=Frame(mywindow)
frame0.pack(side=TOP)
frame0.configure(background="#FFCF4B")
Label(frame0,text="Band Pass Filter",font=("Calibri","15"),bg="#FFCF4B").pack(padx=10,pady=5)
frame1=Frame(mywindow)
frame1.pack(side=TOP)
frame1.configure(background='#FFCF4B')
Label(frame1,text="Choose your audio file",bg='#FFCF4B',font=("Calibri","10")).pack(padx=10,pady=10,side=LEFT)
displaypath= StringVar()
Label(frame1,textvariable=displaypath).pack(padx=10,pady=10,side=LEFT)
Button(frame1,text="Select File",command=lambda:audio.getmyfile()).pack(padx=10,pady=25,side=LEFT)
frame2=Frame(mywindow)
frame2.pack(padx=20,side=TOP)
frame2.configure(background='#FFCF4B')
Button(frame2,text="Play",command=lambda:mPlay(audio.mytext)).pack(padx=10,pady=10,side=LEFT)
Button(frame2,text="(Un)Pause",command =mPause).pack(padx=10,pady=15,side=LEFT)
Button(frame2,text="Stop",command =mClose).pack(padx=10,pady=20,side=LEFT)
frame3=Frame(mywindow)
frame3.pack(padx=10,side=TOP)
frame3.configure(background='#FFCF4B')
frame4=Frame(mywindow)
frame4.pack(padx=20,side=TOP)
frame4.configure(background='#FFCF4B')
Label(frame4,text="Low Pass Frequency here : ",bg="#FFCF4B").pack(padx=10,pady=5,side=LEFT)
lpass=Entry(frame4)
lpass.pack(padx=10,pady=15,side=LEFT)
Label(frame4,text="High pass Frequency here : ",bg="#FFCF4B").pack(padx=15,pady=5,side=LEFT)
hpass=Entry(frame4)
hpass.pack(padx=15,pady=15,side=LEFT)
Button(frame3,text="FFT visual before filtering",command=lambda:Compress()).pack(padx=10,pady=20,side=LEFT) 
Button(frame3,text="FFT visual after filtering",command=lambda:Extract()).pack(padx=10,pady=25,side=LEFT)
mywindow.mainloop()