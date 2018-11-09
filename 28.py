# progam to convert the input string to inverse case (upper->lower, lower->upper)
str=input("enter the string")
var=""
for i in str:
	if  ord(i) >= 65 and ord(i) <= 90:
		x = ord(i)+32
		y = chr (x)
		var= var + y
	elif ord(i) >= 97 and ord(i)<=122:
		x = ord(i) - 32
		y = chr (x)
		var= var + y
print(var)





