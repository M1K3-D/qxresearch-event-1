import os
import unidecode
import tkinter as tk
from tkinter.filedialog import askdirectory
from pathlib import Path
from functools import partial

win = tk.Tk()
win.title("Suppression caracteres accentues".upper())
win.geometry("800x800")
Lsize = 0
cpt_lu = 0
cpt_tr = 0
home_folder = os.path.expanduser('~')
homedrive = home_folder
rep_source = home_folder
selection=""
r_record = []

# Selection fichier
def openfile(evt): 
#    pass
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
#    print('You selected item %d: "%s"' % (index, value))
    selection = value
    v_sel.set(selection)

def ask_question(rep_source):
#    global rep_source
    lb.delete(0, tk.END)
    win.update()
    rep_source = tk.filedialog.askdirectory(
    parent=win, initialdir=homedrive, title="Selectionnez le dossier SOURCE")
    try:
        os.listdir(rep_source)
    except Exception as e:
        tk.messagebox.showinfo('Return', 'Traitement annulé', parent=win)
    read_files(rep_source)
    
def read_files(rep_source):
#    global rep_source
    r_record.clear()
    cpt_lu = 0
    cpt_tr = 0

    for file in os.listdir(rep_source):
        fileDec = unidecode.unidecode(file)
        cpt_lu = cpt_lu+1
        v_cpt.set(str(cpt_lu)+"/"+str(cpt_tr))
#        la1.config(text=str(cpt_lu)+"/"+str(cpt_tr))

        filePath = Path(rep_source)
        newFile = filePath / fileDec
        oldFile = filePath / file
        if os.path.isfile(oldFile) is True : 
            v_type = 'F'
        if os.path.isdir(oldFile) is True :
            v_type = 'D'
        if os.path.isfile(newFile) is True : 
            v_exist = 'Y'
        if os.path.isdir(newFile) is True :
            v_exist = 'Y'    
        r_record.append([file,fileDec,oldFile,newFile,v_type,v_exist])
        
    for [file,fileDec,oldFile,newFile,v_type,v_exist] in r_record :  
        # print(file, oldFile)    
        lb.insert(0, "  " + file + "  "+"\t" + v_type+"\t" + v_exist)
        if file != fileDec:
            lb.insert(1, "  "+"\t" + fileDec + "  "+"\t" + v_type+"\t" + v_exist)  
        
    win.update()
    Lsize = lb.size()
    if Lsize != 0:
        do_job(rep_source)

def do_job(rep_source):
    msg_box = tk.messagebox.askquestion('Return', 'Validation des modifications ?',
                                        icon='warning', parent=win)
    if msg_box == 'yes':
#       pass
        rename_files(rep_source)
        tk.messagebox.showinfo('Return', 'Traitement terminé', parent=win)
    else:
        tk.messagebox.showinfo(
            'Return', 'Modifications non effectuées', parent=win)

def rename_files(rep_source):
#    global rep_source
    cpt_lu = 0
    cpt_tr = 0    

    for [file,fileDec,oldFile,newFile,v_type,v_exist] in r_record :  
        # print(file, oldFile)    
        cpt_lu = cpt_lu+1
        if newFile != oldFile:
            pass
            # filePath = Path(rep_source)
            # newFile = filePath / fileDec
            # oldFile = filePath / file
            if not ( v_type == "D" and v_exist == "Y" ) :
                try:
                    os.rename(oldFile, newFile)  
                    cpt_tr = cpt_tr+1
                except Exception as e:
                    print(str(e))
                    tk.messagebox.showinfo('Return', str(e), parent=win)

    v_cpt.set(str(cpt_lu)+"/"+str(cpt_tr))
#   la1.config(text=str(cpt_lu)+"/"+str(cpt_tr))

v_cpt = tk.StringVar(win, value=str(cpt_lu)+"/"+str(cpt_tr))
v_sel = tk.StringVar(win, value=selection)
action_with_arg = partial(ask_question, rep_source)
bt1 = tk.Button(win, text="Open a File", command= action_with_arg)
bt1.pack()
lb = tk.Listbox(win)
lb.pack(expand=tk.YES, fill=tk.BOTH)
lb.bind("<<ListboxSelect>>",openfile)
# Utilisation de variable
#la1 = tk.Label(win,text=str(cpt_lu)+"/"+str(cpt_tr))
#la1.pack()
# Utilisation de tk.StringVar
la2 = tk.Label(win, textvariable=v_cpt)
la2.pack()
# Affichage de selection
la3 = tk.Label(win, textvariable=v_sel)
la3.pack()

win.mainloop()
