import tkinter

window = tkinter.Tk()

button = tkinter.Button(window, text="Click Me!")
button.pack()

button2 = tkinter.Button(window, text="Click 222!")
button2.pack()




list = tkinter.Listbox(window)
list.pack()

window.mainloop()
