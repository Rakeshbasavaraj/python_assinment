
str = input ('Enter the string ')
var = ""
for i in str:
    if  ord(i) >= 65 and ord(i) <= 90:
        x = ord(i) + 32
        y = chr (x)
        var= var + y
print(var)

