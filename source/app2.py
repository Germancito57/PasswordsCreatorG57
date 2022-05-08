import random
import string
from tkinter import *

import clipboard

from .config import CONFIG


class App():

    def __init__(self): 
        self.appConfig = CONFIG["APP"]
        self.window = Tk()
        self.window.title(self.appConfig["title"])
        self.window.geometry(self.appConfig["resolution"])

        self.loadWidgets()
    
        self.window.mainloop()


    def loadWidgets(self):  

        self.pPassword = ""
        self.wPasswordText = StringVar()

        self.wTitle = Label(self.window, text = self.appConfig["title"], font = (self.appConfig["font"], 20,))
        self.wTitle.place(x=80, y=1)

        self.wButtonCreate = Button(self.window, text = "Create new password", fg = "white", bg = "green", font = (self.appConfig["font"], 12), command=self.createPassword)
        self.wButtonCreate.place(x=120,y=80)


        self.wPassword = Label(self.window, text = "", font = (self.appConfig["font"], 10, "bold"), textvariable=self.wPasswordText)
        self.wPassword.place(x=120,y=130)


    def createPassword(self):
        self.pPassword = ""
        self.pCaracters = 18
        self.pStringCaracters = list(string.printable)
        self.pAvalibleCaracts = self.pStringCaracters[:-6]

        for word in range(self.pCaracters):
            self.pPassword += random.choice(self.pAvalibleCaracts)

        self.wPasswordText.set(self.pPassword)

        self.wButtonCopy = Button(self.window, text = "Copy", fg = "white", bg = "green", font = (self.appConfig["font"], 10,), command=self.copyPassword(self.pPassword))
        self.wButtonCopy.place(x=170,y=170)


    def copyPassword(self, toCopy):
        clipboard.copy(toCopy)
