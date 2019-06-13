#!/usr/bin/python
import  socket 
recv_ip="192.168.174.142"
recv_port=4647
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
i=0
while i!=1:
	msg=raw_input("plz  enter your message :   ")  
	if len(msg)>150:
		print("------plz send message in limit of 150 character-------")
	else:
		s.sendto(msg,(recv_ip,recv_port)) 
		print(s.recvfrom(150))
		i=int(input("Do you want to continue this chat::\nif yes then press 0\n 1 for continue"))
		if i==1:
			s.sendto('$',(recv_ip,recv_port))
			print("thank you!! ")
			s.close()
			break

