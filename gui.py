import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions import *

# creating the window 
root= tk.Tk()

root.geometry("350x200")
root.resizable(False, False)

root.title("Library Information Session")

Label(root, text="Welcome to the Library Information Session.").grid(row=1, column=1, padx=30)
Label(root, text="Please pick an option from the drop down menu,").grid(row=2, column=1, padx=30)
Label(root, text="Thank you!").grid(row=3, column=1, padx=20)   

# defining mylab variable
mylab=Label(root)

sel = StringVar()
e = StringVar()

# creating to_type function to output different labels based on what is picked 
def to_type(*args):
    global mylab
    mylab.destroy()
    if sel.get() == "Subject":
        mylab=Label(root, text="Please input your part or full subject")
        mylab.grid(row=5, column=1)
    elif sel.get() == "Classmark":
        mylab=Label(root, text="Please input your classmark")
        mylab.grid(row=5, column=1)
    elif sel.get() == "Location":
        mylab=Label(root, text="Please input your location")
        mylab.grid(row=5, column=1)
    

# creating click command to use for button
def click():
    if sel.get() == "Subject":
        result = subject(e.get())
        messagebox.showinfo("Your Information", result)
        entryb.delete(0, END)
    elif sel.get() == "Classmark":
        result = classmark(e.get())
        messagebox.showinfo("Your Information", result)
        entryb.delete(0, END)
    elif sel.get() == "Location":
        result = location(e.get())
        messagebox.showinfo("Your Information", result)
        entryb.delete(0, END)

# creating a function to make all entries in the entrybox all capitals
def to_upper(*args):
    e.set(e.get().upper())

# options for a drop down menu
options=["Subject",
         "Classmark",
         "Location"]

# creating the drop down menu box
combo = ttk.Combobox(root, values=options, text = sel)
combo.grid(row=4, column=1, pady=10)

# creating an entry box
entryb=Entry(root, width=25, textvariable=e)
entryb.grid(row=6, column=1, pady=5)

# creating a button
but=Button(root, text="Search", command=click)
but.grid(row=7, column=1, pady=5)

# tracing variables to the defined functions
sel.trace('w', to_type)
e.trace('w', to_upper)

root.mainloop()
 