# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:12:12 2019

@author: DELL
"""

import pygame
from tkinter import *
from tkinter import filedialog
import Package

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
    Package.fname=audio.mytext
    Package.cutOffFrequency=float(cutoff.get())
    print(Package.cutOffFrequency,type(Package.cutOffFrequency))
    Package.fft_dis(Package.fname)

def Extract():
    Package.create_output()

mywindow=Tk()
audio=getaudio()
mywindow.title("\tAudio Compression")
mywindow.geometry("1000x600")
mywindow.resizable(0,0)
mywindow.configure(background="#17BBB0")
frame0=Frame(mywindow)
frame0.pack(side=TOP)
frame0.configure(background='#17BBB0')
Label(frame0,text="Digital Low-Pass Filter by means of convolution",font=("TimesNewRoman","15"),fg="#1E003D",bg="#17BBB0").pack(padx=10,pady=5)
frame1=Frame(mywindow)
frame1.pack(side=TOP)
frame1.configure(background='#17BBB0')
Label(frame1,text="Select Audio Files Here",bg='#17BBB0',font=("TimesNewRoman","10")).pack(padx=10,pady=10,side=LEFT)
displaypath= StringVar()
Label(frame1,textvariable=displaypath).pack(padx=10,pady=10,side=LEFT)
Button(frame1,text="Select File",command=lambda:audio.getmyfile()).pack(padx=10,pady=25,side=LEFT)
frame2=Frame(mywindow)
frame2.pack(padx=20,side=TOP)
frame2.configure(background='#17BBB0')
Button(frame2,text="Play",command=lambda:mPlay(audio.mytext)).pack(padx=10,pady=10,side=LEFT)
Button(frame2,text="(Un)Pause",command =mPause).pack(padx=10,pady=15,side=LEFT)
Button(frame2,text="Stop",command =mClose).pack(padx=10,pady=20,side=LEFT)
frame3=Frame(mywindow)
frame3.pack(padx=10,side=TOP)
frame3.configure(background='#17BBB0')
Button(frame3,text="Frequency vs Power before Filtering",command=lambda:Compress()).pack(padx=10,pady=20,side=LEFT) 
Button(frame3,text="Frequency vs Power after Filtering",command=lambda:Extract()).pack(padx=10,pady=25,side=LEFT)
frame4=Frame(mywindow)
frame4.pack(padx=20,side=TOP)
frame4.configure(background='#17BBB0')
Label(frame4,text="Cut-off Frequency here : ").pack(padx=10,pady=5,side=LEFT)
cutoff=Entry(frame4)
cutoff.pack(padx=10,pady=15,side=LEFT)
mywindow.mainloop()