#!/usr/bin/python3
import os
import subprocess
usrlist=[]
i=0
nu=int(input("Plz enter no. of users you want to create"))
while i<nu:
	usr=input("Plz enter user name::")
	if usr.isalpha():
		usrlist.append(usr)
		i+=1
	else:
		print("you can't enter this type of user name")
	
for j in usrlist:
	usrpass="hello"+j
	comm="useradd -p $(openssl passwd -1 "+usrpass+") "+j
	os.system(comm)

 
