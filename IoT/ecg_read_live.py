import serial
import datetime

arduino_port = "COM3"
baud = 9600
samples = 100

print_labels = False

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port : " + arduino_port)

print("Created File")

line = 0

fileName = "analog-data-inf.csv"
file = open(fileName, "w")
file.write("Timestamp,ECG_Value\n")
while 1:
    
    print("Line" + str(line) + ": writing...")
    getData = str(ser.readline())
    data = getData[0:][:-2]
    data = data.split('\'')
    data = data[1]
    data = data.split('\\')
    data = data[0]
    print(data)

    
    now = datetime.datetime.now()
    

    file.write(now.strftime("%H:%M:%S") +","+ data + "\n")
    line = line + 1

print("Data collection complete !")
