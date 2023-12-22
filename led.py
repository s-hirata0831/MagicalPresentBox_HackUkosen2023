import time
import board
import neopixel



pixel_pin = board.D10


num_pixels = 120


ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def led_light():
    for i in range(60):
        pixels[i] = (0,255,0)
    pixels.show()

def No_led():
    for i in range(60):
        pixels[i] = (0,0,0)
    pixels.show()

