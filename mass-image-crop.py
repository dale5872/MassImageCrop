import os, sys, glob
from PIL import Image, ImageFilter, ImageOps

#Get list of files
images = glob.glob(sys.argv[1] + '/**/*.jpeg', recursive=True)
print(images)

for file in images:
    print("Opened: " + file)
    image = Image.open(file)
    imageWidth = image.width
    imageHeight = image.height
    imageRGB = image.convert('RGB')

    rightBorder = 0
    bottomBorder = 0
    leftBorder = 0
    topBorder = 0

    var = reversed(range(imageWidth))

    print("Image width: " + str(imageWidth) + "\nImage Height: " + str(imageHeight))
    
    #Work from the right side
    for pixel in reversed(range(imageWidth)):
        r,g,b = imageRGB.getpixel((pixel, 50))
        if r != 0 | g != 0 | b != 0:
            rightBorder = pixel
            print("Right Border at: " + str(pixel))
            break

    #Work from the bottom
    for pixel in reversed(range(imageHeight)):
        r,g,b = imageRGB.getpixel((100, pixel))
        if r != 0 | g != 0 | b != 0:
            bottomBorder = pixel
            print("Bottom Border at: " + str(pixel))
            break

    #work from the left
    for pixel in range(imageHeight):
        r,g,b = imageRGB.getpixel((pixel, 100))
        if (r != 0 | g != 0 | b != 0) | (r != 255 | g != 255 | b != 255):
            leftBorder = pixel
            print("Left Border at: " + str(pixel))
            break

    #work from the top
    for pixel in range(imageHeight):
        r,g,b = imageRGB.getpixel((100, pixel))
        if (r != 0 | g != 0 | b != 0) | (r != 255 | g != 255 | b != 255):
            topBorder = pixel
            print("Top Border at: " + str(pixel))
            break

    if rightBorder == 0 & bottomBorder == 0:
        print("File unchanged! \n")
        continue

    imageRegion = (leftBorder + 10, topBorder + 10, (rightBorder-25)+leftBorder, (bottomBorder-25)+topBorder)
    region = image.crop(imageRegion)

    region.save(file)
    print("Saved file: " + file + "\n")


