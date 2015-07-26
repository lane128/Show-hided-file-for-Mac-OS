__author__ = 'lane128.top'

# !/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python

from Tkinter import *
from tkMessageBox import *
import os

def showOpt():
	os.system('defaults write com.apple.finder AppleShowAllFiles -bool true')
	os.system('killall Finder')
	showinfo('Show file','The system file are shown')
	print "-->>The system file are shown."

def hideOpt():
	os.system('defaults write com.apple.finder AppleShowAllFiles -bool false')
	os.system('killall Finder')
	showinfo('Hide file','The system file are hided')
	print "-->>The system file are hided."

def quitOpt():
	userRep=askyesno('Quit', 'Do you want to quit?')
	if userRep:
		print "-->>Your have quited the programme."
		quit()

def centerWindow(self):
	w = 300
	h = 160
	sw = self.winfo_screenwidth()
	sh = self.winfo_screenheight()
	x = (sw - w) / 2
	y = (sh - h) / 2
	self.geometry('%dx%d+%d+%d' % (w, h, x, y))

def iniFrame():
	root=Tk()
	root.title('Show/Hide the system file of Mac OS')
	centerWindow(root)
	Label(text='This is the tool to show/hide\n your mac os system file.\n develoment by Lane128',width=200,height=4,bg='#D3D3D3').pack(fill=BOTH)
	Button(text='Show the system file',bg='#D3D3D3',command=showOpt).pack(fill=BOTH)
	Button(text='Hide the system file',bg='#D3D3D3',command=hideOpt).pack(fill=BOTH)
	Button(text='Quit',bg='#D3D3D3',command=quitOpt).pack(fill=BOTH)
	root.resizable(False,False)
	root.mainloop()

if __name__=='__main__':
	iniFrame()
