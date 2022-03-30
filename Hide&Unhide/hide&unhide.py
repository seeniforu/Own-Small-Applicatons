from cProfile import label
import tkinter as tk
from tkinter import *
import os
from numpy import size
from tkinter import filedialog

path = []

def hide_files():
    file_path = filedialog.askopenfilename()
    path.append(file_path)
    file_name = get_filename(file_path)
    os.system('cmd /c attrib +h +s +r '+file_name)
    label = Label(root, text = "File Hidden")
    label.place(x = 6, y = 30) 
    root.after(2000, label.destroy)

def unhide_files():
    unhide_name = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    os.system('cmd /c attrib -h -s -r '+unhide_name)
    label=tk.Label(root, text = "File UnHidden")
    label.place(x = 230, y = 30)
    root.after(2000, label.destroy)

def get_filename(path_of_file):
    count = 0
    for i in path_of_file:
        count= count +1
        if i == '/':
            temp_str = path_of_file[count:]
    return temp_str

def send(a):
    password = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if password == "hello":
        Label(root, text = "Enter Name of the file in below Password field and Click UNHIDE").place(x = 6, y = 10) 
        hide_button = Button(root, font=("Sans Serif",12,'bold italic'), text="Hide", width="5", height=5,          
                    bd=0,bg='green',activebackground="#3c9d9b",fg='#000000',
                    command= lambda: hide_files(), overrelief='groove', relief='sunken')
        hide_button.place(x=100, y=30, height=45)

        unhide_button = Button(root, font=("Sans Serif",12,'bold italic'), text="unHide", width="5", height=5,          
                    bd=0,bg='green',activebackground="#3c9d9b",fg='#000000',
                    command= lambda: unhide_files(), overrelief='groove', relief='sunken')
        unhide_button.place(x=170, y=30, height=45)
    else:
         print("Sorry Password is Wrong!")

root = Tk()
root.title("Hide/Unhide Files")                  
root.geometry("400x150")
root.resizable(width=TRUE, height=TRUE)
Label(root, text = "Enter Password : ").place(x = 6, y = 70) 
SendButton = Button(root, font=("Sans Serif",12,'bold italic'), text="Enter", width="12", height=5,          
                    bd=0,bg='green',activebackground="#3c9d9b",fg='#000000',
                    command= lambda: send(1), overrelief='groove', relief='sunken')

EntryBox = Text(root, bd=0, bg="white",width="10", height="3", font="Arial" )
EntryBox.bind("<Return>",send)
                 
EntryBox.place(x=6, y=101, height=45, width=265)
SendButton.place(x=270, y=101, height=45)


root.mainloop()