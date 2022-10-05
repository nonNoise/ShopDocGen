




import os
from PIL import Image
import re

print("FILE Making.....")

dir_path = './img'
os.makedirs(dir_path, exist_ok=True)
dir_path = './img/raw'
os.makedirs(dir_path, exist_ok=True)
dir_path = './img/1024x1024'
os.makedirs(dir_path, exist_ok=True)
dir_path = './img/640x640'
os.makedirs(dir_path, exist_ok=True)
dir_path = './PDF'
os.makedirs(dir_path, exist_ok=True)

print("Good.")

import glob


print("Image Building.....")

files = glob.glob("./img/raw/*.png")
file_list = files
files = glob.glob("./img/raw/*.jpg")
file_list = file_list + files

print("=== 1024 x 1024 ===")
img_size = 1024
output_dir = './img/1024x1024/'
for img_file in file_list:
    print("\t" + os.path.split(img_file)[1])
    img = Image.open(img_file).convert('RGBA')
    result = Image.new("RGBA", (img_size, img_size),  (255, 255, 255, 0))
    if(img.width > img.height):
            height = round(img.height * img_size / img.width)
            img_resized = img.resize((img_size, height))
            result.paste(img_resized, (0, int( (img_size-height)/2)))
    if(img.width < img.height):
            width  = round(img.width  * img_size / img.height)
            img_resized = img.resize((width, img_size))
            result.paste(img_resized, (int( (img_size-width)/2),0))
    if(img.width == img.height):
            img_resized = img.resize((img_size, img_size))
            result.paste(img_resized, (0,0))
    fname = os.path.split(img_file)[1].rsplit('.', 1)[0].replace(' ', '')
    result.save(output_dir+fname+".png", quality=100)


print("=== 640 x 640 ===")
img_size = 640
output_dir = './img/640x640/'
for img_file in file_list:
    print("\t" + os.path.split(img_file)[1])
    img = Image.open(img_file).convert('RGBA')
    result = Image.new("RGBA", (img_size, img_size),  (255, 255, 255, 0))
    if(img.width > img.height):
            height = round(img.height * img_size / img.width)
            img_resized = img.resize((img_size, height))
            result.paste(img_resized, (0, int( (img_size-height)/2)))
    if(img.width < img.height):
            width  = round(img.width  * img_size / img.height)
            img_resized = img.resize((width, img_size))
            result.paste(img_resized, (int( (img_size-width)/2),0))
    if(img.width == img.height):
            img_resized = img.resize((img_size, img_size))
            result.paste(img_resized, (0,0))
    fname = os.path.split(img_file)[1].rsplit('.', 1)[0].replace(' ', '_')
    result.save(output_dir+fname+".png", quality=100)


print("Success!")