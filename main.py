#   Main python file to run

import os
import tkinter as tk

#   Import compressor file
from compressor import *

window=tk.Tk(screenName="File Compressor")
window.title("File Compressor by huffman coding")
if 'sfu' == os.name:
    img = tk.PhotoImage(file="imgs/app_icon.gif")
    window.iconphoto(True,img)
else:
    window.iconbitmap("imgs/app_icon.ico")


    #   Set window size
width = 1000
height= 1000
window.geometry("{}x{}".format(width, height)) #same as in width and height
#window.config(bg = tk.darkThemeBg)


#ADD A LABEL THAT WRITES FILE COMPRESSOR IN THE WINDOW
label=tk.Label(text="File Compressor",
            font=("times new roman", 16),
            border=5,
            #image = r"D:\DSA project\imgs\compress2.png",
            width=20,
            height=5,
            fg="white",
            justify="center")
label.config(text="File Compressor", 
             #image = r"D:\DSA project\imgs\compress2.png",
             fg="Black")
label.pack(padx=100,pady=50)
homeImg = tk.PhotoImage(file="imgs/new.png").subsample(3,3)
window.mainloop()