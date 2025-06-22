from tkinter import *
window = Tk()
window.title("Welcome to AH CAREER")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=1)
def clicked():
 lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=2)
window.mainloop()