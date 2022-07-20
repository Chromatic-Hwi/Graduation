import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
                
ads = ADS.ADS1115(i2c)
ads.gain = 1

channel = AnalogIn(ads, ADS.P0)

while True:
    Amp=channel.value/100
    Volt=220
    Watt=Amp*Volt
    #print("%0.3f Watt"%Watt)
    print(channel.value, "|", channel.voltage)
    time.sleep(1)