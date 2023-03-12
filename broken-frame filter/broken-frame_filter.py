#!/usr/bin/env python
# coding: utf-8

# # Filter #1: Broken Frame 🔨

# My broken_frame() function creates a fractured effect in the image below that I liken in appearance to the Distorted Glass filter in Photoshop. 

import PIL.ImageOps
from PIL import Image

def broken_frame(image):
    length = image.size[1]
    for x in range(image.size[0]):
        for y in range(length - x):
            left = image.getpixel((x, y))
            right = image.getpixel((length - 1 - x, y))
            image.putpixel((length - 1 - x, y), left)
            image.putpixel((x, y), right)

testimage = Image.open('black girls in ux.png') 

testimage

broken_frame(testimage)
testimage
