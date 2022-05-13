from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

import spidev
import time

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50

spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 7629

"""
PCA
Brushless:
- front left  -> 0
- back left   -> 2
- front right -> 4
- back right  -> 6
- top left    -> 8
- top right   -> 10

Servo:
- claw        -> 12
- rotate      -> 13
"""

#Initialization of T200 motors
pca.channels[0].duty_cycle = 0x1333
time.sleep(0.01)
pca.channels[2].duty_cycle = 0x1333
time.sleep(0.01)
pca.channels[4].duty_cycle = 0x1333
time.sleep(0.01)
pca.channels[6].duty_cycle = 0x1333
time.sleep(0.01)
pca.channels[8].duty_cycle = 0x1333
time.sleep(0.01)
pca.channels[10].duty_cycle = 0x1333
time.sleep(7)

while(1):
    val_front = 0x1148
    val_back  = 0x151F
    pca.channels[0].duty_cycle = val_front
    time.sleep(0.01)
    pca.channels[2].duty_cycle = val_back
    time.sleep(0.01)
    pca.channels[4].duty_cycle = val_front
    time.sleep(0.01)
    pca.channels[6].duty_cycle = val_back
    time.sleep(0.01)
    
    
    spi.writebytes([0x31])
    time.sleep(0.1)
    high=spi.readbytes(1)
    time.sleep(0.1)
    print('hig:',hex(high[0]))

    spi.writebytes([0x32])
    time.sleep(0.1)
    low=spi.readbytes(1)
    print('low:',hex(low[0]))

    res = (high[0] << 8) | low[0]

    print('total:',float(res))
    print()
    print()

    time.sleep(0.1)



