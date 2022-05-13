from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)
kit.servo[1].set_pulse_width_range(1100,1900)
kit.servo[2].set_pulse_width_range(1100,1900)
kit.servo[3].set_pulse_width_range(1100,1900)
kit.servo[4].set_pulse_width_range(1100,1900)
kit.servo[5].set_pulse_width_range(1100,1900)
kit.servo[6].set_pulse_width_range(1100,1900)
i=0
flag=0
while True:
	for j in range(1,6):
		for i in range(1,180):
			kit.servo[j].angle = 90
			time.sleep(0.03)
		for i in range(180,90):
			kit.servo[j].angle = 90
			time.sleep(0.03)



