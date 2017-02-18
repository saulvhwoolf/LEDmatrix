import sys
# import time
from time import *
mode = "n"
if len(sys.argv) < 3:
    print("please input x and y")
    sys.exit()
if len(sys.argv) == 4:
    mode = sys.argv[3]

width = int(sys.argv[1])
height = int(sys.argv[2])

if mode == "m":
    from matrixLibrary import *
elif mode == "d":
    from displayLibrary import *
else:
    mode = "n"
    from displayLibrary import *
    from matrixLibrary import *


class Controller(object):

    def __init__(self):
        global width, height, mode
        self.width = width
        self.height = height
        self.mode = mode
        self.lastTick = time()
        if self.mode == "m":
            self.controller1 = Matrix(self.width, self.height)
        elif self.mode == "d":
            self.controller1 = Display(600, 600, self.width, self.height)
        else:
            self.controller1 = Display(600, 600, self.width, self.height)
            self.controller2 = Matrix(self.width, self.height)

    def updateScreen(self, updateTime):
        newTime = time()
        dif = newTime - self.lastTick
        if dif < updateTime:
            sleep(updateTime - dif)
        self.lastTick = time()
        self.controller1.updateScreen()
        # self.strip.show()

    def setPixel(self, x, y, r, g, b):
        self.controller1.setPixel(x, y, r, g, b)
        if(self.mode == "n"):
            self.controller2.setPixel(x, y, r, g, b)

    def clearScreen(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.controller1.setPixel(x, y, 0, 0, 0)
                if(self.mode == "n"):
                    self.controller2.setPixel(x, y, 0, 0, 0)

    def updateKeyPress(self, new):
        print("PLSS")
        if self.mode == "d":
            self.controller1.updateKeyPressMethod(new)

    def getDim(self):
        return [self.width, self.height]
