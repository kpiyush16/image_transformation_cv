import tkinter as tk
from tkinter import filedialog
import sys
from PIL import ImageTk, Image
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__))

#This creates the main window of an application
window = tk.Tk()
window.title("ImageTransformation")
window.geometry("1200x720")
window.configure(background='grey')

path =  "ThreePanel4.jpg"

menubar = tk.Menu(window)
window.config(menu = menubar)

filemenu = tk.Menu(menubar)
#Create a menu button labeled "File" that brings up a menu
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Quit', command=sys.exit)

# path = "ThreePanel4.jpg"
resized = Image.open(path).resize((1200, 720), Image.ANTIALIAS)
resized.save("resize.jpg")
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(resized)

imagecv = cv2.imread("resize.jpg")

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.bind("<Button-1>", click)

panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()