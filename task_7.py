# Largest of 3 numbers

a = int(input("Enter the value a:"))
b = int(input("Enter the value b:"))
c = int(input("Enter the value c:"))

if a >= b and a >=c:
    print("Largest number is a:",a)
elif b >= c and b >= a:
    print("Largest number is b:",b)
else:
    print("Largest number is c:",c)
