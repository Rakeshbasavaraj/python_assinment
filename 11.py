#progm to find area,square,triangle
def area(b):
	c=float(3.14*radius*radius)
	return c
def triangle(x,y,z):
	c=float(x*y*z)
	return c
def square(b):
	c=float(b*b)
	return c

radius=int(input('enter the value of radius'))
b=area(radius)
print(b)
x=int(input("enter the vale of triale x"))
y=int(input("enter the vale of triale y"))
z=int(input("enter the vale of triale z"))
b=triangle(x,y,z)
print(b)
s=int(input("enter the number for squar"))
b=square(s)
print(b)
