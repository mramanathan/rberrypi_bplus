#!/usr/bin/env python

from gpiozero import Buzzer
from time import sleep

##pinout reference
# gpio_bcm

# GPIO17 maps to pin # 11 in Model B+
buzzer = Buzzer(17)

while True:
	buzzer.on()
	sleep(1)
	buzzer.off()
	sleep(1)

while True:
	buzzer.beep()
	sleep(1)


