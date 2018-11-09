#program to write a line from the console to a file.
import sys

for i in range(1,len(sys.argv)):
	a=sys.argv[i]
	file=open("23.txt","a")
	file.write(a)