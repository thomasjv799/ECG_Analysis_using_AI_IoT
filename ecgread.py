import serial
import datetime

arduino_port = "COM6"
baud = 9600

samples = 100
chunks = 10
print_labels = False

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port : " + arduino_port)

print("Created File")
x=1
line = 0
while(x <= chunks):
    fileName = "analog-data"+str(x)+".csv"
    file = open(fileName, "w")
    while line <= samples:
        if(print_labels):
            if line == 0:
                print("ECG Value")
            else:
               print("Line" + str(line) + ": writing...")
        getData = str(ser.readline())
        data = getData[0:][:-2]
        data=data.split('\'')
        data = data[1]
        data = data.split('\\')
        data = data[0]
        print(data)

        file = open(fileName, "a")
        now = datetime.datetime.now()

        file.write(now.strftime("%H:%M:%S.%f") +","+ data + "\n")
        line = line +1
    x=x+1
    line = 0

print("Data collection complete !")
