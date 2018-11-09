import re
def validate(email):
	 return re.match('^[a-zA-Z0-9]*@[a-zA-Z0-9',email)
def main():
	email=input("entet email")
	if validate(email):
		print("no")
	else:
		print("yes")
if __name__=="__main__":
	main()


