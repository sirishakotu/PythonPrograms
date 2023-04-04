# Practice on OOPS,class,__init__,self

# class(template)

# class Siri(): ## Class declaration
#     def class_fun(self):
#         print("This is first class example")

# Obj=Siri()
# Obj.class_fun() 

# class Rithwik:
#     def niha_obj(self):
#         print("This is second class example")

# niha = Rithwik()
# niha.niha_obj()

# class Shiva():
#     a = 10
#     def inner(self):
#         print("This is third example")

# ranga = Shiva()
# print(ranga.a)
# ranga.inner()

# class Naveen():
#     a = 10
#     def display(self):
#         print(self.a)

# ram = Naveen()
# syam = Naveen()
# ram.display()
# syam.display()


# class Sirisha():
#     def __init__(self,a,b,c,d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#     def Test(self):
#         print(self.a,self.b,self.c,self.d)

# niha = Sirisha(10,20,30,40)
# niha.Test() 


class Bike():
    def __init__(self,name,cc,color,price,mileage):
        self.a = name
        self.b = cc
        self.c = color
        self.d = price
        self.e = mileage
    def Bike_Details(self):
        print("Bike Name:",self.a)
        print("Bike CC:",self.b)
        print("Bike Color:",self.c)
        print("Bike Price:",self.d)
        print("Bike Mileage:",self.e)

bike_name = input("Enter the bike name:")
bike_cc = input("Enter the bike CC:")
bike_color = input("Enter the bike color:")
bike_price = input("Enter the bike price:")
bike_mileage = input("Enter the bike mileage:")

Bike_obj = Bike(bike_name,bike_cc,bike_color,bike_price,bike_mileage)
Bike_obj.Bike_Details()
