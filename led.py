# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel



pixel_pin1 = board.D18
pixel_pin2 = board.D27


num_pixels = 60


ORDER = neopixel.GRB



def wheel(pos):
    
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait,LED):
    if LED:
        pixels = neopixel.NeoPixel(pixel_pin1, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
    else:
        pixels = neopixel.NeoPOixel(pixel_pin2, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def No_led(LED):
    if LED:
        pixels = neopixel.NeoPixel(pixel_pin1, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
    else:
        pixels = neopixel.NeoPixel(pixel_pin2, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
    pixels.fill((0,0,0))
    pixels.show()
