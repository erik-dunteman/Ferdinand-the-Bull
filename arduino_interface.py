import serial, time, random
# ser = serial.Serial(port='COM8', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=5, xonxoff=0, rtscts=0)
# try:
#     ser.open()
# except:
#     pass
# i = 1
# while i < 7:
#     if i%3 == 0:
#         print("!")
#         ser.write(b'!')
#     else:
#         print("Non !")
#         ser.write(b'Something')
#     i += 1
#     time.sleep(5)
#     message = ser.read(ser.inWaiting())
#     # message = message.decode()
#     print(message)

# ser.close()

# servo control 15.12.2016
 
# 1) user set servo position in python
# 2) position is sent to arduino
# 3) arduino moves servo to position
# 4) arduino send confirmation message back to python
# 5) message is printed in python console
 
import serial                                           # import serial library
arduino = serial.Serial('COM8', 9600)   # create serial object named arduino
while True:
        positions = [(str(random.randint(0,180))+'\n').encode('utf-8'), 
        (str(random.randint(0,180))+'\n').encode('utf-8'), 
        (str(random.randint(80,120))+'\n').encode('utf-8')]
        time.sleep(1)
        for position in positions:
                arduino.write(position)                          # write position to serial port
        reachedPos = arduino.readline().decode('utf-8')         # read serial port for arduino echo
        print(reachedPos)                               # print arduino echo to console


# print("".join(map(chr, positions)))