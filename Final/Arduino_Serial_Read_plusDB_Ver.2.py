import serial
import MySQLdb

port = "/dev/ttyACM0"
brate = 9600
cdm = "power"

serial = serial.Serial(port, baudrate=brate, timeout=None)

db = MySQLdb.connect("localhost", "hwi", "20191223", "testdb")
curs = db.cursor()

Data_Cycle = {"Sec":100, "Min":6000}
Time="Sec"

while True:
    value_list=[]
    for _ in range(Data_Cycle[Time]):
        try:
            value = float(str(serial.readline())[2:-5])
            value_list.append(value)
        except TypeError:
            pass
        except ValueError:
            pass
    max_value = max(value_list)
    #print(max_value)
    curs.execute("insert into Power (value) values(%f)"%max_value)
    db.commit()