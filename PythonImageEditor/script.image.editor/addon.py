from Tkinter import *
import tkFileDialog as filedialog
import PIL
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
from functools import partial
import glob
import os
import threading

import xbmc,xbmcgui

from GestureController import getFirstEvent

"""
Initializes th GUI
"""
root = Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
"""
Global callback that will be excuted when a gesture is detected
"""
leftCallback = lambda e: 0
rightCallback = lambda e: 0
returnCallback = lambda e: 0
escapeCallback = lambda e: 0
active = True

"""
Executes correct global callback depending on gesture
(event loop)
"""
def executeCommand():
    print "starting execute command"
    if active:
        commandString = getFirstEvent()
        print commandString
        if commandString == 'WaveIn' or commandString == "SwipeLeft":
            leftCallback(None)
        elif commandString == 'WaveOut' or commandString == "SwipeRight":
            rightCallback(None)
        elif commandString == 'DoubleTap' or commandString == "WaveRight":
            returnCallback(None)
        elif commandString == 'FingersSpread' or commandString == "WaveLeft":
            escapeCallback(None)
        root.after(100,executeCommand)

"""
Sets a global callback to a correct 'local' callback
This depends on the current mode
"""
def setKey(key,callback):
    global leftCallback,rightCallback,returnCallback,escapeCallback
    if key == 'left':
        #root.bind("<Left>",callback)
        leftCallback = callback
    elif key == 'right':
        #root.bind("<Right>",callback)
        rightCallback = callback
    elif key =='return':
        #root.bind("<Return>",callback)
        returnCallback = callback
    elif key =="back":
        #root.bind("<Escape>",callback)
        escapeCallback = callback

"""
The current mode and their indexes are stored to show the menu buttons correctly
"""
currentmode = 'root'
rootindex = 0
editindex = 0


"""
The 'local' left callback for the root and the top-level edit mode
"""
def leftkey(event):
    global currentmode,rootindex,editindex,fileindex
    print "pressed left"
    if currentmode == 'root':
        menubar.entryconfig(rootindex,background="lightgrey")
        rootindex = rootindex - 1
        rootindex = max(0,rootindex)
        menubar.entryconfig(rootindex,background="red")
    elif currentmode == 'edit':
        editmenubar.entryconfig(editindex,background="lightgrey")
        editindex = editindex - 1
        rootindex = max(0,editindex)
        editmenubar.entryconfig(editindex,background="red")
    else:
        print currentmode

"""
The 'local' right callback for the root and the top-level edit mode
"""
def rightkey(event):
    global currentmode,rootindex,editindex,fileindex
    print "pressed right"
    if currentmode == 'root':
        menubar.entryconfig(rootindex,background="lightgrey")
        rootindex = rootindex + 1
        rootindex = min(3,rootindex)
        menubar.entryconfig(rootindex,background="red")
    elif currentmode == 'edit':
        editmenubar.entryconfig(editindex,background="lightgrey")
        editindex = editindex + 1
        editindex = min(5,editindex)
        editmenubar.entryconfig(editindex,background="red")
    else:
        print currentmode

"""
The 'local' enter callback for the root and the top-level edit mode
"""
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
"""
Custom menu class (implemented as button), because Windows does not support editing of their native menus
All mehthods that are provided by the Tkinter Menu class (and are used in the application) are reimplemented
"""
class MyMenu:
    def __init__(self,root):
        self.root = root
        self.entries = []
        self.buttonframe = Frame(self.root)
        self.buttonframe.grid(row=2, column=0, columnspan=2)
        
    def add_command(self,label = False,command = False):
        button = Button(self.buttonframe,text = label,command = command)
        button.grid(row=0,column = len(self.entries))
        #button.pack()
        self.entries.append(button)
    def entryconfig(self,idx,**kwargs):
        button = self.entries[idx]
        button.config(kwargs)

    def invoke(self,idx):
        self.entries[idx].invoke()

    def hide(self):
        self.buttonframe.pack_forget()
    def show(self):
        self.buttonframe.pack()
    
"""
Initialize and allocated a frame to show the image
"""
imageframe = Frame(root,height=200,width=300)


"""
Initializes the edit menu bar
"""
editmenubar = MyMenu(root)
editmenubar.add_command(label="Rotate")
editmenubar.add_command(label="Scale")
editmenubar.add_command(label="Brightness")
editmenubar.add_command(label="Contrast")
editmenubar.add_command(label="Filter")
editmenubar.add_command(label="Close")

editmenubar.show()
editmenubar.hide() #small hack to allocate the space in the window


"""
Method called when the 'edit' button is pushed
This method hides the root menu, show the edit menu and initialzes the button functions
"""
def enterEditMode():
    if (not imageframe.winfo_children()): #return if no image is selected
        return;
    global currentmode

    editmenubar.show()
    menubar.hide()
    
    editindex = 0
    currentmode = 'edit'
    #editmenubar = Menu(root)

    
    editmenubar.entryconfig(0, command=rotate)
    editmenubar.entryconfig(1, command=scale)
    editmenubar.entryconfig(2, command=brightness)
    editmenubar.entryconfig(3, command=contrast)
    editmenubar.entryconfig(4, command=ifilter)
    editmenubar.entryconfig(5, command=closeedit)

    editmenubar.entryconfig(0,background="red")

    

""""
Opens an image given a certain filename.
It fills the image frame and removes the file explorer (filedialog)

It initializes the image with an original image which is itself
"""
def openImage(filedialog,filename):
    filedialog.destroy()
    img = Image.open(filename)
    phimg = ImageTk.PhotoImage(img)
    phimg.current = img
    phimg.original = img
    panel = Label(imageframe, image = phimg)
    panel.filename = filename
    panel.image = phimg
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    #reset the key callbacks
    setKey("left",leftkey)
    setKey("right",rightkey)
    setKey("return",enterKey)

"""
Opens an image given a certain filename. Function is called without filedialog.
This function is called if main has parameter
"""
def openImageStandAlone(filename):
    img = Image.open(filename)
    phimg = ImageTk.PhotoImage(img)
    phimg.current = img
    phimg.original = img
    panel = Label(imageframe, image = phimg)
    panel.filename = filename
    panel.image = phimg
    panel.pack(side = "bottom", fill = "both", expand = "yes")

"""
Opens the file explorer to select an image to edit.
If a previous image was selected, it will be removed
"""
def openfilemenu():
    for widget in imageframe.winfo_children():
        widget.destroy()


    fileindex = [0]
    filedialog = Toplevel(root)

    size = 128, 128
    COLUMNS = 10
    image_count = 0

    filenames = glob.glob(os.path.join(os.getcwd(), '*[.jpg ][.jpeg][.png][.gif]'))
    labels = []

    #active state draws a rectangle around the selected image
    def left(event):
        labels[fileindex[0]].config(state="normal")
        fileindex[0] = max(0,fileindex[0] - 1)
        labels[fileindex[0]].config(state="active")

    def right(event):
        labels[fileindex[0]].config(state="normal")
        fileindex[0] = min(len(filenames)-1,fileindex[0] + 1)
        labels[fileindex[0]].config(state="active")
        pass

    #set the correct key callbacks
    setKey('left',left)
    setKey('right',right)
    setKey('return',lambda e: openImage(filedialog,filenames[fileindex[0]]))

    for infile in filenames:

        image_count += 1
        r, c = divmod(image_count - 1, COLUMNS)
        img = Image.open(infile)
        img.thumbnail(size)
        phimg = ImageTk.PhotoImage(img)

        label = Label(filedialog,image = phimg,borderwidth=5,activebackground="red")
        label.image = phimg


        label.grid(row=r, column=c)

        labels.append(label)

    #select the first image
    labels[fileindex[0]].config(state="active")

"""
Saves the current edit to the image with the original filename.
"""
def save():
    if (not imageframe.winfo_children()):
        return;
    label = imageframe.winfo_children()[0]
    label.image.current.save(label.filename)
    menubar.entryconfig(2,background="green")

"""
Quits the program and stops the event loop (executeCommand)
"""
def myquit():
    global active
    active =False
    #quitController()
    root.destroy()

    
"""
Initializes the main menu bar. Defined here because it requires the definition of all button methods 
"""
menubar = MyMenu(root)
menubar.add_command(label="Edit", command=enterEditMode)
menubar.add_command(label="Open", command=openfilemenu)
menubar.add_command(label="Save", command=save)
menubar.add_command(label="Close", command=myquit)
menubar.entryconfig(0,background="red")
menubar.show()
imageframe.pack()

###############################################

######################edit#####################
"""
Rotate the current selected image. It creates a new image but retains the original image to prevent the quality to drop significantly
ly. It increases or deceases the rotation counter of the image so we can reuse the original image for the next rotation.
"""
def rotate_left(event):
    label = imageframe.winfo_children()[0]
    rotation = label.rotation
    newrotation = rotation + 5
    newrotation %= 360
    newimage = label.image.original.rotate(newrotation,expand=True)
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    label.rotation = newrotation
    label.configure(image=newphimage)
    label.image=newphimage


def rotate_right(event):
    label = imageframe.winfo_children()[0]
    rotation = label.rotation
    newrotation = rotation - 5
    newrotation %= -360
    newimage = label.image.original.rotate(newrotation,expand=True)
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    label.rotation = newrotation
    label.configure(image=newphimage)
    label.image=newphimage

def back(event):
    label = imageframe.winfo_children()[0]
    label.image.original = label.image.current
    label.rotation = 0
    setKey("left",leftkey)
    setKey("right",rightkey)
    editmenubar.entryconfig(editindex,background="red")

"""
Is called when the rotate option in the edit menu is selected.
It intializes the current rotation to 0.
The rotation is reset each time the rotate option is selected
"""
def rotate():
    label = imageframe.winfo_children()[0]
    label.rotation = 0
    setKey("left", rotate_left)
    setKey("right",rotate_right)
    setKey("back",back)

#######################################################
"""
Scales the current selected image. It creates a new image but retains the original image to prevent the quality to drop significantly
ly. The scale factor is not stored because it can be calculated from the image dimensions. 
"""
def scale_left(event):
    label = imageframe.winfo_children()[0]
    newwidth = label.image.width() - 5
    newheight = label.image.height() - 5
    newimage = label.image.original.resize((newwidth,newheight),resample=PIL.Image.LANCZOS)
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
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
    label.configure(image=newphimage)
    label.image=newphimage

"""
Is called when the rotate option in the scale menu is selected.
"""
def scale():
    setKey("left", scale_left)
    setKey("right",scale_right)
    setKey("back",back)

###############################################
"""
Change the brightness of the current selected image. It creates a new image but retains the original image to prevent the quality to drop significantly
ly. It increases or decreases the brightness of the image so we can reuse the original image for the next rotation.
"""
def brightness_left(event):
    label = imageframe.winfo_children()[0]
    oldbrightness = label.brightness
    newbrightness = oldbrightness - 0.1
    enhancer = ImageEnhance.Brightness(label.image.original)
    bright_im = enhancer.enhance(newbrightness) #any value you want
    newimage = bright_im
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    newphimage.rotation = label.image.rotation
    label.configure(image=newphimage)
    label.image=newphimage
    label.brightness = newbrightness

def brightness_right(event):
    label = imageframe.winfo_children()[0]
    oldbrightness = label.brightness
    newbrightness = oldbrightness + 0.1
    enhancer = ImageEnhance.Brightness(label.image.original)
    bright_im = enhancer.enhance(newbrightness) #any value you want
    newimage = bright_im
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    newphimage.rotation = label.image.rotation
    label.configure(image=newphimage)
    label.image=newphimage
    label.brightness = newbrightness

"""
Is called when the rotate option in the edit menu is selected.
It intializes the current brightness to 1.
The rotation is reset each time the rotate option is selected
"""
def brightness():
    label = imageframe.winfo_children()[0]
    label.brightness = 1.0
    setKey("left", brightness_left)
    setKey("right",brightness_right)
    setKey("back",back)

###############################################
"""
Change the contrast of the current selected image. It creates a new image but retains the original image to prevent the quality to drop significantly
ly. It increases or decreases the constrast of the image so we can reuse the original image for the next rotation.
"""
def contrast_left(event):
    label = imageframe.winfo_children()[0]
    oldcontrast = label.contrast
    newcontrast = oldcontrast - 0.1
    enhancer = ImageEnhance.Contrast(label.image.original)
    bright_im = enhancer.enhance(newcontrast) #any value you want
    newimage = bright_im
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    newphimage.rotation = label.image.rotation
    label.configure(image=newphimage)
    label.image=newphimage
    label.contrast = newcontrast

def contrast_right(event):
    label = imageframe.winfo_children()[0]
    oldcontrast = label.contrast
    newcontrast = oldcontrast + 0.1
    enhancer = ImageEnhance.Contrast(label.image.original)
    bright_im = enhancer.enhance(newcontrast) #any value you want
    newimage = bright_im
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    newphimage.rotation = label.image.rotation
    label.configure(image=newphimage)
    label.image=newphimage
    label.contrast = newcontrast

"""
Is called when the contrast option in the edit menu is selected.
It intializes the current contrast to 1.
The contrast is reset each time the rotate option is selected
"""
def contrast():
    label = imageframe.winfo_children()[0]
    label.contrast = 1.0
    setKey("left", contrast_left)
    setKey("right",contrast_right)
    setKey("back",back)

###############################################
"""
Black and white filter
"""
def filter1(image):
    im = image.convert("L")
    return im

"""
Sepia filter
"""
def filter2(image):
    def make_linear_ramp(white):
        ramp = []
        r, g, b = white
        for i in range(255):
            ramp.extend((r*i/255, g*i/255, b*i/255))
        return ramp

    sepia = make_linear_ramp((255, 240, 192))
    im = image.convert("L")
    im.putpalette(sepia)
    return im

"""
Orignal image filter
"""
def filter0(image):
    return image

"""
List of filter functions
"""
filters = [filter0,filter1,filter2] 

"""
Loop over filters and apply it immedialty
"""
def filter_right(event):
    label = imageframe.winfo_children()[0]
    curfilter = label.filter
    newfilter = min(curfilter + 1,len(filters) - 1)
    label = imageframe.winfo_children()[0]

    origimage = label.image.original
    filterfunction = filters[newfilter]
    newimage = filterfunction(origimage)
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    newphimage.rotation = label.image.rotation
    label.configure(image=newphimage)
    label.image=newphimage
    label.filter = newfilter
    
def filter_left(event):
    label = imageframe.winfo_children()[0]
    curfilter = label.filter
    newfilter = max(0,curfilter - 1)
    label = imageframe.winfo_children()[0]

    origimage = label.image.original
    filterfunction = filters[newfilter]
    newimage = filterfunction(origimage)
    newphimage = ImageTk.PhotoImage(newimage)
    newphimage.current = newimage
    newphimage.original = label.image.original
    newphimage.rotation = label.image.rotation
    label.configure(image=newphimage)
    label.image=newphimage
    label.filter = newfilter

"""
Called when the filter option button is pushed.
Named ifilter because filter already exists
"""
def ifilter():
    label = imageframe.winfo_children()[0]
    label.filter = 0
    setKey("left", filter_left)
    setKey("right",filter_right)
    setKey("back",back)
################################################
def chooseimage():
    return 0
def closeedit():
    global currentmode,editindex,rootindex
    currentmode = 'root'
    rootindex = 0
    editmenubar.entryconfig(editindex,background="lightgrey")
    editindex = 0

    editmenubar.hide()
    menubar.show()



###############################################


setKey("left",leftkey)
setKey("right",rightkey)
setKey("return",enterKey)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        root.after(0,openImageStandAlone,sys.argv[1])
     #   root.mainloop()
    else:
     #   root.mainloop()
     pass

while True:
     commandString = getFirstEvent()
     if commandString == "Fist":
         root.after(100,executeCommand)
         root.mainloop()
         dialog = xbmcgui.Dialog()
         dialog.ok("Attention","Please make a fist and enter to close this message")
         break 
     else:
        pass
