#!/usr/bin/python3
chars=0
lines=0
words=0
ab=open("a.txt","r")
while True:
	f=ab.read(1)
	if f:
		if f=='\n':
			lines=lines+1 
			words=words+1 	  
		elif f==" ":
			words=words+1
		chars=chars+1
	else:
        	print("file end")
        	break
print("Number of words in the string:")
print(words)
print("Number of lines in the string:")
print(lines)
print("Number of characters in the string:")
print(chars)
ab.close() 
