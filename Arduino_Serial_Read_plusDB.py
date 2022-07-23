import serial
import MySQLdb

port = "/dev/ttyACM0"
brate = 9600
cdm = "power"

serial = serial.Serial(port, baudrate=brate, timeout=None)
#print(serial.name,"\n")

db = MySQLdb.connect("localhost", "hwi", "20191223", "testdb")
curs = db.cursor()

while True:
    line = str(serial.readline())[2:-5]
    IValue=float(line[9:14])
    WValue=float(line[-7:-1])
    #print(line)
    #curs.execute("INSERT INTO Power (value) VALUES (%f)", WValue)
    print(IValue, WValue, "\n")