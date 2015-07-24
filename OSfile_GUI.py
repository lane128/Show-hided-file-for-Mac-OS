__author__ = 'lane'

# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, BOTH
from ttk import Frame, Button, Style
import os


class Example(Frame):
    __h = 300
    __w = 384

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Show/Hide the system file of Mac OS")
        self.pack(fill=BOTH, expand=1)
        buttonW=50
        buttonH=8
        self.parent.geometry('%dx%d+%d+%d' % (self.__w, self.__h, 100,100))
        quitButton = Button(self, text="Quit",width=buttonW,command=self.quit)
        quitButton.place(x=0,y=buttonH*6)
        showButton=Button(self,text="Show the system file",width=buttonW,command=self.showInfo)
        showButton.place(x=0,y=0)
        hideButton=Button(self,text="Hide the system file",width=buttonW,command=self.hideInfo)
        hideButton.place(x=0,y=buttonH*3)
        #self.focus()
        print "-->>The GUI app start!"


    def showInfo(self):
        os.system('defaults write com.apple.finder AppleShowAllFiles -bool true')
        os.system('killall Finder')
        print "-->>The system file are shown."

    def hideInfo(self):
        os.system('defaults write com.apple.finder AppleShowAllFiles -bool false')
        os.system('killall Finder')
        print "-->>The system file are hided."


def main():
    root = Tk()
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
