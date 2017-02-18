from controller import *
from random import randint, random


controller = Controller()
dim = controller.getDim()
width = dim[0]
height = dim[1]

myMap = [[[0, 0, 0] for y in range(height)] for x in range(width)]

compute = []
nextC = []

numIslands = 1
disapear = .00000000001
#chooseStart


def genColor(ro, go, bo, x, y):

    r = myMap[x][y][0]
    g = myMap[x][y][1]
    b = myMap[x][y][2]

    if r+b+g ==0:
        r = 255
        b = 255
        g = 255
    # elif r+b+g < 30:
    #     return [0, 0, 0]

    return [(ro)*r,(go)*g,(bo)*b]
    # return [(ro)*r,(ro)*r, (ro)*r]


def colorOdds():
    o = random()*-.15
    return o

def gen():
    global compute, nextC
    if len(compute) >0:
        for i in compute:
            x = i[0]
            y = i[1]
            o = i[2]
            if o > 0 and x >= 0 and x < width and y >= 0 and y < height and myMap[x][y] == [0, 0, 0]:
                odds = random()
                # if odds <= i[2]:
                myMap[x][y]= genColor(colorOdds() + o, colorOdds()+ o, colorOdds() + o, i[3], i[4])
                controller.setPixel(x, y, myMap[x][y][0], myMap[x][y][1], myMap[x][y][2])
                if not(myMap[x][y] == [0, 0, 0]):
                    nextC.append([x-1, y, o-random()*disapear, x, y])
                    nextC.append([x+1, y, o-random()*disapear, x, y])
                    nextC.append([x, y-1, o-random()*disapear, x, y])
                    nextC.append([x, y+1, o-random()*disapear, x, y])
                # else:
                #     print(x, y, "did not")
        controller.updateScreen(0)
        compute = nextC
        nextC = []
        gen()

def do(): 
    global myMap       
    for i in range(numIslands):
        x = randint(0,width)
        y = randint(0,height)
        compute.append([x, y, 1, 0, 0])
    gen()
    myMap = [[[0, 0, 0] for y in range(height)] for x in range(width)]


# do()
while True:
    do()
    controller.updateScreen(.1)

