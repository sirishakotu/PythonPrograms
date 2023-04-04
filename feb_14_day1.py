# Calculate the multiplication and sum of two numbers
'''
Given two integer numbers 
return their product only if the product is equal to or lower than 1000,
 else return their sum.

'''
# Integer numbers taking from user

# int_1 = int(input("Enter the first integer number:"))
# int_2 = int(input("Enter the second integer number:"))

# product = int_1 * int_2

# if product <= 1000:
#     print("Product of two integers is",product)
# else:
#     total = int_1 + int_2
#     print("Sum of two integers is",total)

# 2. Print the sum of the current number and the previous number

'''
Write a program to iterate the first 10 numbers 
and in each iteration, print the sum of the current and previous number.

'''
# prev_numb = 0


# for i in range(10):
#     print("Previous Number",prev_numb,end = " ")
#     curr_numb = i
#     print("Current Number",curr_numb,end = " ")
#     total = prev_numb + curr_numb
#     print("Sum is",total)
#     prev_numb = curr_numb

# 3.Print characters from a string that are present at an even index number

'''
Write a program to accept a string 
from the user and display characters 
that are present at an even index number.

'''

# input_string = input("Enter the string:")
# print("Original string is",input_string)
# print("Printing only even index chars")

# for i in range(len(input_string)):
#     if i % 2 == 0:
#         print(input_string[i])

# 4.Remove first n characters from a string

'''
Write a program to remove characters 
from a string starting from zero up 
to n and return a new string.

'''

# string_name = input("Enter the string:")
# n = int(input("Enter the integer:"))
# final_string = string_name[n:]
# print("New string after removing from 0 to n:",final_string)

# 5. Check if the first and last number of a list is the same

'''
Write a function to return True if the first 
and last number of a given list is same. 
If numbers are different then return False.

'''
# list_x = [10,20,30,40,50,10]
# list_y = [75,65,30,25,10,50]

# def funct_list(a):
#     if a[0] == a[-1]:
#         print("List:",a)
#         print("Result is True")
#     else:
#         print("List:",a)
#         print("Result is False")
# funct_list(list_x)
# funct_list(list_y)

# 6. Display numbers divisible by 5 from a list

'''
Iterate the given list of numbers and 
print only those numbers which are divisible by 5

'''
# given_list = [10,23,55,64,15,50,65]
# print("Given List is:",given_list)
# print("Divisible by 5") 

# for each in given_list:
#     if each % 5 == 0:
#         print(each)

# 7. Return the count of a given substring from a string

'''
Write a program to find how many times substring “Emma” appears in the given string.

'''
# given = "Emma is good developer. Emma is a writer"
# count_emma = given.count("Emma")
# print("Emma appeared {} times".format(count_emma))

# 8. Print the following pattern

'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

'''
# for i in range(1,6):
#     print((str(i)+" ") * i)

# 9.Check Palindrome Number 

'''
Write a program to check if the given number is a palindrome number.

'''
# number = int(input("Enter the number:"))
# str_numb = str(number)
# reverse_numb = str_numb[::-1]
# reverse = int(reverse_numb)
# if number == reverse:
#     print("Given number is palindrome")
# else:
#     print("Given number is not palindrome")

# 10. Create a new list from a two list using the following condition

'''
Given a two list of numbers, write a program to create a new list 
such that the new list should contain odd numbers from the first list 
and even numbers from the second list.

'''

# list_1 = [10,20,11,24,55,87,91,33]
# list_2 = [3,22,45,64,87,52,88,22]
# new_list = []
# for each in list_1:
#     if each % 2 != 0:
#         new_list.append(each)
# for each in list_2:
#     if each % 2 == 0:
#         new_list.append(each)
# print(new_list)