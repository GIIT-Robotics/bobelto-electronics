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
for j in range(1,7):
    for i in range(1,90):
        kit.servo[j].angle = 91-i
        time.sleep(0.03)
    for i in range(1,180):
        kit.servo[j].angle = i
        time.sleep(0.03)
    for i in range(1,90):
        kit.servo[j].angle = 181-i
        time.sleep(0.03)

kit.servo[1].angle = 90
kit.servo[2].angle = 90
kit.servo[3].angle = 90
kit.servo[4].angle = 90
kit.servo[5].angle = 90
kit.servo[6].angle = 90
