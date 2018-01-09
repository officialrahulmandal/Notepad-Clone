from tkinter import *

notepad_window = Tk()
notepad_window.title("Notepad clone")
notepad_window.geometry("400x400")


def about():
    about_window = Tk()
    about_window.geometry("300x100")
    about_window.title("About Notepad Clone")
    about_label = Label(about_window, text="Software name :- Notepad clone")
    about_label.grid(row=0, column=0)
    about_label = Label(about_window, text="Made By :- Rahul kumar mandal")
    about_label.grid(row=1, column=0)
    about_label = Label(about_window, text="Email id :- officialrahulmandal@gmail.com")
    about_label.grid(row=2, column=0)
    about_window.mainloop()


def savefile():
    print(inputtext.get("1.0", END))
    with open("output.txt", 'w') as f:
        f.write(inputtext.get("1.0", END))


mymenu = Menu(notepad_window)
notepad_window.config(menu=mymenu)
submenu1 = Menu(mymenu, tearoff=FALSE)
mymenu.add_cascade(label="File", menu=submenu1)

submenu1.add_command(label="New")
submenu1.add_command(label="Open")
submenu1.add_command(label='Save', command=savefile)
submenu1.add_command(label='Save As')
submenu1.add_separator()
submenu1.add_command(label='Page Setup')
submenu1.add_command(label='Print')
submenu1.add_separator()
submenu1.add_command(label="Exit", command=notepad_window.quit)

submenu2 = Menu(mymenu, tearoff=FALSE)
mymenu.add_cascade(label="Edit", menu=submenu2)
submenu2.add_command(label="Undo")
submenu2.add_separator()
submenu2.add_command(label="cut")
submenu2.add_command(label="copy")
submenu2.add_command(label="Paste")
submenu2.add_command(label="Delete")
submenu2.add_separator()
submenu2.add_command(label="find")
submenu2.add_command(label="find next")
submenu2.add_command(label="Replace")
submenu2.add_command(label="Go to..")
submenu2.add_separator()
submenu2.add_command(label="select all")
submenu2.add_command(label="Time/Date")

submenu3 = Menu(mymenu, tearoff=FALSE)
mymenu.add_cascade(label="Format", menu=submenu3)
submenu3.add_command(label="Wordwrap")
submenu3.add_command(label="Font")

submenu4 = Menu(mymenu, tearoff=FALSE)
mymenu.add_cascade(label="View", menu=submenu4)
submenu4.add_command(label="Statusbar")

submenu5 = Menu(mymenu, tearoff=FALSE)
mymenu.add_cascade(label="Help", menu=submenu5)
submenu5.add_command(label="View help")
submenu5.add_separator()
submenu5.add_command(label="About Notepad Clone", command=about)

inputtext = Text(notepad_window, width=200, height=200)
inputtext.grid()
notepad_window.mainloop()
