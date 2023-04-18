import serial

serdev = 'COM3'
s = serial.Serial(serdev, 9600)

s.write('loc'.encode('utf-8'))

line = s.readline()
print(line)

s.write('22'.encode('utf-8'))


print("hellow")