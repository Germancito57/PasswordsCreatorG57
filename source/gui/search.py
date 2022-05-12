import tkinter


def Search(window, label, config, position, btnPosition, function):
  modify = tkinter.Entry(window)
  modify.place(x=position["x"], y=position["y"])
  modify.insert(-1, label)
  modify.config(config)

  button = tkinter.Button(window, text="Search", command=lambda: function(modify))
  button.place(x=btnPosition["x"], y=btnPosition["y"])

  return modify



