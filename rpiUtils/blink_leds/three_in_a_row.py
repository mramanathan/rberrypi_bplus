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



def blink(led):
	""" Pull pin HIGH and light up LED.

	Then sleep for 1mSec and pull pin
	down to turn OFF LED.
	"""

	gpio.output(led, gpio.HIGH)
	time.sleep(1)
	gpio.output(led, gpio.LOW)
	time.sleep(1)



def main():
	""" Each and every LED shall be

	blinked in sequential order, the
	blink freqquency is 5 times with
	an interval of 1mSec.
	"""

	for i in led_pins:
		for inc in range(10,15):
			blink(i)

	gpio.cleanup()



if __name__ == "__main__":
	main()
