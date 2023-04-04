# Functions

# def fn_name():
#     print("This is function")
# fn_name()

# def fn_1(a,b):
#     print("hi",a,b)
# fn_1("Python",52)

# def fn_2(*a):
#     print(a)
# fn_2(1,2,33,4,5,66,7,8)

'''
* arbitary argument --> tuple
** kwargs --> dict
'''
# def fn_2(**a):
#     print(a)
# fn_2(a=1,b=2)

### Advance Functions

# Lamda Functions

# x = lambda a,b,c : a + b + c
# print(x(56,28,17))

# y = lambda a : a * 3
# print(y("Python "))
# print(y(5))

# l1= [23,1,45,54,21,15]
# l2 = []
# for i in l1:
#     a = lambda x : x + 1
#     l2.append(a(i))
# print(l2)

# Filter Functions

# ages = [12,18,25,11,45,69]
# def myFunc(x):
#     if x >= 18:
#         return True
#     else:
#         return False
# adults= filter(myFunc,ages)
# print(list(adults))

### Generator Functions

# def myGen_gn():
#     yield 1
#     yield 2
#     yield 3
# x = myGen_gn()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

### Map Functions

# def calAdd(n):
#     return n + n
# numb = [1,2,3,4,5]
# a = list(map(calAdd,numb))
# print(a)

# def add(*a):
#     return a+a
# numb = [4,2,5,7,1,6]
# b = add(numb)
# print(b)

# from functools import reduce
# d=reduce(lambda a,b:a+b,[24,54,75,98,12])
# print(d)

# def even_fn(x):
#     if x % 2==0:
#         print(x)

# numb = [45,22,12,58,96,35,21,49]
# even = filter(lambda x :x%2 == 0,numb)
# print(list(even))
# odd = filter(lambda x:x%2 != 0,numb)
# print(list(odd))

# numb = [2,3,4,5,6,7]
# square = map(lambda x :x**2 ,numb)
# print(list(square))

# def outer():
#     print("Outer")
#     def inner():
#         print("Inner")
#     inner()
# outer()

g=[2,325,23,546,363,6]
print(list(filter(lambda x: x>23,g)))
