from datetime import datetime

name=input("Enter your name:")

lists="""
**********************************
==================================
Butter    Rs 180  /  kg
Peanuts   Rs 160  /  kg
Jam       Rs 135  /  kg
Olive oil Rs 1800 /  Liter
Maggie    Rs 75   /  each
Milk      Rs 35   /  each
===================================
***********************************

 """
 # Declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist= []
qlist=[]
plist=[]

# rates per items
items={'Butter':180,
'Peanuts':160,
'Jam':135,
'Olive oil':1800,
'Maggie':75,
'Milk':35}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
     inp1=int(input("if you want to buy press 1 or 2 for exit:"))
     if inp1==2:
        break
     if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
     if  item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
     else:
        
            print("Sorry you entered item is not available")
else:
     print("you entered wrong number")

input=input("can i bill the items yes or no:")
if input=='yes':
        pass
        if finalamount!=0:
            print(25*"=","MANA DUKANAM",25*"=")
            print(28*" ","Mumbai")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"=")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')

        for i in range(len(pricelist)):
            print(i,8*'  ',8*'  ',ilist[i],3*'  ',qlist[i],plist[i])
        print(75*"-")
        print(50*" ",'TotalAmount:','Rs',totalprice)
        print("gst amount",50*" ",'Rs',gst)
        print(75*"-")
        print(50*" ",'TotalAmount:','Rs','finalamount')
        print(75*"-")
        print(50*" ","Thank you for Visiting")
        print(75*"-")



    






