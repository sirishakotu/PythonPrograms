## Challenge Day 1 ##

# 1. Program to check whether the number is positive or negative or zero

'''
if a number is greater than 0 ==> Positive Number
if a number is less than 0 ==> Negative number

'''

# number = int(input("Enter the number:"))
# if number > 0:
#     print("The given number",number,"is Positive")
# elif number < 0:
#     print("The given number",number,"is Negative")
# else:
#     print("The given number is Zero")

'''
input: 10 23 -85 0

output:
The given number 10 is Positive
The given number 23 is Positive
The given number -85 is Negative
The given number is Zero
'''

# 2. Check the input number is odd or even

'''
For even => it is divisible by 2 that is %2 == 0
For odd => it is not divisible by 2 that is %2 != 0

'''

# number = int(input("Enter the number:"))
# if number % 2 == 0:
#     print("The given number",number,"is Even")
# else:
#     print("The given number",number,"is Odd")

'''
Input: 32 21
Output:
The given number 32 is Even
The given number 21 is Odd
'''

# 3. Program to find Leap year or not

'''
1. If a year is evenly divisible by 4 means having no remainder then go to next step. 
   If it is not divisible by 4. It is not a leap year.
2. If a year is divisible by 4, but not by 100. Leap year
    If a year is divisible by both 4 and 100, go to next step.
3. If a year is divisible by 100, but not by 400.
   If a year is divisible by both, then it is a leap year.
'''
def check_leap(year):
    if ((year % 400 == 0) or (year % 100 !=0)and (year % 4 == 0)):
        print("Given year",year,"is Leap year")
    else:
        print("Given year",year,"is not Leap year")

year = int(input("Enter the year:"))
check_leap(year)


'''
Input: 1700
Given year 1700 is not Leap year
Input:2012
Given year 2012 is Leap year
Input:1900
Given year 1900 is not Leap year
Input:2012
Given year 2012 is Leap year
'''