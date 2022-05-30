import os
import cv2
import sys
import numpy as np
from PIL import Image

#ASCII CHARACTERS USED TO BUILD THE OUTPUT TEST
ASCII_CHARS=["@","#","S","%","?","*","+",";",":",",","."]

#RESIZE IMAGE ACCORDING TO A new_width AND COVERTING EACH PIXEL TO GRAYSCALE
def resized_gray_image(image,new_width=70): 
    width,height=image.size
    aspect_ratio=height/width
    new_height=int(aspect_ratio*new_width)
    resized_gray_image=image.resize((new_width,new_height)).convert('L')
    return resized_gray_image

#CONVERT PIXELS TO A STRING OF ASCII CHARACTERS
def pix2chars(image): 
    pixels = image.getdata()
    characters="".join([ASCII_CHARS[pixel//25]for pixel in pixels])
    return characters


def generate_frame(image,new_width=70): 
#COVERT IMAGE TO ASCII
    new_image_data=pix2chars(resized_gray_image(image))

#FORMAT   
    total_pixels=len(new_image_data)
    
    ascii_image="\n".join([new_image_data[index:(index+new_width)]for index in range(0,total_pixels,new_width)])

#DISPLAY OUTPUT DIRECTLY TO SCREEN UNLIKE PRINT IT CANT SWITCH TO NEW LINE 
    sys.stdout.write(ascii_image)

#THIS EXECUTES COMMAND IN A SUBSHELL AND OS IS OPENED    
    os.system('cls')

#THIS F'N ALLOWS YOU TO TAKE VIDEOS IF cv2.VideoCapture(0) OTHERWISE YOU CAN ENTER THE PATH TO VIDEO FILE USING R AS R 
#CHANGES THE STRING TO UNICODE SO THAT IT CAN BE DETECTED.
cap=cv2.VideoCapture(r"C:\Users\shivansh uppal\Videos\Captures\blackvideo.mp4")

#TILL VIDEO IS VALID
while True:

#THIS RETURNS SPECIFIED NUMBER OF BYTES FROM THE FILE DEFAULT IS -1 THAT IS COMPLETE FILE
   ret,frame=cap.read()

#The function imshow displays an image in the specified window.
   cv2.imshow('frame',frame)

#Creates an image memory from an object exporting the array interface (using the buffer protocol).
#If obj is not contiguous, then the tobytes method is called and ~PIL.Image.frombuffer is used.
#If you have an image in NumPy:
#from PIL import Image
#import numpy as np
#im = Image.open('hopper.jpg')
#a = np.asarray(im)
#Then this can be used to convert it to a Pillow image:
#im = Image.fromarray(a)

   generate_frame(Image.fromarray(frame))
   
#The function waitKey waits for a key event infinitely  or for delay . milliseconds, when it is positive
   cv2.waitKey(4)
   