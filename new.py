#!/usr/bin/python2

import socket

rec_ip="127.0.0.1"
my_port="8888"

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#bind
x.bind(("127.0.0.1",8888))

while 4>2:
    data=x.recvfrom(100)
    print "data is:",data[0]
    print "IP of client is:",data[1][0]
    reply=raw_input("enter your reply:")
    x.sendto(reply,data[1])
    reply.lstring()
