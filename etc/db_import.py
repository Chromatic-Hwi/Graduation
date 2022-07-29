import serial
import MySQLdb


port = serial.Serial("/dev/ttyACM0", "9600")

db = MySQLdb.connect("localhost", "hwi", "20191223", "testdb")
curs = db.cursor()

while True:
    try:
        serial_data = port.readline()
        curs.excute("INSERT INTO Power (values) VALUES (%f), serial_data")
        db.commit()
        
    except KeyboardInterrupt:
        break
    
port.close()
db.close()