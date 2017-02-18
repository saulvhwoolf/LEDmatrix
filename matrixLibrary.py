from neopixel import *

# LED strip configuration:
LED_COUNT      = 0      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


class Matrix(object):
	def __init__(self, pX, pY):
		self.width = pX
		self.height = pY
		self.makeTranslationMatrix(self.width, self.height)
		self.strip = Adafruit_NeoPixel(self.width*self.height, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		self.strip.begin()


	def updateScreen(self):
		self.strip.show()

	def setPixel(self, x, y, r, g, b):
		self.strip.setPixelColor(self.translateMatrix[x][y], Color(int(r), int(g), int(b)))

	def makeTranslationMatrix(self, width, height):
		self.translateMatrix = [[0 for x in range(width)] for y in range(height)] 
		for x in range(0, width):
			for y in range(0, height):
				newX = x
				if y%2 == 1:
					newX = width-x-1
				index = y*width + newX
				self.translateMatrix[x][y] = index


#strip = adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
