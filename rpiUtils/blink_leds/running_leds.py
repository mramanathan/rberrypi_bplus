#!/usr/bin/env python

import RPi.GPIO as gpio
import time

## pinout reference
# gpio_bcm_board

## generic settings for Pi Modem B+ Rev1.2

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

# code for blinking one LED
""" 
pin_num = 7
gpio.setup(pin_num, gpio.OUT)
"""

## power up 3 LEDs in sequential order
led_pins = [22, 24, 26]
for i in led_pins:
	gpio.setup(i, gpio.OUT)



def blink():
	""" Pull pin HIGH and light up LED.

	Then sleep for 0.25mSec and then
	pull the pin LOW. 
	Repeat the sequence for three LEDs.
	"""

	for led in led_pins:
		gpio.output(led, gpio.HIGH)
		time.sleep(0.25)
		gpio.output(led, gpio.LOW)
#		time.sleep(1)



def main():
	""" Each and every LED shall be

	blinked in sequential order with
	frequency of five times.
	"""

	for inc in range(10,15):
		blink()

	gpio.cleanup()



if __name__ == "__main__":
	main()
