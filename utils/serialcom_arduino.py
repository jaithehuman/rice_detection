# Importing Libraries
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


def start():
    num = input("Write command: ") # Taking input from user
    print("capture") #cap
    time.sleep(1)
    arduino.write(bytes(num, 'utf-8'))
    time.sleep(1)
    for i in range(9):
        print("capture") #cap
        time.sleep(2.04)
    print("done")


start()