'''
Created on 12 Sep 2014

@author: hpais
'''

import os
from PIL import Image

PIC_EXT_LIST = [".png", ".jpeg", ".bmp", "png",".tif",".tiff"]

def crop_folder(fd,fdout,top,bottom,left,right):
    if not os.path.exists(fdout):
        os.makedirs(fdout)
    for fn in os.listdir(fd):
        fn_extension = os.path.splitext(fn)[1]
        if os.path.isfile(fd+fn) and fn_extension in PIC_EXT_LIST:
            print fn
            im = Image.open(fd+fn)
            cropped = im.crop((left,top,right,bottom))
            cropped.save(fdout+fn, "png")
            #cropped.close()
