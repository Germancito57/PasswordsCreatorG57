import tkinter


def List(window, elements, config, position = {"x" : 10, "y" : 10}):
  list = tkinter.Listbox(window)
  list.place(x=position["x"], y=position["y"])
  list.config(config)
  for element in elements:
    list.insert(tkinter.END, elements[element]["title"])

  return list


