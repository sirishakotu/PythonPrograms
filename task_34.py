#### OOPS Object  oriented programming ###

# class Pramod():# class defination
#     # constructors
#     # functions
#     # variables


# attribute (variable) data members
'''
age=20 
color='blue'
'''

# method(behaviour) or functions , member functions
'''
eat() 
sleep()
'''

# self keyword
'''
we can access the attributes and methods of the class(current class only)
'''

# # # __init__

# # '''
# # Constructors are generally used for instantiating an object. 
# # The task of constructors is to initialize(assign values)
# # to the data members of the class when an object of the class 
# # is created.
# # In Python the __init__() method is called the constructor
# # and is always called when an object is created

# # does'nt support multiple constructor
# # '''


# class Rithwik():
#     def __init__(self,a,b,c,d):
#         self.a=a 
#         self.b=b
#         self.c=c
#         self.d=d

#     def Test(self):
#         print(self.a,self.b,self.c,self.d)

# obj=Rithwik(1,2,3,4)
# obj.Test()



# class Prakash():
#     def __init__(self,a,b,c):
#         self.ff=a
#         self.vv=b
#         self.dd=c
#         print(a)
#     def Output(self):
#         print(self.ff,self.vv,self.dd)
# p=Prakash(1,2,3)
# p.Output()


# class Mobiles():
#     def __init__(self,Mobile_name,Mobile_Ram,Mobile_battery,Mobile_Price):
#         self.a=Mobile_name
#         self.c=Mobile_Ram
#         self.d=Mobile_battery
#         self.e=Mobile_Price

#     def Mobile_Data(self):
#         print("Mobile Name:",self.a)
#         print("Mobile Ram:",self.c)
#         print("Mobile Battery:",self.d)
#         print("Mobile Price:",self.e)

# name=input("Enter the Mobile Name:")
# ram=input("Enter the Mobile Ram:")
# bat=input("Enter the Mobile Battery:")
# Price=float(input("Enter the Mobile Price:"))

# Mobile_obj=Mobiles(name,ram,bat,Price)
# Mobile_obj.Mobile_Data()




        # # inheritance # #

# # single (parent child)
# # multiple(two are more base classes)
# # multilevel(tree)
# # hierarchical(one base with sibiling childs)


## Single inheritance ##

# class Parent:
#     def output(self):
#         print("This is Parent class")
# class Child(Parent):
#     def outputChild(self):
#         print("This is Child class")

# i = Child()
# i.output()
# i.outputChild()

## Multiple - 2 or more base classes ##

# class Father:
#     def output(self):
#         print("This is Father class")
# class Mother:
#     def outputM(self):
#         print("This is Mother class")
# class Child(Father,Mother):
#     def outputChild(self):
#         print("This is Child class")

# a = Child()
# a.output()
# a.outputM()
# a.outputChild()

### Hierarchial Inheritance   ####

# class Grandfather:
#     def output(self):
#         print("This is GrandFather class")
# class Father(Grandfather):
#     def outputFather(self):
#         print("This is Father class")
# class Child(Father):
#     def outputChild(self):
#         print("This is Child class")
# siri = Child()
# siri.output()
# siri.outputFather()
# siri.outputChild()

#### Multilevel inheritance ####

# class Father:
#     def op(self):
#         print("This is Father class")
# class Child1(Father):
#     def op1(self):
#         print("This is Child1 class")
# class Child2(Father):
#     def op2(self):
#         print("This is Child2 class")
# a = Child1()
# a.op1()
# a.op()
# b = Child2()
# b.op2()
# b.op()


# class A:
#     def op(self):
#         print("This is A")
# class B:
#     def op1(self):
#         print("This is B")
# class C:
#     def op2(self):
#         print("This is C")
# class D(A,B,C):
#     def op3(self):
#         print("This is D")

# a = D()
# a.op()
# a.op1()
# a.op2()
# a.op3()

'''
Output:
This is A
This is B
This is C
This is D
'''


### Polymorphism -- many forms
### 1. Method Overloading 2. Method Overriding

# def numbers(a,b):
#     print(a+b)
# numbers(3,8)
# numbers("Lakshmi","Siri")
# numbers([2,3],[5,8])

'''
Output:
11
LakshmiSiri
[2, 3, 5, 8]
'''
# 1. Method Overload

# class A:
#     def op(self,a = 10,b = 20,c = 30,d = 40):
#         print(a,b,c,d)
# obj_A = A()
# obj_A.op(5,10,15,20)
# obj_A.op(6,12)
# obj_A.op(16,24,32)
# obj_A.op()

'''
Output:
5 10 15 20
6 12 30 40
16 24 32 40
10 20 30 40
'''

# 2. Method Overriding

# class A:
#     def op(self):
#         print("This is A")
# class B(A):
#     def op(self):
#         print("This is B")
#         super().op()
# class C(B):
#     def op(self):
#         print("This is C")
#         super().op()
# abc = C()
# abc.op()

'''
Output:
This is C
This is B
This is A
'''


# Encapsulation ==> binding of class (methods and variables(attributes))
# 1. public 
# 2. private __
# 3. protected _


# class Siri:
#     def __init__(self,a):
#         self._y=a
#         print(self._y)
# class Rithwik(Siri):
#     def op1(self):
#         print(self._y)
# class Niha(Rithwik):
#     def op2(self):
#         print("Niha",self._y)
# obj=Niha(22)
# obj.op1()
# obj.op2()

'''
Output:
22
22
Niha 22
'''



