#program to create a list with two tuple of fruits and vegetables. Access fruits separately and vegetables separately. 
conv=list()
fru = tuple(("pineappl", "supota", "mango"))
veg= tuple(("ladylies finger", "califlower", "carrot"))
conv.append(fru)
conv.append(veg)
print(conv)
for i in conv[0]:
	print(i)
for i in conv[1]:
	print(i)
