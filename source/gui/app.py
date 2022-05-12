import tkinter

from data.gui import GUI
from data.language import LANGUAGE
from theme.set import set_theme
from utils.information import showPasswordInformation
from utils.password import getPasswords, searchPassword

from gui.frame import Frame
from gui.list import List
from gui.search import Search

left_frame, right_frame = None, None
search, list, pTitle, pDescription, pValue, pTags, pNotes = None, None, None, None, None, None, None
selected = None

def setAppProperties(window):
  window.title(LANGUAGE["title"])
  window.geometry(f"{GUI['dimensions']['width']}x{GUI['dimensions']['height']}")
  window.resizable(GUI["resizable"], GUI["resizable"])
  window.iconbitmap('source/data/assets/icon.ico')


def select(event):
  global selected
  elements = getPasswords()
  for element in elements:
    try:
      if elements[element]["title"] == list.get(list.curselection()[0]):
        selected = elements[element]
    except IndexError:
      selected = None
    finally:
      showPasswordInformation()

  

def createApp():
  window = tkinter.Tk()
  setAppProperties(window)

  global left_frame, right_frame, search, list
  set_theme("dark")
  left_frame = Frame(window, dict(bg=GUI["colors"]["primary"], width=300, height=GUI["dimensions"]["height"]), "left", "y")
  right_frame = Frame(window, dict(bg=GUI["colors"]["secondary"], width=GUI["dimensions"]["width"] - 300, height=GUI["dimensions"]["height"]), "right", "y")
  search = Search(left_frame, "Search", dict(width = 20, font=('Inter', 12)), dict(x=10, y=10), dict(x=219, y=10), function = searchPassword)
  list = List(left_frame, getPasswords(), dict(fg="#ffffff", bg="#1c1c1c", highlightbackground='white', width = 25, height = 22, font=('Inter 15')), dict(x=10, y=50))
  list.bind("<<ListboxSelect>>", select)

  showPasswordInformation()
  window.mainloop()

  
