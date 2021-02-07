from tkinter import *
from tkinter.messagebox import showinfo 
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import os
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak():
    global file
    engine.say(textarea.get(1.0, END))
    engine.runAndWait()

def newfile():
    global file
    root.title("Untitled - Notepad")
    file =None
    textarea.delete(1.0, END)

def openfile():
    global file 
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0,END)
        f=open(file, "r")
        textarea.insert(1.0, f.read())
        f.close

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename((file)) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()
def cuttext():
    textarea.event_generate(("<<Cut>>"))
def copytext():
    textarea.event_generate(("<<Copy>>"))
def pastetext():
    textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad developed by rishabh srivastava")




if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("600x400")
    #add text area
    textarea =  Text(root, font = "lucida 13")
    file = None
    textarea.pack(fill=BOTH, expand =True)

    #menu bar
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff = 0)
    # to open new file
    filemenu.add_command(label= "New", command=newfile)
    #to open already existing file
    filemenu.add_command(label="Open", command=openfile)
    #to save the current file
    filemenu.add_command(label="Save", command= savefile)
    filemenu.add_separator()
    #to add exit command
    filemenu.add_command(label="Exit", command=quitapp )
    menubar.add_cascade(label="File", menu=filemenu)
    
    #edit menu
    editmenu = Menu(menubar, tearoff = 0)
    #to cut 
    editmenu.add_command(label="Cut", command=cuttext)
    #to copy
    editmenu.add_command(label="Copy", command=copytext)
    #to paste
    editmenu.add_command(label="Paste", command=pastetext)
    menubar.add_cascade(label="Edit", menu=editmenu)

    #help menu
    helpmenu = Menu(menubar, tearoff = 0)
    helpmenu.add_command(label="About notepad", command=about)
    helpmenu.add_command(label="help")
    menubar.add_cascade(label="Help", menu=helpmenu)
    menubar.add_command(label="speak", command=speak)
    root.config(menu = menubar)

    #adding scroll bar
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    
    root.mainloop()
"""
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    for i in range(1, 3000):
        speak(f"")"""