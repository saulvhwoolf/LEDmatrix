from pygletLibrary import *
import sys


class Display(object):
	def updateKeyPressMethod(self, newMethod):
		print("Transplanting ")
		self.onKeyPress = newMethod
		@self.app.win.event
		def on_key_press(key, modifiers):
			self.onKeyPress(self, key, modifiers)
			self.escape(key, modifiers)
		# onKeyPress = newMethod

	def __init__(self, wIn, hIn, pX, pY):
		self.width = pX
		self.height = pY
		self.app = App(wIn, hIn, self.width, self.height)
		self.app.updateScreen()

		@self.app.win.event
		def on_key_press(key, modifiers):
			self.escape(key, modifiers)
		    # if key == pyglet.window.key.UP:
		    #     print("")
		    # elif key == pyglet.window.key.DOWN:
		    #     c.move_down()
		    # elif key == pyglet.window.key.RIGHT:
		    #     c.move_right()
		    # elif key == pyglet.window.key.LEFT:
		    #     c.move_left()

	def updateScreen(self):
		self.app.updateScreen()

	def setPixel(self, x, y, r, g, b):
		self.app.setPixel(x, y, r, g, b)

	def escape(self, key, modifiers):
		if key == pyglet.window.key.ESCAPE:
			print("Quit")
			sys.exit()

	