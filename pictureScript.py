# text morphing
# tetris
# brick breaker
from PIL import Image
from controller import *
import math


def main():
    controller = Controller()
    dim = controller.getDim()
    width = dim[0]
    height = dim[1]

    # image_part = kitten.get_region(x=10, y=10, width=100, height=100)

    imgArray = [[[] for y in range(height)] for x in range(width)]

    for i in range(10):
        for photoNum in range(0, 4):
            print("Displaying file ", photoNum, "...")
            fileName = "Images/" + str(photoNum) + ".txt"
            file = open(fileName, "r")

            pw, ph = 30, 30
            # pix_val = list(im.getdata())
            currRow = 0
            for line in file:
                # print(currRow)
                analyzeLine(controller, line, currRow, 0)
                currRow = currRow + 1
            controller.updateScreen(0)
            for i in range(10):
                controller.updateScreen(.1)

    while(True):
        controller.updateScreen(.1)


# pix_val_flat = [x for sets in pix_val for x in sets]

def analyzeLine(controller, line, currRow, currCol):
    if currCol < 30:
        left = line.find("[")
        right = line.find("]")

        section = line[left + 1:right]
        # print(section)

        space = section.find(" ")
        # print("space" + str(space))
        r = int(section[:space])
        # print("r:" + str(r))

        section = section[space + 1:]
        space = section.find(" ")
        g = int(section[:space])
        # print("g:" + str(g))

        section = section[space + 1:]
        # space = section.find(" ")
        b = int(section)
        # print("b:" + str(b))

        # print(str(int(r) + int(b) + int(g)))
        rest = line[right + 1:]
        # print(r + "," + g  + "," +  b)
        controller.setPixel(currCol, currRow, r, g, b)
        analyzeLine(controller, rest, currRow, currCol + 1)


main()
