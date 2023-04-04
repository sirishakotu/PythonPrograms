# Dictionary

# a = {}
# b = dict()
# print(type(a))
# print(b)

# dict_1 = {1:"Siri",2:"Lakshmi","Niha":1234,(1,2):5547}
# print(dict_1["Niha"])
# print(dict_1.get(1))
# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items())
# dict_1.pop("Niha")
# print(dict_1)

# dict_1.update({2:"Rithwik"})
# print(dict_1)

# # Nested dict

# new = {
#     'a':1,
#     'b':2,
#     'c':{3:4,5:6,7:8}
# }
# print(new.get('c').get(5))
# print(new['c'][7])

# print({1:"Python",2:"Java",3:"PowerBI","data":12334}.items())

# for key,value in {1:"Python",2:"Java",3:"PowerBI","data":12334}.items():
#     print(key,end = " ")
#     print(value)

# users_list = {"Siri":1432,"Bunny":2345,"Sunny":1542,"Niha":7894}
# user_name = input("Enter the name:")
# if user_name in users_list:
#     print("Yes")
# else:
#     print("No")


### Tuples

# sai = ()
# s = tuple()
# print(type(sai))
# print(s)

# a = (10,20,30,40,50)
# print(a[1])
# print(a.add(60)) # not possible
# a.add(60)
# print(a)
# print(len(a))
# print(max(a))
# print(min(a))
# print(sum(a))

# t1 = (1,2,3,4,5)
# t2 = (6,7,8,9)
# # print(t1+t2)
# l = []
# for i,j in zip(t1,t2):
#     l.append(i+j)
# print(l)

# t1 = (1,2,3,4,5)
# print(t1 * 5) # repitition
# print(20 in t1)
# print(20 not in t1)

# t1 = (1,2,3)
# t2 = (1,2,3)
# print(t1 is t2)

# total = 0
# for i in (10,20,30,40,50):
#     total += i
# print(total)

# c = ("     this is strip    ")
# print(c.rstrip())

# d = print("hi")
# print(d)

# rows = int(input("Enter the rows:"))
# for i in range(rows + 1,0,-1):
#     for j in range(0,i-1):
#         print("*",end = " ")
#     print(" ")