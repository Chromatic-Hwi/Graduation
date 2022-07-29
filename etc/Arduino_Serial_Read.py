import serial

port = "/dev/ttyACM0"
brate = 9600
cdm = "power"

serial = serial.Serial(port, baudrate=brate, timeout=None)
print(serial.name,"\n")

#serial.write(cdm.encode())

while True:
    line = str(serial.readline())[2:-5]
    IValue=line[9:14]
    WValue=line[-7:-1]
    #print(line)
    print(IValue, WValue, "\n")