#!/usr/bin/env python3 

#Emmanuella Birato u19322594
#Ayanda Juqu
import socket 
import telnetlib

def main():
        adrs=('localhost', 55555)
        with telnetlib.Telnet(adrs[0], adrs[1]) as telnetClient:
                try:
                        while True:
                                question = telnetClient.read_until(b'\n').decode().strip()
                                print(question)

                                usrResp=input("Your answer: ")
                                telnetClient.write(usrResp.encode() + b'\n')

                                serverResp = telnetClient.read_until(b'\n').decode().strip()
                                print(serverResp)

                                if serverResp.lower().startswith('do you want to continue?'):
                                        cont = input("Do you want to continue? (yes/no): ")
                                        telnetClient.write(cont.encode() + b'\n')
                                        if cont.lower() != 'yes':
                                                break
                                
                                else:
                                        break
                except EOFError:
                        print("Failed to connect to port 55555")

        print("CONNECTION CLOSED")