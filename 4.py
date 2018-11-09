#check the count of vowels in a given string
vowles=['a','e','i','o','A','E','I','O']
str=input("enter the string")
count=0
for i in str:
	if i in vowles:
		count=count+1
print(count)

