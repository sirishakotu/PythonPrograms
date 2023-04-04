# def func(a,b):
#     a += 2
#     b += "1"

# a = 2
# b = "3"
# func(a,b)
# print(f'{a}{b}')

# 1. Print multiplication table form 1 to 10

'''
1  2 3 4 5 6 7 8 9 10 		
2  4 6 8 10 12 14 16 18 20 		
3  6 9 12 15 18 21 24 27 30 		
4  8 12 16 20 24 28 32 36 40 		
5  10 15 20 25 30 35 40 45 50 		
6  12 18 24 30 36 42 48 54 60 		
7  14 21 28 35 42 49 56 63 70 		
8  16 24 32 40 48 56 64 72 80 		
9  18 27 36 45 54 63 72 81 90 		
10 20 30 40 50 60 70 80 90 100 
'''

# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j,end = " ")
#     print()

# 2. Print downward Half-Pyramid Pattern with Star

'''
* * * * *  
* * * *  
* * *  
* *  
*
'''

# for i in range(6,0,-1):
#     for j in range(0,i-1):
#         print("*",end = " ")
#     print()

# 3.  Write a function 
# called exponent(base, exp) that returns an int value of base raises to the power of exp.

'''
base = 5
exponent = 4

5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)
'''

# def exponent(base,exp):
#     return base ** exp

# base = int(input("Enter the base number:"))
# exp = int(input("Enter the exp number:"))
# answer = exponent(base,exp)
# print("{} raises to the power of {}".format(base,exp),":",answer)

# 4.  Accept numbers from a user

'''
Write a program to accept two numbers from the user and calculate multiplication

'''

# number_1 = int(input("Enter the first number:"))
# number_2 = int(input("Enter the second number:"))
# print("Multiplication of two numbers are:",number_1*number_2)

# 5. Display three string “Name”, “Is”, “James” as “Name**Is**James”

# str_1 = input("Enter the string 1:")
# str_2 = input("Enter the string 2:")
# str_3 = input("Enter the string 3:")
# print(str_1+"**"+str_2+"**"+str_3)

# 6. Convert Decimal number to octal using print() output formatting

'''
num = 8
The octal number of decimal number 8 is 10
'''

# num = int(input("Enter the number:"))
# print("%o"% num)    # Format to convert into octal number

# 7. Display float number with 2 decimal places using print()

# float_number = float(input("Enter the float number:"))
# print(round(float_number,2))

# 8.  Accept a list of 5 float numbers as an input from the user

# list_float = []
# for i in range(5):
#     a = float(input("Enter the float number:"))
#     list_float.append(a)
# print(list_float)

# 9. Accept any three string from one input() call

# string_input = input().split()
# print("String1:",string_input[0])
# print("String2:",string_input[1])
# print("String3:",string_input[2])

# 10. Format variables using a string.format() method.

'''
Write a program to use string.format() 
method to format the following three variables as per the expected output

'''
# total_money = 10000
# quantity = 3
# price = 450
# statement = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars."
# print(statement.format(total_money,quantity,price))

#### Python if else, for loop, and range() Exercises

# 1. Print First 10 natural numbers using while loop

# x = 1
# while x <= 10:
#     print(x)
#     x += 1

# 2. Print the following pattern
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()

# 3. Calculate the sum of all numbers from 1 to a given number

'''
Write a program to accept a number from a user and calculate 
the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
'''
# user_number = int(input("Enter the number n:"))
# total_sum = 0
# for i in range(1,user_number+1):
#     total_sum += i
# print("Total sum from 1 to given number",user_number,"is",total_sum)

# 4. Write a program to print multiplication table of a given number

'''
2
4
6
8
10
12
14
16
18
20

'''

# num = int(input("Enter the number:"))
# for i in range(1,11):
#     print(num*i)




