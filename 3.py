# Area of triangle = (base * height)/2
# base = float(input("Enter the base of triangle:"))
# height = float(input("Enter the height of triangle:"))
# area = (base * height)/2
# print("Area of the triangle:",area)

# Program to find area of triangle and get a number from the user and find square of
# that number.Add with area of triangle and display to the user.
base = float(input("Enter the base of triangle:"))
height = float(input("Enter the height of triangle:"))
number = int(input("Enter the number:"))
area = (base * height)/2
square = number ** 2
result = round(area + square,2)
print("Result of square and area:",result)