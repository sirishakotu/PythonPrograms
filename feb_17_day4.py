# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

# 5. Display numbers from a list using loop
'''
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
ouput:75
150
145

'''


# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)

# 7. Count the total number of digits in a number
'''
Write a program to count the total number of digits in a number using a while loop.

'''
# number = int(input("Enter the number:"))
# count = 0

# while number != 0:
#     number = number // 10
#     count += 1
# print("Number of digits are:",count)

# 7.  Print the following pattern

'''
Write a program to use for loop to print the following reverse number pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

'''
# number = int(input("Enter the number:"))
# for i in range(number+1,0,-1):
#     for j in range(i-1,0,-1):
#         print(j,end = " ")
#     print()


# Print list in reverse order using a loop

'''
list1 = [10, 20, 30, 40, 50]
output:
50
40
30
20
10

'''
# list1 = [10, 20, 30, 40, 50]
# list2 = list1[::-1]
# for each in list2:
#     print(each)

# 9. Display numbers from -10 to -1 using for loop

# for i in range(-10,0):
#     print(i)

# 10. Use else block to display a message “Done” after successful execution of for loop

# for i in range(1,6):
#     print(i)
# else:
#     print("Done!")

# 11. Write a program to display all prime numbers within a range

