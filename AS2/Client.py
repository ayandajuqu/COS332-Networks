#!/usr/bin/env python3 
import socket 
import socket

adrs=('localhost', 55555)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServer:
    try:
        socketServer.connect(adrs)
        print("Connected to port 55555")
    except Exception as e:
        print("Failed to connect to port 55555" + e)

print("CONNECTION CLOSED")