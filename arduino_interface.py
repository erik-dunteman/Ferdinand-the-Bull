import serial, time, random
arduino = serial.Serial('COM8', 9600)
while True:
        positions = [(str(random.randint(0,180))+'\n').encode('utf-8'), 
        (str(random.randint(0,180))+'\n').encode('utf-8'), 
        (str(random.randint(80,120))+'\n').encode('utf-8')]
        time.sleep(1)
        for position in positions:
                arduino.write(position)
        reachedPos = arduino.readline().decode('utf-8')
        print(reachedPos)