#!/usr/bin/python
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
J=[]
K=[]
for i in adhoc:
	if i>5:
		print(i)
		J.append(i)
	elif i<=2:
		print(i)
		K.append(i)
print("List of values greater than 5",J)
print("List of values less than or equals to 2",K)
		