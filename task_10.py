# Empty list
# a = []
'''
a = list()
print(a)
print(type(a))



a = [1,2.2,"Siri",True]
print(a[1])
a[1] = 55
print(a[1])

'''
'''
a = [1,2.2,35,4,"Niha",True,"Rithwik",False,54,25]
print(a[:5])
print(a[0:7:2])
print(a[::-2])



# List methods in Python

#variable.method()

a = [1,2,3.2,34,True,"Siri",False,123]
a.append(35)
print(a)
a.extend(["Ranga","Siri"])
print(a)

v = a.copy()
print(v)
a.append(154)
print(a)

'''

a = [1,2,3.2,2,2,3,3,34,True,"Siri",False,123]
# a.clear()
# print(a.count(3))
# print(a.count(2))
# print(len(a))
# print(a.index("Siri"))
'''
a.insert(1,"Ranga")
print(a)
a[2] = 25
print(a)
a.pop(0)
a.remove(True)
print(a)


a.reverse()
print(a)

'''

# a = [3,1,23,43,12,11,45,33]
# a.sort()
# a.sort(reverse = True)
# print(a)

#find indexes of all same numbers

'''

l = [1,2,2,3,3,4,5,6,7,88,9,3,2,88,78,9,2,2]
for i in range(len(l)):
    if l[i] == 3:
        print(i)

l = [1,2,2,3,3,4,5,6,7,88,9,3,2,88,78,9,2,2]
for i in range(len(l)):
    if l[i] == 88:
        l[i] = 78
print(l)

'''

## List Comprehension

## Ex:1
# print(["Even" if i%2 == 0 else "Odd" for i in range(1,20)])

## Ex:2
# print([num**2 for num in [1,2,3,4,5,6,7,8,9]])

## Ex: 3
# Create a list of only first letter in list of words
# print([i[0] for i in ["Siri","Ranga","Bunny","Niha"]])

## Ex:4

# Create a list of positive numbers 
# print([num  for num in [-1,5,-3,12,15,-36,-45,-8,13,18] if num>0])

# Normal way
'''
list_1 = [-1,5,-3,12,15,-36,-45,-8,13,18]
for num in list_1:
    if num > 0:
        print(num,end = " ")

'''

#Membership operator (not in,in)
# v = [1,5,12,8,45,87,2,3,32]
# print(-10 not in v)
# print(-10 in v)

# How to remove multiple elements using list comprehension

# num = [1,2,3,4,5,6,6,6,7,7,7,8,8,8,9,9,9,9]
# num_to_remove = [6,9]
# pl = [i for i in num if i not in num_to_remove]
# print(pl)

# l=[1,1,24,3,435,53,435,1,2,321,131,1]
# c = []
# [c.append(i) if l[i] == 1 else " " for i in range(len(l))]
# print(c)