#program with lamda functions, for finding the area of circle, triangle, square.
def function(value, x,y):
    return {
        'a': lambda x: x+y,
        'b': lambda x: x*y,
        'c': lambda x: x-y,
        'd': lambda x: x/y
    }.get(value)(x)

# take user input
print("enter a for ADD")
print("enter b for MUL")
print("enter c for SUB")
print("enter d for DIV")
choice = input('enter your choic: ')

print('The result is : ', function(choice, 4, 2))
