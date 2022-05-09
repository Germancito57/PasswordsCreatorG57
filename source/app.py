import tkinter

from ..data.gui import GUI
from ..data.language import LANGUAGE
from ..utils.password import addPassword, deletePassword, getPasswords


def setAppProperties(window):
  window.title(LANGUAGE["title"])
  window.geometry(f"{GUI['dimensions']['width']}x{GUI['dimensions']['height']}")
  window.resizable(GUI["resizable"], GUI["resizable"])
  window.iconbitmap('source/data/assets/icon.ico')


def hola():
  addPassword({
    "title": "dd",
    "value": 123456,
  })

def deeleee():
  deletePassword(2)
  passwords = getPasswords()
  print(passwords)


def createApp():
  window = tkinter.Tk()
  setAppProperties(window)

  button = tkinter.Button(window, text="Click Me!", command=hola)
  button.pack()

  button2 = tkinter.Button(window, text="Click 222!", command=deeleee)
  button2.pack()


  

  list = tkinter.Listbox(window)
  list.pack()
  passwords = getPasswords()
  print(passwords)
  for id in passwords:
    print(passwords[id]["title"] + " " + str(passwords[id]["value"]))
    list.insert(id, passwords[id]["title"])
    
  window.mainloop()

