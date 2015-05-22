'''
Created on 12 Sep 2014

@author: hpais
'''

import argparse
import cropper, slider

def crop_and_add_to_slide(fd,fdout,top,bottom,left,right,nrow,ncol):
    picwidth = right - left
    picheight = bottom - top

    cropper.crop_folder(fd,fdout,top,bottom,left,right)
    slider.image_folder2pptx(fdout,fd+"presentation.pptx",nrow,ncol,\
                             picwidth, picheight)



def execute(args):
    fd = args.image_folder
    top = int(args.pixel_top)
    bottom = int(args.pixel_bottom)
    left = int(args.pixel_left)
    right = int(args.pixel_right)
    nrow = int(args.number_rows)
    ncol = int(args.number_columns)
    fdout = fd+"cropped/"
    crop_and_add_to_slide(fd,fdout,top,bottom,left,right,nrow,ncol)

parser = argparse.ArgumentParser(description="Automates generation of powerpoint slides from set of images")
parser.set_defaults(func=execute)
parser.add_argument("-f","--image_folder", help="folder containing images to be included in powerpoint file")
parser.add_argument("-t","--pixel_top", help="top coordinate for cropping")
parser.add_argument("-b","--pixel_bottom", help="bottom coordinate for cropping")
parser.add_argument("-l","--pixel_left", help="left coordinate for cropping")
parser.add_argument("-r","--pixel_right", help="right coordinate for cropping")
parser.add_argument("-x","--number_rows", help="number of image rows per powerpoint slide")
parser.add_argument("-y","--number_columns", help="number of image columns per powerpoint slide")

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
