import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)

flag = False
while True:
	GPIO.output(17, flag)
	flag = not(flag)
	sortie = raw_input()
	if sortie == "exit":
		GPIO.output(17, False)
		break

while True:
	time.sleep(1)
	GPIO.output(17, flag)
	flag = not(flag)

