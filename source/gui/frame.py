import tkinter


def Frame(window, config, side, fill):
  frame = tkinter.Frame(window)
  frame.config(config)
  frame.pack(side=side, fill=fill)
  return frame


