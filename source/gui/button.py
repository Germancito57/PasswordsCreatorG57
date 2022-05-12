from tkinter import ttk


def Button(window, text, position = {"x" : 10, "y" : 10}, function = None):
  button = ttk.Button(window, text=text, command=function)
  button.place(x=position["x"], y=position["y"])
  return button


