#program to find the euclidean distance of two points.
import math

f1=float(input("enter the ecludian vale at first point"))
s1=float(input("enter the ecludian vale at first point"))
f2=float(input("enter the ecludian value at second point"))
s2=float(input("enter the ecludian value at second point"))
a=f2-f1
b=s2-s1
a= a*a
b=b*b
c=a+b
d=math.sqrt(c)
print("the root is",d)