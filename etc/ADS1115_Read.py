import time
import Adafruit_ADS1x15
from datetime import datetime

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 16

while True:
    value_sum=0
    
    for _ in range(100):
        value = adc.read_adc_difference(0, gain=GAIN)*1.1
        
        if value<145:
            value=0
            
        value_sum+=value
        time.sleep(0.01)
        
    value_avg=value_sum/100
    value_avg = int(round(value_avg, 0))
    
    if value_avg<145:
        value_avg=0
        
    print(value_avg)
    
    """
    date_milli = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    value = adc.read_adc_difference(0, gain=GAIN)
    print(value, "  |  ", date_milli)
    """
