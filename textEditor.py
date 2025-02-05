from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

# References: Make With Data (2011) https://www.youtube.com/watch?v=xqDonHEYPgA

filename = None # Initialize filename

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END) # 0th Row and 0th Column respectively; from (0,0) to END 

def saveFile():
    global filename
    t = text.get(0.0, END) # Retrieves text from start to END
    f = open(filename, 'w') # Opens the file with the corresponding filename 
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip()) # Removes whitespace below the end of text
    except:
        showerror(title="Error", message="Unable to save file.")

def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("Basic Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack() # Display textbox

# Menubar
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()