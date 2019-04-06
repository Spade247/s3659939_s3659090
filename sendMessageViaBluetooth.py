import sys
import bluetooth

bd_addr = '[48:3B:38:60:97:0B]'
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))
sock.send("2".encode())