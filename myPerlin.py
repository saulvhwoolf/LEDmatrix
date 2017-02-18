from controller import *
from time import *
import math
from noise import pnoise3, snoise3
from random import randint

controller = Controller()
dim = controller.getDim()
width = dim[0]
height = dim[1]
theRoot = .9
rootMult = -1


def changeRoot():
    global theRoot, rootMult
    theRoot = theRoot + .05 * rootMult
    if theRoot < .3:
        # print("Increasing")
        rootMult = 1
    elif theRoot > 1:
        # print("Decreasing")
        rootMult = -1


def root(n):
    multiplier = 1
    if n < 0:
        multiplier = -1
    return multiplier * math.pow(multiplier * n, theRoot)

per = .1

scale = 1 / 16.0
dist = scale * width
start = randint(0, 1000)

zScale = 1 / 64.0
for z in range(10000):
    # changeRoot()
    for y in range(width):
        for x in range(height):
            r = 128.0 + 127.0 * \
                root(snoise3(x * scale, y * scale, start +
                             z * zScale, octaves=1, persistence=per))
            g = 128.0 + 127.0 * root(snoise3(x * scale + dist, y * scale +
                                             dist, start + z * zScale,
                                             octaves=1, persistence=per))
            b = 128.0 + 127.0 * root(snoise3(x * scale - dist, y * scale -
                                             dist, start + z * zScale,
                                             octaves=1, persistence=per))
            # minMax(v)
            # val = v*127.0 + 128.0
            controller.setPixel(x, y, r, g, b)
    # sleep(.1)
    controller.updateScreen(.1)
    # print("frame")
