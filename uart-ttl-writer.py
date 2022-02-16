
from machine import UART
import time
uart = UART(2, 115200)  
uart.init(115200, bits=8, parity=None, stop=1)

while True:
	d = input("write: ")
	if d != '':
		uart.write(f'{d}\r\n')
	time.sleep(3)
	str(uart.read().decode()).replace("\r\n", " ").replace('\x1b',' ').replace('[1;34m', '').replace('[1;36m', '').replace('[0m', '').replace('[0;0m','').replace('[1;32m', '').replace(d, '')
	
















