#Simple Atm Program

# Enter the Account holder name
name = input("Enter the account holder name:")
print("Welcome to your bank account",name)

total_money = 90000
money = int(input("Enter the amount:"))

def deposit_cash(money):
     a = lambda b,c : b + c
     return a(total_money,money)
def withdraw_cash(money):
     w = lambda b,c : b - c
     return w(total_money,money)
        
option = int(input("Enter your option 1 or 2:"))

if option == 1:
        credit = deposit_cash(money)
        print("Mini Statement:")
        print("Available Balance before credit is",total_money)
        print("Money to be credited is",money)
        print("Total balance after credited is",credit)
elif option == 2:
    if money < total_money:
         draw = withdraw_cash(money)
         print("Mini Statement:")
         print("Available Balance before withdrawal is",total_money)
         print("Money to be drawn is",money)
         print("Total balance after withdrawal is",draw)
    else:
         print("Your account didnot have required cash")    
    
else:
    print("Choose the correct option")