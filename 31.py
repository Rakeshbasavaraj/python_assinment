# program to check the elements of a list is a palindrome or not.
n=int(input("Enter number:"))
temp=n
rem=0
while(n>0):
    div=n%10
    rem=rem*10+div
    n=n//10
if(temp==rem):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")