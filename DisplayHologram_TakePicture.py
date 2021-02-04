"""
Starter program to display an image on the SLM and take a picture 
with the webcam. by changing the img_name different images can be 
displayed on the webcam.

@author: SJohnson Jan 2021 UofGlasow
"""

import tkinter as tk
from PIL import Image, ImageTk
import cv2
import time

# %% Load a picture to display
img_name = "example_grating.png"
img = Image.open(img_name)


# %% Make a window and draw picture
screen_size_X = 768
screen_size_Y = 1024
root = tk.Tk() # Create at TK window
root.geometry("768x1024+1270+0") # SLM screen size: WVGA (1024x768)
canvas = tk.Canvas(root, width=screen_size_X, height=screen_size_Y)
canvas.pack()

img = img.resize( (screen_size_X, screen_size_Y) ) # Resize the image to fit
img = ImageTk.PhotoImage(img) 
canvas.create_image(0, 0, anchor="nw", image=img)

root.update() # Show plot in TK window

# %% Take an image with the webcam
cam = cv2.VideoCapture(1)
while(True): 

    ret, frame = cam.read()
    cv2.imshow('frame', frame) 
    	    
    if cv2.waitKey(1) & 0xFF == ord('q'):     
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        cv2.imwrite('WebCamPic_'+timestamp+'.png', frame)
        break

cv2.destroyAllWindows() 
cam.release()
    
root.destroy() # Distroy TK window


