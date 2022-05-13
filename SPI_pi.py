import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629
# Repeatedly switch a MCP4151 digital pot off then on
while True:
    spi.writebytes([0x21])
    time.sleep(0.1)
    high=spi.readbytes(1)
    time.sleep(0.1)
    print('hig:',hex(high[0]))

    spi.writebytes([0x22])
    time.sleep(0.1)
    low=spi.readbytes(1)
    print('low:',hex(low[0]))

    res = (high[0] << 8) | low[0]

    print('total:',(float(res)+20)/340)
    print()
    print()

    time.sleep(0.1)
