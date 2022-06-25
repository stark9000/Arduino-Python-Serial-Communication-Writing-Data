import serial
import time

SERIAL_PORT = serial.Serial('com13', 9600, timeout=0)
time.sleep(2)
print(SERIAL_PORT.name+"is opened !")
print("\n")

while(1):
    print("1 to TURN ON LED & 0 to TURN OFF LED and 2 to quit")
    USER_INPUT = input()
    print("USER Entered :"+USER_INPUT)
    
    if (USER_INPUT == '1'):
        SERIAL_PORT.write(b'1')
        print ("LED ON")
        
    if (USER_INPUT == '0'):
        SERIAL_PORT.write(b'0')    
        print ("LED OFF")
       
    if (USER_INPUT == '2'):
        print ("quitting...")
        exit(0)
