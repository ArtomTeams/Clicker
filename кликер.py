from tkinter import *
import tkinter as tk
n=0
root=Tk()
root.title("Clicer")
root.geometry("500x500")
def callback():
    global n
    n +=1
    text.configure(text=n)
text=tk.Label(root, text='0', bg='black', fg='green', width=15, font='Arial 20')
text.place(x=1, y=2)
button1=Button(root, text= '*click*', width=10, height=5, bg='black', fg='red', font='arial 14', command=callback)
button1.place(x=200, y=150)
root.mainloop()
