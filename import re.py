import re
a=input("emter the txt:")

x= re.findall("^[a-z]",a)
c= re.findall("$[0-9]",a)
d= re.findall("gmail.com$")
print(x)
print(c)
print(d)
if x:
    print("true")
if c:
    print("yes")
if d:
    print("okay")
else:
    print("false")