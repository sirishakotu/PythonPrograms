# Swapping the variables (with temp variable)
# a = input("Enter the variable a:")
# b = input("Enter the variable b:")
# print("Variables before swapping:")
# print("a=" + str(a))
# print("b=" + str(b))
# print("Variables after swapping:")
# temp = a
# a = b
# b = temp
# print("a=" + str(a))
# print("b=" + str(b))


# Swapping the variables (without temp variable)
a = input("Enter the variable a:")
b = input("Enter the variable b:")
print("Variables before swapping:")
print("a=" + str(a))
print("b=" + str(b))
print("Variables after swapping:")
a,b = b,a
print("a=" + str(a))
print("b=" + str(b))