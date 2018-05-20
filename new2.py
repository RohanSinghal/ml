#!/usr/bin/python2

import socket
import time

rec_ip="127.0.0.1"
my_port="8888"

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send to:

while 3>2:
    msg=raw_input("enter message to be send:")
    x.sendto(msg,("127.0.0.1",8888))
    msg.lstrip()
    print x.recvfrom(100)
    #time.sleep(1)
    
    

