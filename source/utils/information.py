from turtle import color

import gui.app as app
from gui.text import Text


def setPasswordValuesInformation(state):
  
  if app.pTitle != None:
    app.pTitle.config(text="")
    app.pDescription.config(text="")
    app.pValue.config(text="")
    app.pTags.config(text="")
    app.pNotes.config(text="")

  if state:
    app.pTitle = Text(app.right_frame, app.selected["title"], dict(font=('Inter 30 bold')), dict(x=160, y=50))
    app.pDescription = Text(app.right_frame, app.selected["description"], dict( font=('Inter 15')), dict(x=30, y=130))
    app.pValue = Text(app.right_frame, app.selected["value"], dict(font=('Inter 15')), dict(x=30, y=210))
    app.pTags = Text(app.right_frame, app.selected["tags"], dict(font=('Inter 15')), dict(x=30, y=290))
    app.pNotes = Text(app.right_frame, app.selected["notes"], dict(font=('Inter 15')), dict(x=30, y=400))
  else:
    app.pTitle = Text(app.right_frame, "Selecciona una contraseña", dict(font=('Inter 25')), dict(x=70, y=100)) 
    app.pDescription = Text(app.right_frame, "", dict(font=('Inter 15')), dict(x=1, y=30))
    app.pValue = Text(app.right_frame, "", dict(font=('Inter 15')), dict(x=1, y=60))
    app.pTags = Text(app.right_frame, "", dict(font=('Inter 15')), dict(x=1, y=90))
    app.pNotes = Text(app.right_frame, "", dict(font=('Inter 15')), dict(x=1, y=120))

def showPasswordInformation():
  setPasswordValuesInformation(app.selected != None)
