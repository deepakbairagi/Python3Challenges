#!/usr/bin/python
import socket
recv_ip="127.0.0.1"
recv_port=4647
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))
while 1<2:
	data=s.recvfrom(150)
	if data[0]=='$':
		print("connection terminated")
		s.close()
		break
	else:
		
		print("message received from sender::",data[0])
		print("sender IP + socket::",data[1])
		reply=raw_input("enter your reply here:-")
        	if len(reply) > 150:
			print("plz send reply in 150 characters")
		else:
			s.sendto(reply,data[1])

