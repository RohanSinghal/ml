#!/usr/bin/python2

import socket

rec_ip="127.0.0.1"
my_port="8888"

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#bind
x.bind(("127.0.0.1",8888))

while True:
	data=x.recvfrom(100)
	data=+data[0].decode()+
	print("data fro client",data)
	s=data.split()
	s=list(set(s))
	leng=len(s)
	for i in range(len):
		find = +str(s[i])+
		count=data.count(find,0,len(data))
		time.sleep(1)
		plt.bar(i+1,count,label=str(s[i]))
	plt.legend()
	plt.xlabel("words")
	plt.ylabel("count")
	plt.show()
