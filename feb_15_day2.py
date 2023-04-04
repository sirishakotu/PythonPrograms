# 1. Python program to interchange first and last elements in a list

'''
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

'''


# try: print(1)
# except:print(2)
# finally:print(3)

# while x <= 18:
#     x = x + 3
# print(x)

# given_list = [12, 35, 9, 56, 24]
# given_list = [1,2,3]
# a = given_list[0]
# given_list[0] = given_list[-1]
# given_list[-1] = a 

# print(given_list)


# 2. Write a Program to extract each digit from an integer in the reverse order.

'''
If the given int is 7536, the output shall be “6 3 5 7“, 
with a space separating the digits.

'''
# given_int = int(input("Enter the input of integer:"))
# int_str = str(given_int)
# rev_str = int_str[::-1]
# for each in rev_str:
#     print(each,end = " ")


# 3. Calculate income tax for the given income by adhering to the below rules

'''
Taxable Income	Rate (in %)

First $10,000	0
Next $10,000	10
The remaining	20

'''
'''
suppose the taxable income is 45000 the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000.
'''
# income = int(input("Enter the income:"))
# tax = 0
# if income <= 10000:
#     tax = 0
# elif income <= 20000:
#     x = income - 10000
#     tax = x *(10/100)
# else:
#     tax = 0
#     tax = 10000 * (10/100)
#     x = income - 20000
#     tax += x * (20/100)
# print(int(tax))

 
