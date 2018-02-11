import tkinter as tk
from tkinter import filedialog
import sys
from PIL import ImageTk, Image
import cv2
import matplotlib as plt
import numpy as np
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

#This creates the main window of an application
window = tk.Tk()
window.title("Image_GUI")
window.geometry("1366x768")
window.configure(background='grey')

path =  filedialog.askopenfilename(initialdir = dir_path,title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (path)

menubar = tk.Menu(window)
window.config(menu = menubar)

filemenu = tk.Menu(menubar)
#Create a menu button labeled "File" that brings up a menu
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Quit', command=sys.exit)

# path = "ThreePanel4.jpg"
resized = Image.open(path).resize((1366, 768), Image.ANTIALIAS)
resized.save("resize.jpg")
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(resized)

imagecv = cv2.imread("resize.jpg")

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

def joinImage(v):
	y_res = int((v[0][1]+v[1][1]+v[2][1])/len(v))

	joined = Image.new("RGB", ((v[0][0]+v[1][0]+v[2][0]), y_res))
	cc = 0
	for i in range(3):
		img=Image.open("part_image0%d.jpg" %(i+1)).resize((v[i][0],y_res), Image.ANTIALIAS)
		joined.paste(img, (cc, 0, int(cc+v[i][0]), y_res))
		cc += v[i][0]

	joined.save('joinedImage.jpg')


clickv, clicks, pixel_vector = [], [], []
count = -1
def click(event):
	print ("You clicked at pixel: (%s, %s)" %(str(event.x), str(event.y)))
	clickv = [int(event.x), int(event.y)]
	clicks.append(clickv)

	if(len(clicks) % 4 == 0):
		global count
		count +=1
		print("The image %d is being processed.." %(count))

		if(count > 0):
			index = count*4
		else:
			index = 0

		pixels = clicks[index:index+4]
		
		a = int(1.3*(pixels[1][0] - pixels[0][0]))
		
		if(count == 1):
			a = int(a/(1.3))

		b = (pixels[2][1] - pixels[0][1])
		pixel_vector.append([a,b])

		print("This image will be fitted in %dx%d dimensions" %(a, b))
		
		pts1 = np.float32(pixels)
		pts2 = np.float32([[0,0],[a,0],[0,b],[a,b]])

		homography = cv2.getPerspectiveTransform(pts1,pts2)
		print("Homography matrix for this image is: \n", homography)

		dst = cv2.warpPerspective(imagecv,homography,(a,b))
		cv2.imwrite("part_image0%d.jpg" %(count+1), dst)
		
		if(len(clicks) == 12):
			global joinImage
			joinImage(pixel_vector)


#The Pack geometry manager packs widgets in rows or columns.
panel.bind("<Button-1>", click)

panel.pack(side = "bottom", fill = "both", expand = "yes")


#Start the GUI
window.mainloop()