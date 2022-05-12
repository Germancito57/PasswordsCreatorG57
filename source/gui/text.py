from tkinter import ttk


def Text(window, text, config, position = {"x" : 10, "y" : 10}):
  text = ttk.Label(window, text=text)
  text.place(x=position["x"], y=position["y"])
  text.config(config)

  return text


