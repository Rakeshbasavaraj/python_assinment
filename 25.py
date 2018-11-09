#25. Implement a function to count the number of vowels present in the file. 
f=open('25.txt',"r")
fp=f.read()
print("the volwes are:\n",fp)
count=0
for line in fp:
	for ch in line:
		if ch in ('a','e','i','o','u','A','E','I','O','U'):
			count=count+1
print("Number of vowels in file is:",count)