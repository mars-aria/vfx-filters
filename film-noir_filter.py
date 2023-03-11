#!/usr/bin/env python
# coding: utf-8

# In[1]:


# # Filter #2: Film Noir 🕵🏾‍♀️

# My film_noir() function transforms this image of the Strawhat Pirates from the manga "One Piece" by creating a black-and-white, vintage style effect similar to the Grayscale filter in Photoshop. 

# In[54]:


from PIL import Image


# In[55]:


import PIL.ImageOps


# In[56]:


def film_noir(img):
    img = Image.open('strawhat pirates.png')
    rgbimage = img.convert('RGB')
    film_noir = PIL.ImageOps.grayscale(rgbimage)
    film_noir.save('film_noir.png')
    return film_noir


# In[57]:


film_noir(film_noir)

