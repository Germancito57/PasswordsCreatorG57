import tkinter

from data.gui import GUI
from data.language import LANGUAGE
from utils.password import addPassword, deletePassword, getPasswords

from gui.frame import Frame


def setAppProperties(window):
  window.title(LANGUAGE["title"])
  window.geometry(f"{GUI['dimensions']['width']}x{GUI['dimensions']['height']}")
  window.resizable(GUI["resizable"], GUI["resizable"])
  window.iconbitmap('source/data/assets/icon.ico')


def createApp():
  window = tkinter.Tk()
  setAppProperties(window)

  left_frame = Frame(window, dict(bg="blue", width=300, height=GUI["dimensions"]["height"]), "left", "y")
  right_frame = Frame(window, dict(bg="red", width=GUI["dimensions"]["width"] - 300, height=GUI["dimensions"]["height"]), "right", "y")
  window.mainloop()

  
