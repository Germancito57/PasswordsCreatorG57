from msilib.schema import Font
from tkinter import *
from tkinter import font

from .config import CONFIG


class Window():
  def __init__(self):
    self.window = Tk()
    self.widgets = {}
    self.setWindowProperties()
    self.setWidgets()
    
    self.window.mainloop()
  
  def setWindowProperties(self):
    self.window.title(CONFIG["WINDOW"]["title"])
    self.window.geometry(CONFIG["WINDOW"]["resolution"])
    self.window.resizable(False, False)
    self.window.config(
      background=CONFIG["WINDOW"]["background"],
    )
    self.window.attributes("-alpha", CONFIG["WINDOW"]["alpha"])
  
  def setWidgets(self):
    self.widgets["title"] = Label(self.window, {
      "text" : CONFIG["WINDOW"]["title"],
      "font" : (CONFIG["WINDOW"]["font"], 20, "bold"),
      "fg" : "black",
    })
    self.widgets["title"].place(x=80, y=1)

  

  
