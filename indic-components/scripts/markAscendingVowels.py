#!/usr/bin/python
#-*- coding:utf8 -*-

import Image,ImageDraw
import sys, os


maatraaLocations = []

def findMaatraaLocations (histoGram):
    currentLine = 0
    max = 0
    firstRun = True
    maatraa = -1
    store = True
    print histoGram
    while currentLine < len (histoGram):
        if histoGram [currentLine] == 0:
            currentLine += 1
            if not firstRun and store:
                maatraaLocations.append (maatraa)
                store = False
                max = 0
            continue
        else:
            firstRun = False   
            store = True
            currentLine += 1
            if histoGram [currentLine] > max :
                maatraa = currentLine
                max = histoGram [currentLine]
    print maatraaLocations
        


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
    findMaatraaLocations (histoGram)


def markMaatraas (input_image):
    identifyMatraas (input_image)
#    pen = ImageDraw.Draw (input_image)
#    width = input_image.size[0]
#    for y in maatraaLocations:
#        pen.line ((0, y, width, y))
#    del pen
    input_image.show ()

def createGaps (input_image):
    global maatraaLocations
    originalHeight = input_image.size [1]
    numberOfLines = len (maatraaLocations)
    newHeight = originalHeight + ( 4 * numberOfLines) # We will introduce a vertical gap of 3 pixel height for each maatraa
    newWidth = originalWidth = input_image.size [0]
    gappedImage = Image.new ("1",(newWidth, newHeight), 255)
    count = 0
    while count < len (maatraaLocations):
        print count
        if count == len (maatraaLocations) - 1:
            imageToPaste = input_image.crop ((0, maatraaLocations[count], newWidth, originalHeight))
        else:
            imageToPaste = input_image.crop ((0, maatraaLocations[count], newWidth, maatraaLocations[count + 1]))
        gappedImage.paste (imageToPaste, (0, maatraaLocations[count] + (3 * count))) 
        count += 1
    gappedImage.show ()

input_image = Image.open(sys.argv[1])
markMaatraas (input_image)
createGaps (input_image)
