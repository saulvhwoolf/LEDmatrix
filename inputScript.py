from controller import *
from time import *
# import noise
from noise import pnoise3, snoise3
from random import randint


width = 30
height = 30
controller = Controller()


class Snake(object):

    def __init__(self, x, y, width, height):
        self.sWidth = width
        self.sHeight = height
        self.length = 1
        self.loc = [[x, y]]
        self.color = [255, 50, 0]
        self.fColor = [93, 59, 100]
        self.food = [20, 20]
        self.dir = [1, 0]
        self.newFood()
        self.dead = False

    def newFood(self):
        newX = randint(0, self.sWidth - 1)
        newY = randint(0, self.sHeight - 1)
        for i in range(len(self.loc)):
            if self.loc[i][0] == newX and self.loc[i][1] == newY:
                self.newFood()
            else:
                self.food = [newX, newY]

    def draw(self):
        for aLoc in self.loc:
            controller.setPixel(aLoc[0], aLoc[1], self.color[
                                0], self.color[1], self.color[2])
        controller.setPixel(self.food[0], self.food[1], self.fColor[
                            0], self.fColor[1], self.fColor[2])
        # controller.updateScreen(.1)

    def up(self):
        if not self.dir == [0, 1]:
            self.dir = [0, -1]

    def down(self):
        if not self.dir == [0, -1]:
            self.dir = [0, 1]

    def left(self):
        if not self.dir == [1, 0]:
            self.dir = [-1, 0]

    def right(self):
        if not self.dir == [-1, 0]:
            self.dir = [1, 0]

    def move(self):
        if not self.dead:
            newX = self.loc[0][0] + self.dir[0]
            newY = self.loc[0][1] + self.dir[1]
            self.wallCheck(newX, newY)
            self.selfCheck(newX, newY)
            if not self.dead:
                if len(self.loc) > 1:
                    for i in range(len(self.loc) - 1, 0, -1):
                        self.loc[i] = self.loc[i - 1]
                self.loc[0] = [newX, newY]

    def wallCheck(self, x, y):
        if x >= self.sWidth or x < 0 or y >= self.sHeight or y < 0:
            print("YOU DUN FUCKED UP")
            self.dead = True

    def selfCheck(self, newX, newY):
        if len(self.loc) > 1:
            for i in range(1, len(self.loc)):
                if self.loc[i][0] == newX and self.loc[i][1] == newY:
                    print("WHY'D OYU DO THSAT tho")
                    self.dead = True

    def foodCheck(self):
        # print(self.loc[0], self.food)
        if self.loc[0][0] == self.food[0] and self.loc[0][1] == self.food[1]:
            self.newFood()
            self.extend()

    def extend(self):
        lastId = len(self.loc) - 1
        self.loc.append([self.loc[lastId][0], self.loc[lastId][1]])

    def restart(self):
        self.loc = [self.loc[0]]
        self.dead = False
        self.newFood()
        self.dir = [self.dir[0] * -1, self.dir[1] * -1]


##########################################################################


snake = Snake(10, 10, width, height)


def onKeyPress(self, key, modifiers):
    global snake
    if key == pyglet.window.key.UP:
        snake.up()
    elif key == pyglet.window.key.DOWN:
        snake.down()
    elif key == pyglet.window.key.LEFT:
        snake.left()
    elif key == pyglet.window.key.RIGHT:
        snake.right()
    elif key == pyglet.window.key.ESCAPE:
        print("Quit")
        sys.exit()
    elif key == pyglet.window.key.R:
        snake.restart()
controller.updateKeyPress(onKeyPress)

while(True):
    snake.move()
    snake.foodCheck()
    controller.clearScreen()
    snake.draw()
    controller.updateScreen(.1)
    # print("frame")
