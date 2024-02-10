# Main python file to run

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter
import tkinter.font as font
import os

# Import compressor file
from compressor import *

# Import PhotoImage
from tkinter import PhotoImage

width = 1000
height = 1000

window = Tk()
window.title("File Compressor by Huffman Coding")

# Set window size
window.geometry("{}x{}".format(width, height))

# Set window icon
window.iconbitmap(os.path.join("imgs", "app_icon.ico"))

# Load the background image
background_image = PhotoImage(file="imgs/new.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to display success message
def displayMessageBox(title, description):
    messagebox.showinfo(title, description)

# Function to compress file
def compressFile():
    window.filename = filedialog.askopenfilename(initialdir=os.path.normpath("C://"),
                                                  title="Select A Text File",
                                                  filetypes=(("text files", "*.txt"),))
    file_path = window.filename
    compressFile = compress()  # Corrected instantiation
    compressed_file_path = compressFile.compressor(file_path)
    displayMessageBox("Compression Success",
                      f"You have successfully compressed the file to the same directory")

# Function to extract file
def extractFile():
    window.filename = filedialog.askopenfilename(initialdir=os.path.normpath("C://"),
                                                  title="Select A Binary File",
                                                  filetypes=(("binary files", "*.bin"),))
    file_path = window.filename
    decompressFile = compress()  # Corrected instantiation
    extracted_file_path = decompressFile.decompressor(file_path)
    displayMessageBox("Extraction Success",
                      f"You have successfully extracted the file to the same directory")

# Function to quit the application
def quitApp():
    window.destroy()

# Use CTkButton instead of tkinter Button for compress and extract button

# Set Y coordinates with appropriate spacing
quitButton = customtkinter.CTkButton(master=window,
                                      text="Quit",
                                      text_color=("black", "black"),
                                      hover=True, hover_color="#0b6eca",
                                      width=170,
                                      height=50,
                                      border_width=0,
                                      corner_radius=0,
                                      command=quitApp)
quitButton.place(x=width/2, y=height/2 - 60, anchor=CENTER)

extractButton = customtkinter.CTkButton(master=window,
                                         text="Extract file",
                                         text_color=("black", "black"),
                                         hover=True, hover_color="#0b6eca",
                                         width=170,
                                         height=50,
                                         border_width=0,
                                         corner_radius=0,
                                         command=extractFile)
extractButton.place(x=width/2, y=height/2 - 120, anchor=CENTER)

compressButton = customtkinter.CTkButton(master=window,
                                         text_color=("black", "black"),
                                         text="Compress file",
                                         hover=True,
                                         hover_color="#0b6eca",
                                         width=170,
                                         height=50,
                                         border_width=0,
                                         textvariable="new roman times",
                                         corner_radius=0,
                                         command=compressFile)
compressButton.place(x=width/2, y=height/2 - 180, anchor=CENTER)

window.mainloop()

