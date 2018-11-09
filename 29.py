# In a given list find the total number of odd numbers, even numbers and their respetive sum and average.
list=[1,2,4,3,5]
es=0
os=0
en=0
on=0
for i in list:
	if (i%2==0):
		es=es+i
		en=en+1
		
	else:
		os=os+i
		on=on+1
		
print("sum",es)
print("avg",es/en)
print("sum",os)
print("avg",os/on)