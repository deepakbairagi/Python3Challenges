
#!/usr/bin/python3
x=int(input(("Enter an option from following to execute cat command:\n1.Print the data of a single file\n2.Print data of multiple files\n3.Create a new empty file\n4.Create a file and enter some data\n"))) 
if x==1:
	floc=input("enter name with location:\n")
	myfile=open(floc,"r")
	print(myfile.read())
	myfile.close()
elif x==2:
	loc=[]
	fno=int(input("enter nos. of file to read"))
	for i in range(fno):
		fnloc=input("enter name of file "+str(i)+" with location:\n")
		loc.append(fnloc)
	for lo in loc:
		myfile1=open(lo,"r")
		print(myfile1.read())
		myfile.close()
elif x==3:
	fl=input("enter name of file") 
	myfile=open(fl,"w")
	myfile.close()
elif x==4:
	fl=input("enter name of file which you want to create and write")
	myfile=open(fl,"w")
	print("enter the data to write in file")
	while True:
		data=input()
		if data=='~':
			break
		else:
			myfile.write(data)
	myfile.close()

