from pyglet import clock, font, image, window
from pyglet.gl import *


class Entity(object):

    def __init__(self, id, size, x, y):
        self.id = id
        self.size = size
        self.x = x
        self.y = y
        self.r = 0
        self.g = 0
        self.b = 0

    def draw(self):
        glLoadIdentity()
        glTranslatef(self.x, self.y, 0.0)
    # glRotatef(0, 0, 0, 1)
        if self.size > 4:
            glScalef(self.size - 1, self.size - 1, 1.0)
        else:
            glScalef(self.size, self.size, 1.0)
        glBegin(GL_QUADS)
        glColor3f(self.r, self.g, self.b)
        glVertex2f(1, -1)
        glVertex2f(1, 1)
        glVertex2f(-1, 1)
        glVertex2f(-1, -1)
        glEnd()

    def updateColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class World(object):

    def __init__(self, width, height):
        self.ents = {}
        self.nextEntId = 0
        self.width = width
        self.height = height

    def addEntity(self, x, y, w, h):
        size = 5.0
        x = x * size * 2 - (w - 1) * size
        y = y * size * 2 - (h - 1) * size
        ent = Entity(self.nextEntId, size, x, y)
        self.ents[ent.id] = ent
        self.nextEntId += 1
        return ent

    def updateColor(self, x, y, r, g, b):
        theId = y + self.height * x
        self.ents[theId].updateColor(r / 255.0, g / 255.0, b / 255.0)

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        for ent in self.ents.values():
            ent.draw()


class Camera(object):

    def __init__(self, win, x=0.0, y=0.0, rot=0.0, zoom=1.0):
        self.win = win
        self.x = x
        self.y = y
        self.rot = rot
        self.zoom = zoom

    def worldProjection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        widthRatio = self.win.width / self.win.height
        gluOrtho2D(
            -self.zoom * widthRatio,
            self.zoom * widthRatio,
            -self.zoom,
            self.zoom)

    def hudProjection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.win.width, 0, self.win.height)


class Hud(object):

    def __init__(self, win):
        self.fps = clock.ClockDisplay()

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.fps.draw()


class App(object):

    def __init__(self, wIn, hIn, pX, pY):
        self.world = World(pX, pY)
        self.win = window.Window(
            width=wIn, height=hIn, fullscreen=False, vsync=True)
        self.camera = Camera(self.win, zoom=pX * 5 + 1)
        self.hud = Hud(self.win)
        self.pX = pX
        self.pY = pY
        clock.set_fps_limit(30)
        for x in range(0, pX):
            for y in range(0, pY):
                self.world.addEntity(x, pY - y - 1, pX, pY)

    def updateScreen(self):
        self.win.dispatch_events()

        self.camera.worldProjection()
        self.world.draw()

        self.camera.hudProjection()
        self.hud.draw()

        clock.tick()
        self.win.flip()
        return self

    def setPixel(self, x, y, r, g, b):
        self.world.updateColor(x, y, r, g, b)
