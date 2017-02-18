from controller import *
from time import *
import math
from noise import pnoise3, snoise3
from random import randint

controller = Controller()
dim = controller.getDim()
width = dim[0]
height = dim[1]

PositiveThreshold = 0
NegativeThreshold = .65
scale = 1 / 16.0
zScale = 1 / 64.0
dist = scale * width

start = randint(0, 100000)
per = .1

last = [[[0, 0, 0, 0] for y in range(height)] for x in range(width)]
curr = [[[0, 0, 0, 0] for y in range(height)] for x in range(width)]
twoB4 = last[:]
threeB4 = last[:]


def randomize1(z, threshold, normal):
    # controller.clearScreen()
    # z = 1
    global curr
    # curr = [ [ [0, 0, 0]  for y in range(height)] for x in range(width)]
    for y in range(width):
        for x in range(height):
            r = 128.0 + 127.0 * \
                (snoise3(x * scale, y * scale, start +
                         z * zScale, octaves=1, persistence=per))
            g = 128.0 + 127.0 * (snoise3(x * scale + dist, y * scale +
                                         dist, start + z * zScale, octaves=1,
                                         persistence=per))
            b = 128.0 + 127.0 * (snoise3(x * scale - dist, y * scale -
                                         dist, start + z * zScale, octaves=1,
                                         persistence=per))
            if(normal):
                curr[x][y][0] = r
                curr[x][y][1] = g
                curr[x][y][2] = b
            if r > 255 * threshold or g > 255 * threshold or
            b > 255 * threshold:
                if normal:
                    curr[x][y][3] = 1
                    controller.setPixel(x, y, r, g, b)
                else:
                    # print(curr[x][y], curr[x][y] == [0, 0, 0])
                    if curr[x][y][3] == 0:
                        curr[x][y][3] = 1
                        controller.setPixel(x, y, curr[x][y][0], curr[
                                            x][y][1], curr[x][y][2])
                    else:
                        curr[x][y][3] = 0
                        controller.setPixel(x, y, 0, 0, 0)
            # else:
        # controller.updateScreen(0)


def nCount(lx, ly):
    global last
    neighbors = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            # neighbors.append(1)
            if not (x == 0 and y == 0):
                nx = lx + x
                ny = ly + y
                if not (nx < 0 or nx >= width or ny < 0 or ny >= height):
                    if not (last[nx][ny][3] == 0):
                        neighbors.append(last[nx][ny])
    # print(len(neighbors))
    return neighbors
    # if x >
    # return 0


def computeColor(neighbors):
    r = 0
    g = 0
    b = 0
    num = len(neighbors)
    dom = randint(0, num - 1)
    # for i in range(num):
    # print(dom, num)
    r = neighbors[dom][0]
    g = neighbors[dom][1]
    b = neighbors[dom][2]
    return [r, g, b, 1]


def tick(z):
    global curr, last, twoB4
    twoB4 = last

    # print(z)
    curr = [[[0, 0, 0, 0] for y in range(height)] for x in range(width)]
    for y in range(width):
        for x in range(height):
            neighbors = nCount(x, y)
            if len(neighbors) < 2 or len(neighbors) > 3:
                # if not last[x][y] == [0, 0, 0]:
                controller.setPixel(x, y, 0, 0, 0)
            elif len(neighbors) == 3:
                if last[x][y][3] == 0:
                    # last[120, 100, 500]#GETCOLOR
                    curr[x][y] = computeColor(neighbors)
                    controller.setPixel(x, y, curr[x][y][0], curr[
                                        x][y][1], curr[x][y][2])
                else:
                    curr[x][y] = last[x][y]
                    controller.setPixel(x, y, curr[x][y][0], curr[
                                        x][y][1], curr[x][y][2])
                    # controller.setPixel(x, y, 100, 50, 10)
            elif len(neighbors) == 2:
                curr[x][y] = last[x][y]
    controller.updateScreen(.1)
    # print(last == curr)
    last = curr


def reset(array1, array2, astr):
    reset = True
    for y in range(height):
        for x in range(width):
            if difColor(array1[x][y], array2[x][y]):
                return False
    return True


def difColor(c1, c2):
    # if int(c1[0]) == int(c2[0]) and int(c1[1]) == int(c2[1]) and int(c1[2])
    # == int(c2[2]):
    if c1[3] == c2[3]:
        return False
    return True


def randomize(seed):
    randomize1(seed, PositiveThreshold, True)
    for i in range(0, 100):
        randomize1(seed + i * 500, NegativeThreshold, False)
    controller.updateScreen(0)
    controller.updateScreen(5)


randomize(0)
last = curr
numThis = 0
resetTick = 1
for i in range(100000000000):
    # curr
    fourB4 = threeB4[:]
    threeB4 = twoB4[:]
    twoB4 = last[:]
    last = curr[:]
    # curr = []
    tick(i)
    if resetTick > 0 and (reset(threeB4, curr, "3b4") or
       reset(fourB4, curr, "4b4")):
        resetTick = -10
        # controller.updateScreen(2)
        # print("reseting..")
    if resetTick == 0:
        randomize(i)

        numThis = 0

    numThis = numThis + 1
    resetTick = resetTick + 1
    # print(curr[0][0])


# while True:
# 	controller.updateScreen(1)
# for z in range(10000):
# 	for y in range(width):
# 		for x in range(height):
# 			# minMax(v)
# 			# val = v*127.0 + 128.0
# 			controller.setPixel(x, y, r, g, b)
# 	# sleep(.1)
# 	controller.updateScreen(.1)
# 	# print("frame")
