#Implement a python take email id as input and check its validity using regular expressions.
import re
email=input("Enter your email id")
if re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email):
	print("VALID EMAIL ID")
else:
	print("INVALID EMAIL ID")