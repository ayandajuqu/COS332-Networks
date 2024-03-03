#!/usr/bin/env python3 
import socket

adrs=('localhost', 55555)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServer:
    socketServer.bind(adrs)
    socketServer.listen()
    print(" server listening on port 55555")

    while True:
        connection, address=socketServer.accept()
        print(" server accepted on client address: "+ address)