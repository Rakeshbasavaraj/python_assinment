str = input ('Enter the string ')
var = ""
for i in str:
    if ord(i) >= 97 and ord(i) <= 122:
        x = ord(i) -32
        y = chr (x)
        var= var + y
print(var)