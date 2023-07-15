from tkinter import *
import os
programs = {
    'Main': [
        ('Notepad', 'C:/Windows/notepad.exe'),
        ('Explorer', 'C:/Windows/explorer.exe'),
        ('Taskmgr', 'C:/Windows/System32/taskmgr.exe'),
        ('Paint', 'C:/Windows/System32/mspaint.exe'),
        ('Calc', 'C:/Windows/System32/calc.exe'),
        ('Char map', 'C:/Windows/System32/charmap.exe'),
    ],
    'Advanced': [
        ('Cmd', 'C:/Windows/System32/cmd.exe')
    ]
}
def make_command(index, data):
    def command():
        run(data[index][1])
    return command

def make_command1(folder):
    def command():
        openfolder(folder)
    return command

def run(prog):
    print(prog)
    os.startfile(prog)
def logout():
    print('Logging out...')
    root.destroy()
def openfolder(folder):
    print('Opened folder!', folder)
    top = Toplevel()
    top.geometry(f"300x200+{root.winfo_x()+50}+{root.winfo_y()+50}")
    top.title(folder)
    rendericons(programs[folder], top)

root = Tk()
menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Exit", command=logout)
menubar.add_cascade(label="File", menu=menu1)

root.geometry('400x300')

def rendericons(opened, window):
    y = 0
    x = 0
    for i,l in enumerate(opened):
        p = Button(window, text=l[0], command=make_command(i, opened),width=7,height=2)
        p.grid(column=x,row=y)
        if x > 3:
            x = -1
            y += 1
        x += 1

def renderfolders(window, folders):
    for i,folder in enumerate(folders):
        p = Button(window, text=folder, command=make_command1(folder),width=7,height=2)
        p.grid(column=i,row=1)
openfolder('Main')
renderfolders(root, programs)
root.config(menu=menubar)
root.mainloop()

