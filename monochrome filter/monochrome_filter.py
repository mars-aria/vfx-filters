#!/usr/bin/env python
# coding: utf-8

# In[1]:

#!/usr/bin/env python
# coding: utf-8

# # Monochrome Filter 🐺

# My monochrome_filter() function transforms this image of the wolf character Legoshi from the manga "Beastars" into a formidable beast by adding a monochrome effect to his appearance.

# In[189]:

from PIL import Image

# In[190]:

import PIL.ImageOps

def monochrome_filter(monochrome):
    img = Image.open('legoshi.png')
    rgbimage = img.convert('RGB')
    monochrome = PIL.ImageOps.invert(rgbimage)
    monochrome.save('monochrome.png')
    return monochrome

monochrome_filter(monochrome_filter)
