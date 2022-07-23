import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")

pyfirmata.util.Iterator(board).start()
board.analog[0].enable_reporting()

while True:
    value = board.analog[0].read()
    print(value)
    time.sleep(0.5)