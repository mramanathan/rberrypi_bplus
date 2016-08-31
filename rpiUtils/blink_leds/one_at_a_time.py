#!/usr/bin/env python

from gpiozero import LED
import time

# code for blinking one LED
led = LED(17)


def blink():
	""" Pull pin HIGH and light up LED.

	Then sleep for 1mSec and pull pin
	down to turn OFF LED.
	"""

	led.on()
	time.sleep(1)
	led.off()
	time.sleep(1)



def main():
	""" Each and every LED shall be

	blinked in sequential order, the
	blink freqquency is 5 times with
	an interval of 1mSec.
	"""

	for inc in range(10,15):
		blink()




if __name__ == "__main__":
	main()
