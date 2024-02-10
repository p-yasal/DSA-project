import os

image_path = r"D:\DSA project\imgs\compress2.png"

if os.path.exists(image_path):
    print("Image file exists.")
else:
    print("Image file not found.")
