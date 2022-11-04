import os
import unicodedata
import unidecode
import tkinter as tk
from tkinter.filedialog import askdirectory
#from tkinter.messagebox import showinfo
win = tk.Tk()
win.title("Browser")
win.geometry("800x800")
#def openfile(evt): pass

homedrive = os.environ['PWD']
#rep_source = tk.filedialog.askdirectory()

def ask_question():
    lb.delete(0,tk.END)
    rep_source = tk.filedialog.askdirectory(parent=win, initialdir=homedrive, title="Selectionnez le dossier SOURCE")
    for file in os.listdir(rep_source):
        print (file)
        file = unidecode.unidecode(file)
        print(file)
#        lb.insert(0,"  " + file)
#        print (file)

bt1 = tk.Button(win, text="Open a File", command=ask_question)
bt1.pack()
lb = tk.Listbox(win)
lb.pack(expand=tk.YES, fill=tk.BOTH)
# listbox.bind("<<ListBoxSelect>>",openfile)
#rep_source = tk.filedialog.askdirectory( initialdir = homedrive, title = "Selectionnez le dossier SOURCE")
#rep_source = homedrive
# for file in os.listdir("/Users/mdufosse/Documents/AData/Dev/Python/Prog"):
#rep_source = tk.filedialog.askdirectory(parent=win, initialdir=homedrive, title="Selectionnez le dossier SOURCE")
win.mainloop()
