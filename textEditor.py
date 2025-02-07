from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

# References: Make With Data (2011) https://www.youtube.com/watch?v=xqDonHEYPgA

filename = None # Initialize filename

def newFile():
    global filename
    filename = None
    text.delete(0.0, END) # 0th Row and 0th Column respectively; from (0,0) to END 

def saveFile():
    global filename
    if filename is None:
        saveAs()
    else:
        try:
            with open(filename, 'w') as f:
                f.write(text.get(0.0, END))
        except:
            showerror(title="Error", message="Unable to save file.")

def saveAs():
    global filename
    f = asksaveasfile(mode='w', defaultextension='.txt')
    if f is None:
        return
    filename = f.name
    try:
        f.write(text.get(0.0, END).rstrip())
        f.close()
    except:
        showerror(title="Error", message="Unable to save file.")

def openFile():
    global filename
    f = askopenfile(mode='r')
    if f is None:
        return
    filename = f.name
    text.delete(0.0, END)
    text.insert(0.0, f.read())

def update_cursor_position(event=None):
    row, col = text.index(INSERT).split('.')
    status_bar.config(text=f"Line: {row} | Column: {int(col) + 1}")

# Applicaton
root = Tk()
root.title("Basic Python Text Editor")
root.geometry("600x400")

# Widget & Scrollbar frame
frame = Frame(root)
frame.pack(fill=BOTH, expand=TRUE)

# Text Widget
text = Text(frame, wrap=NONE, undo=TRUE)
text.pack(side=LEFT, fill=BOTH, expand=TRUE)

# Scrollbar (Vertical)
scrollbar = Scrollbar(frame, command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scrollbar.set)

# Scrollbar (Horizontal)
scrollbar_x = Scrollbar(root, command=text.xview, orient=HORIZONTAL)
scrollbar_x.pack(side=BOTTOM, fill=X)
text.config(xscrollcommand=scrollbar_x.set)

# Statusbar
status_bar = Label(root, text="Line: 1 | Column: 1", anchor = 'w')
status_bar.pack(fill=X, side=BOTTOM)

# Menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
text.bind("<KeyRelease>", update_cursor_position)
text.bind("<ButtonRelease>", update_cursor_position)

root.mainloop()