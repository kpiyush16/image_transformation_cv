# image_transformation_cv
Transformation GUI based on tkinter with the help of OpenCV and PIL.
# Image transformation to a continuous seamless image

Requirements: OpenCV, PIL, tkinter, Python 3.xx and LINUX based Kernel 
FileName: Assign2.tar.gz

# Instructions
-> To run the program, open terminal in the respective image's folder to run "Transformer.py".

-> Open the image in that folder you want to perform Transformation on.

-> On the GUI, select(click) 4 corner points in general approach one after another to segment out the image.

-> As per Parallel Processing, on the terminal, image co-ordinates selected can be seen.

-> After 4 points, Homography Matrix will be shown in the terminal itself for that image to transform it into scaled rectangular frame.

-> Repeat the same steps of selecting(clicking) for middle image and then for the last image (left to right fashion) on the same GUI.

-> After the 3rd Homography Matrix is shown on the terminal, resultant image named "joinedImage.jpg" will be created which is seamless painting of the three images selected through points.
