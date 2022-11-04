import os
#import unicodedata
import unidecode
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pathlib import Path

win = tk.Tk()
win.title("Suppression caracteres accentues")
win.geometry("800x800")
#def openfile(evt): pass
Lsize = 0
homedrive = os.environ['PWD']
rep_source = os.environ['PWD']

def ask_question():
    lb.delete(0,tk.END)
    global Lsize
    global rep_source
    rep_source = tk.filedialog.askdirectory(parent=win, initialdir=homedrive, title="Selectionnez le dossier SOURCE")
    for file in os.listdir(rep_source):
#        print (file)
        fileDec = unidecode.unidecode(file)
#        print(file)
        lb.insert(0,"  " + file)
        if file != fileDec :
            lb.insert(1,"  "+"\t" + fileDec)
#        lb.pack(expand=tk.YES, fill=tk.BOTH)
    win.update()
    Lsize= lb.size()
#   print(Lsize)
    if Lsize != 0 :
        do_job()


def do_job():
    global rep_source
    msg_box = tk.messagebox.askquestion('Return', 'Validation des modifications ?',
                                        icon='warning',parent=win)
    if msg_box == 'yes':
#        win.destroy()
        pass
        for file in os.listdir(rep_source):
            fileDec = unidecode.unidecode(file)
            if file != fileDec :
                pass
                filePath = Path(rep_source)
                newFile = filePath / fileDec
                oldFile = filePath / file
                try:
                    os.rename(oldFile, newFile)
                except Exception as e:
                    print(str(e))    
                    tk.messagebox.showinfo('Return', str(e), parent=win)
                    break

        tk.messagebox.showinfo('Return', 'Traitement terminé', parent=win)
    else:
        tk.messagebox.showinfo('Return', 'Modifications non effectuées', parent=win)


bt1 = tk.Button(win, text="Open a File", command=ask_question)
bt1.pack()
lb = tk.Listbox(win)
lb.pack(expand=tk.YES, fill=tk.BOTH)
# listbox.bind("<<ListBoxSelect>>",openfile)
win.mainloop()
