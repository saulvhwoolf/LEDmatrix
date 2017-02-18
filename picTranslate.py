from PIL import Image
import sys
import math

photo = "Images/thing.png"
target_file = open("Images/output.txt", 'w')  # write mode
width = 30
height = 30
imgArray = [[[] for y in range(height)] for x in range(width)]

im = Image.open(photo, "r")
pw, ph = im.size
pix_val = list(im.getdata())


for y in range(ph):
    currRow = math.floor(height * y / ph)
    for x in range(pw):
        currCol = math.floor(width * x / pw)
        # print(currCol, currRow)
        imgArray[currCol][currRow].append(list(pix_val[y * pw + x]))
        # print(pix_val[y*pw+x])
        # controller.setPixel(currCol, currRow, 100, 100, 100)
        # controller.updateScreen(.01)

# print("Displaying Photo ", photoNum, "...")

for y in range(height):
    s = ""
    for x in range(width):
        r = 0
        g = 0
        b = 0
        colorRange = imgArray[x][y]
        length = len(colorRange)
        for i in range(length):
            r = r + colorRange[i][0]
            g = g + colorRange[i][1]
            b = b + colorRange[i][2]
        r = math.floor(r / length)
        g = math.floor(g / length)
        b = math.floor(b / length)
        s = s + "[" + str(r) + " " + str(g) + " " + str(b) + "]"
        # controller.setPixel(x, y, r, g, b)
# controller.updateScreen(0)
    target_file.write(s + "\n")
