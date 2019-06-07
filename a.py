#!/usr/bin/python3
chars=0
lines=0
words=0
ab=open("a.txt","r")
for i in ab:
  chars=chars+1
  if i=='\n':
     lines=lines+1
  elif i==" ":
     words=words+1
print("Number of words in the string:")
print(words)
print("Number of lines in the string:")
print(lines)
print("Number of characters in the string:")
print(chars)
