age=int(input("Enter The Age:"))
if age>=0 and age<=12:
    print("child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("adult")
else :
    print("senior")