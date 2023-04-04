# Task 8 (Control Statements)

'''

a = 20
b = 30
c = 50
if a > b and a > c:
    largest = a
elif b > c and b > a:
    largest = b
else:
    largest = c
print(largest)





a = int(input("Enter the age:"))
if a > 18:
    print("You can drive")
else:
    print("You cannot drive")



x = int(input("Enter the Value:"))
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

'''
'''
if False:
    print("This is outer if")
    if False:
        print("This is inner if")
    else:
        print("This is inner else")
else:
    print("This is outer else")

'''
# Short hand if
# a= 2
# b =3
# if a>b:print(a)
# print(a) if a > b else print(b)

'''
username = "Siri"
password = "1432"
user = input()
passw = input()
if user == username and passw == password:
    print("Login Success")
else:
    print("Invalid Login")

'''


