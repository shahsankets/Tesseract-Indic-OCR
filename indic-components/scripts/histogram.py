#!/usr/bin/python
#-*- coding:utf8 -*-

import Image,ImageDraw
import sys, os

def horizontalHistogram (input_image, image_name):
    width = input_image.size[0]
    height = input_image.size[1]
    print "Width = %d and height = %d" %(width,height)
    histoGram = []
    for i in range (height):
        blackPixelCount = 0
        for j in range (width):
            pixel = input_image.getpixel ((j, i))
            if (pixel == 0):
                blackPixelCount += 1
        histoGram.append (blackPixelCount)
    print histoGram
    histogramImage = Image.new("L",(width,height),255)
    pen = ImageDraw.Draw(histogramImage)
    y = 0
    for count in histoGram:
        pen.line((0, y) + (count, y), fill=128)
        y += 1
    cumulativeImage = Image.new("L",(width * 2, height),255)
    cumulativeImage.paste (input_image, (0, 0, width, height))
    cumulativeImage.paste (histogramImage, (width, 0, width*2, height))
    cumulativeImage.save(image_name+"_"+".png","PNG")

def verticalHistogram ():
    pass

path = "/home/debayan/code/lower_descender_images/"
dirName = os.listdir (path)
for image_name in dirName:
    input_image = Image.open(path + image_name)
    horizontalHistogram (input_image, image_name)


#wt = input_image.size[0]
#ht = input_image.size[1]
##print wt," ",ht
#new_image=Image.new("L",(wt*2,ht),255)
#pen=ImageDraw.Draw(new_image)
#
#offset = 0
#prevtlx = 0
#for line in lines:
#    fields = line.split(' ')
#    delta_y = int(int(fields[4].strip())) - int(fields[2])
#    delta_x = int(fields[3]) - int(fields[1])
#    top_left_x = int(fields[1])
#    top_left_y = ht - int(fields[2]) - delta_y
#    bot_right_x = int(fields[3])
#    bot_right_y = ht - int(fields[4].strip()) + delta_y
#    box = (top_left_x,top_left_y,bot_right_x,bot_right_y)
#    char = input_image.crop(box)
#    char = char.rotate(90)
#    if top_left_x<prevtlx:
#        offset = 0
#    
#    newwt = char.size[0]
#    newht = char.size[1]
#
#    newbox = (top_left_x+offset , top_left_y , top_left_x+offset+newwt ,top_left_y+newht)
#    print newbox
#    offset = offset+ (newwt - newht + 2)
#    prevtlx = top_left_x
#     
#        new_image.paste(char, newbox)
#    #aw_input('>')
#new_image.save('mod.tif',"TIFF")
