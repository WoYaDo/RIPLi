from Tkinter import *  
import tkFileDialog as filedialog
import PIL
from PIL import Image
from PIL import ImageTk
import glob
import os

root = Tk()
def setKey(key,callback):
    if key == 'left':
        root.bind("<Left>",callback)
    elif key == 'right':
        root.bind("<Right>",callback)
    elif key =='return':
        root.bind("<Return>",callback)
    elif key =="back":
        root.bind("<Escape>",callback)

def donothing():
   return 0

currentmode = 'root'
rootindex = 1
editindex = 1

def leftkey(event):
    global currentmode,rootindex,editindex,fileindex
    print "pressed left"
    if currentmode == 'root':
        menubar.entryconfig(rootindex,background="lightgrey")
        rootindex = rootindex - 1
        rootindex = max(1,rootindex)
        menubar.entryconfig(rootindex,background="red")
    elif currentmode == 'edit':
        editmenubar.entryconfig(editindex,background="lightgrey")
        editindex = editindex - 1
        rootindex = max(1,editindex)
        editmenubar.entryconfig(editindex,background="red")
    else:
        print currentmode


def rightkey(event):
    global currentmode,rootindex,editindex,fileindex
    print "pressed right"
    if currentmode == 'root':
        menubar.entryconfig(rootindex,background="lightgrey")
        rootindex = rootindex + 1
        rootindex = min(4,rootindex)
        menubar.entryconfig(rootindex,background="red")
    elif currentmode == 'edit':
        editmenubar.entryconfig(editindex,background="lightgrey")
        editindex = editindex + 1
        rootindex = min(4,editindex)
        editmenubar.entryconfig(editindex,background="red")
    else:
        print currentmode

def enterKey(event):
    print "pressed enter"
    if currentmode == 'root':
        menubar.invoke(rootindex)
    elif currentmode == 'edit':
        editmenubar.entryconfig(editindex,background="green")
        editmenubar.invoke(editindex)
    else:
        print currentmode
   
######################root#####################

imageframe = Frame(root,height=200,width=300)
editmenubar = Menu(root)
editmenubar.add_command(label="Rotate")
editmenubar.add_command(label="Scale")
editmenubar.add_command(label="Choose Image")
editmenubar.add_command(label="Close")

def enterEditMode():
    if (not imageframe.winfo_children()):
        return;
    global currentmode
    editindex = 1
    currentmode = 'edit'
    #editmenubar = Menu(root)

    editmenubar.entryconfig(1, command=rotate)
    editmenubar.entryconfig(2, command=scale)
    editmenubar.entryconfig(3, command=chooseimage)
    editmenubar.entryconfig(4, command=closeedit)

    editmenubar.entryconfig(1,background="red")

    root.config(menu=editmenubar)


def openImage(filedialog,filename):
    filedialog.destroy()
    img = Image.open(filename)
    phimg = ImageTk.PhotoImage(img)
    phimg.current = img
    phimg.original = img
    phimg.rotation = 0
    panel = Label(imageframe, image = phimg)
    panel.filename = filename
    panel.image = phimg
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    setKey("left",leftkey)
    setKey("right",rightkey)
    setKey("return",enterKey)


def openfilemenu():
    for widget in imageframe.winfo_children():
        widget.destroy()


    fileindex = [0]
    filedialog = Toplevel(root)

    size = 128, 128
    COLUMNS = 10
    image_count = 0

    filenames = glob.glob(os.path.join(os.getcwd(), '*.gif'))
    labels = []

    def left(event):
        labels[fileindex[0]].config(highlightbackground="red",highlightthickness=0)
        fileindex[0] = max(0,fileindex[0] - 1)
        labels[fileindex[0]].config(highlightbackground="red",highlightthickness=5)

    def right(event):
        labels[fileindex[0]].config(highlightbackground="red",highlightthickness=0)
        fileindex[0] = min(len(filenames),fileindex[0] + 1)
        labels[fileindex[0]].config(highlightbackground="red",highlightthickness=5)
        pass

    setKey('left',left)
    setKey('right',right)
    setKey('return',lambda e: openImage(filedialog,filenames[fileindex[0]]))

    for infile in filenames:

        image_count += 1
        r, c = divmod(image_count - 1, COLUMNS)
        img = Image.open(infile)
        img.thumbnail(size)
        phimg = ImageTk.PhotoImage(img)

        label = Label(filedialog,image = phimg)
        label.image = phimg


        label.grid(row=r, column=c)

        labels.append(label)

    labels[fileindex[0]].config(highlightbackground="red",highlightthickness=5)







def save():
    if (not imageframe.winfo_children()):
        return;
    label = imageframe.winfo_children()[0]
    label.image.current.save(label.filename)
    menubar.entryconfig(3,background="green")

def quit():
    root.destroy()

menubar = Menu(root)
menubar.add_command(label="Edit", command=enterEditMode)
menubar.add_command(label="Open", command=openfilemenu)
menubar.add_command(label="Save", command=save)
menubar.add_command(label="Close", command=quit)
menubar.entryconfig(1,background="red")

root.config(menu=menubar)
imageframe.pack()

###############################################

######################edit#####################

def rotate_left(event):
    label = imageframe.winfo_children()[0]
    rotation = label.image.rotation
    newrotation = rotation + 5
    newrotation %= 360
    newimage = label.image.original.rotate(newrotation,expand=True)
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    #newphimage.original = newimage
    newphimage.original = label.image.original
    newphimage.rotation = newrotation
    label.configure(image=newphimage)
    label.image=newphimage


def rotate_right(event):
    label = imageframe.winfo_children()[0]
    rotation = label.image.rotation
    newrotation = rotation - 5
    newrotation %= -360
    newimage = label.image.original.rotate(newrotation,expand=True)
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    #newphimage.original = newimage
    newphimage.original = label.image.original
    newphimage.rotation = newrotation
    label.configure(image=newphimage)
    label.image=newphimage

def back(event):
    label = imageframe.winfo_children()[0]
    label.image.original = label.image.current
    label.image.rotation = 0
    setKey("left",leftkey)
    setKey("right",rightkey)
    editmenubar.entryconfig(editindex,background="red")

def rotate():
    
    setKey("left", rotate_left)
    setKey("right",rotate_right)
    setKey("back",back)


def scale_left(event):
    label = imageframe.winfo_children()[0]
    newwidth = label.image.width() - 5
    newheight = label.image.height() - 5
    newimage = label.image.original.resize((newwidth,newheight),resample=PIL.Image.LANCZOS)
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    newphimage.rotation = label.image.rotation
    label.configure(image=newphimage)
    label.image=newphimage

def scale_right(event):
    label = imageframe.winfo_children()[0]
    newwidth = label.image.width() + 5
    newheight = label.image.height() + 5
    newimage = label.image.original.resize((newwidth,newheight),resample=PIL.Image.LANCZOS)
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    newphimage.rotation = label.image.rotation
    label.configure(image=newphimage)
    label.image=newphimage

def scale():
    setKey("left", scale_left)
    setKey("right",scale_right)
    setKey("back",back)

def chooseimage():
    return 0
def closeedit():
    global currentmode,editindex,rootindex
    currentmode = 'root'
    rootindex = 1
    editmenubar.entryconfig(editindex,background="lightgrey")
    editindex = 1
    root.config(menu=menubar)



###############################################


setKey("left",leftkey)
setKey("right",rightkey)
setKey("return",enterKey)
root.mainloop()
