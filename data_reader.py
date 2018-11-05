import serial
import time
import csv

port = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0'
#port = '/dev/ttyUSB0'
baud = 9600

ser = serial.Serial(port, baud, timeout=1)
ser.flushInput()

print(ser.name)

oldline = []

while True:
    try:
        #ser_bytes = ser.readline()
        #decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        #print(decoded_bytes)
        
        
        line = ser.readline()                 # read bytes until line-ending
        line = line.decode(encoding='UTF-8')  # convert to string
        #line = line.rstrip('\r\n')            # remove line-ending characters
        
        split_line = line.splitlines()
        
        if oldline != split_line:      
            with open("test_data.csv","a") as f:
                for item in split_line:
                    writer = csv.writer(f,delimiter=",")
                    writer.writerow([time.time(), item])
                
        oldline = split_line
        
    except:
        print("exiting")
        #print("Keyboard Interrupt")
        break
