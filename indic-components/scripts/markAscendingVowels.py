#!/usr/bin/python
#-*- coding:utf8 -*-

import Image,ImageDraw
import sys, os

def findMaatraaLocations (histoGram):
    currentLine = 0
    max = 0
    firstRun = True
    maatraaLocation = []
    maatraa = -1
    print histoGram
    while currentLine < len (histoGram):
        if histoGram [currentLine] == 0:
            currentLine += 1
            if not firstRun:
                maatraaLocation.append (maatraa)
                max = 0
            continue
        else:
            firstRun = False
            currentLine += 1
            if histoGram [currentLine] > max :
                maatraa = currentLine
                max = histoGram [currentLine]
    print maatraaLocation
    return maatraaLocation
        


def identifyMatraas (input_image):
    histoGram = []
    width = input_image.size[0]
    height = input_image.size[1]
    for i in range (height):
        blackPixelCount = 0
        for j in range (width):
            pixel = input_image.getpixel ((j, i))
            if (pixel == 0):
                blackPixelCount += 1
        histoGram.append (blackPixelCount)
    return findMaatraaLocations (histoGram)


def markMaatraas (input_image):
    maatraLocations = identifyMatraas (input_image)
    pen = ImageDraw.Draw (input_image)
    width = input_image.size[0]
    for y in maatraLocations:
        pen.line ((0, y, width, y))
    del pen
    input_image.show ()

input_image = Image.open(sys.argv[1])
markMaatraas (input_image)
