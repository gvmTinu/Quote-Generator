from tkinter import *
import random

root = Tk()
root.title("Quote Generator @gVm")
root.geometry("500x400")

q = ["Life is what happens when you're busy making other plans.","The future belongs to those who believe in the beauty of their dreams.","Whoever is happy will make others happy too.","Tell me and I forget. Teach me and I remember. Involve me and I learn.","Always remember that you are absolutely unique. Just like everyone else.","The way to get started is to quit talking and begin doing.","The greatest glory in living lies not in never falling, but in rising every time we fall.","Sometimes later becomes never.", "Dream it. Do it.", "Never take the easy way out"]

lbl = Label(root, text="This is a quote generator.\n Press the button to generate new quotes.", font=('', 12))
lbl.place(relx=0.5, rely=0.1, anchor=N)

quote = Label(root, text="Work before glory", font=('', 22))
quote.place(relx=0.5, rely=0.5, anchor=CENTER)


def generate():
    quote.configure(text=random.choice(q))

 
submit = Button(root, text="Generate", bg="black", fg="white", command=generate)
submit.place(relx=0.5, rely=0.9, anchor=S)

root.mainloop()
