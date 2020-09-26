import serial
import time
import csv
import traceback
import datetime
import requests

port = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0'
#port = '/dev/ttyUSB0'
baud = 9600

ser = serial.Serial(port, baud, timeout=1)
ser.flushInput()

print(ser.name)

oldline = []
a = 0
while (a == 0):
    try:
        line = ser.readline()                 # read bytes until line-ending
        line = line.decode('UTF-8','ignore')  # convert to string
        #line = line.rstrip('\r\n')            # remove line-ending characters
        
        split_line = line.splitlines()
        
        if oldline != split_line:      
            with open("test_data.csv","a") as f:
                for item in split_line:
                    print (item)
                    x = datetime.datetime.now()
                    
                    # You can write to a text/CSV file.
                    #writer = csv.writer(f,delimiter=",")
                    #writer.writerow([x.strftime("%c"), item])
                    
                    # #You can also send the data to a website/database for processing elsewhere
                    payload = {'pager_message': item}
                    r = requests.post("https://yoursever.com/file_to_post_to.php", data=payload)
                    
                    #Show what the server responded with
                    print(r.text)
                
        oldline = split_line
        
    
    except Exception:
        traceback.print_exc()
        print("exiting")
        #print("Keyboard Interrupt")
        #break doesn't quit now on error.
    
