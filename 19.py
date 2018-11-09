#adding number using argv
import sys

def main(argv):

	if(len(argv) >= 3):
		try:
			print("Sum is ", (int(argv[0]) + int(argv[1]) + int(argv [2])))
		except:
			print("you need to enter three num1 num2 num3 ")

	else:
		print(" you need to enter three numbers num1 num2 num3")

	return

if __name__=="__main__":
	
	main(sys.argv[1:])
