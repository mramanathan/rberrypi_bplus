#!/usr/bin/env python

from gpiozero import LED
from time import sleep

## pinout reference:
# gpio_bcm

# code for blinking one LED
# GPIO17 maps to pin # 11 on Model B+
led = LED(17)


def blink():
	""" Pull pin HIGH and light up LED.

	Then sleep for 1mSec and pull pin
	down to turn OFF LED.
	"""

	cnt1 = 3
	cnt2 = 10
	sleep_msecs = 5

	print("Blink frequency {}".format(cnt1))
	print("Start blinking LED with background set to False")
	## To show the effects of background parameter in led.blink
	for i in range(0, cnt1):
		led.blink(on_time=1, off_time=1, n=i, background=False)

	print("Sleeping for {} milli-seconds ...".format(sleep_msecs))
	sleep(sleep_msecs)

	print("Blink frequency {}".format(cnt2))
	print("Start blinking LED with background set to True")
	# Though counter is set to 10, LED will blink once and then fall silent
	for j in range(0, cnt2):
		led.blink(on_time=1, off_time=1, n=j, background=True)
	
	print("Why LED blinked just once while the request was to repeat {} iterations?".format(cnt2))


def main():
	""" Each and every LED shall be

	blinked in sequential order, the
	blink freqquency is 5 times with
	an interval of 1mSec.
	"""

	# range iteration not needed as led.blink will
	# repeat blinking as per value for n
#	for inc in range(10,15):
	blink()



if __name__ == "__main__":
	main()
