from controller import *
from time import *
from noise import pnoise3, snoise3


width = 30
height = 30
controller = Controller()


def wheel(pos):
	if pos < 85:
		return [pos * 3, 255 - pos * 3, 0]
	elif pos < 170:
		pos -= 85
		return [255 - pos * 3, 0, pos * 3]
	else:
		pos -= 170
		return [0, pos * 3, 255 - pos * 3]

for j in range(256):
	print(j)
	for y in range(height):
		for x in range(width):
			color = wheel((j+x+y)&255)
			controller.setPixel(x, y, color[0], color[1], color[2])
	controller.updateScreen(0)

