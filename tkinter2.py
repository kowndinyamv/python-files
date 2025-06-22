from tkinter import*
window=Tk()
window.title("Wecome to python GUI")
window.geometry('350x200')
lbl=Label(window,text="Hello",bg="green",fg="white")
lbl.grid(column=1,row=0)
btn=Button(window,text="Click Me",bg="orange",fg="white")
btn.grid(column=1,row=1)
window.mainloop()