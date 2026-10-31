# Q1 Even or Odd Function
# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".
# ANS:
# def even_odd(num):
#     if(num%2==0):
#         return "Even"
#     else:
#         return "Odd"

# print(even_odd(7))


# Q2 Largest of Two Numbers
# Write a function largest(a, b) that returns the larger number.
# ANS:
# def largest(a,b):
#     if a==b:
#         return "Equal"
#     elif a>b:
#         return f"{a} greater than {b}"
#     else:
#         return f"{b} greater than {a}"

# print(largest(2,3))


# Q3 Print Numbers
# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.
# ANS:
# def print_number(n):
# for i in range(1,n+1):
#     print(i)

# print_number(10)


# Q4 Sum of Numbers
# Write a function sum_n(n) that returns the sum of numbers from 1 to n.
# ANS:
# def sum_ans(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum

# print(sum_ans(10))


# Q5 Multiplication Table
# Write a function table(n) that prints the multiplication table of n from 1 to 10.
# ANS:
# def mul():
#     for i in range(1,11):
#      for j in range(1,11):
#         ans=i*j
#         print(f"{i} x {j} = {ans}")
# mul()

# Q6 Count Even Numbers
# Write a function that takes a list and returns how many even numbers it contains.
# Example:
# count_even([1, 2, 3, 4, 6])
# Output:3
# ANS:
# def return_list(num):
#     cnt=0
#     for i in num:
#         if i%2==0:
#             cnt+=1
#     return cnt

# my_list=[1,2,3,45,6,78,9,88,4]
# print(return_list(my_list))

# Q7 Find Maximum
# Without using max(), write a function that returns the largest number in a list.
# ANS:
# def return_list(num):
#     largest=num[0]
#     i=1
#     while i < len(num):
#         if(num[i]>largest):
#             largest=num[i]
#         i+=1
#     return largest

# my_list=[1,2,3,45,99,6,78,9,88,4,101]
# print(return_list(my_list))


# Q8 FizzBuzz
# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".
# ANS:
# def print_num():
#     for i in range(1,101):
#         if i%3==0 and i%5==0:
#             print(f"{i}=FizzBuzz")
#         elif i%5==0:
#             print(f"{i}=Buzz")
#         elif i%3==0:
#             print(f"{i}=Fizz")
            
# print_num()

# Q9 Palindrome Checker
# Write a function that returns True if a string is a palindrome.
# ANS
# def palindrome(string):
#     i=0
#     j=len(string)-1
#     while(i<=j):
#         if(string[i]==string[j]):
#             i+=1
#             j-=1
#         else:
#             return "NOT PALINDROME"
#             break
#     return "PALINDROME"

# string="ABCBA"
# print(palindrome(string))


# Q10 Count Vowels
# Write a function that counts the vowels in a string.
# ANS:
# def count_vowels(string):
#     cnt=0
#     vowel_list=["a","e","i","o","u","A","E","I","O","U",]
#     for i in range(len(string)):
#         if(string[i] in vowel_list):
#             cnt+=1
#     return cnt
# string="aEeioEZ"
# print(count_vowels(string))
    

# Q11 Second Largest Number
# Write a function that returns the second largest number in a list without using sort().
# ANS:
# def return_list(num):
#     largest=num[0]
#     Second=-1
#     i=1
#     while i < len(num):
#         if(num[i]>largest):
#             Second=largest
#             largest=num[i]
#         elif num[i]<largest and num[i]>Second:
#             Second=num[i]
#         i+=1
#     return Second

# my_list=[1,2,3,45,999,6,78,9,88,4,101,100.99]
# print(return_list(my_list))


# Q12 Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.
# ANS:
# import random
# def guess():
#     num=random.randint(1,100)
#     while(True):
       
#         user_num=int(input("Guess the number"))
#         if(user_num<num):
#             print("Too low than actual number")
#         elif user_num>num:
#             print("Too larger than actual number")
#         elif user_num==num:
#             print("Good !, you guessed the correct number")
#             break
#         else:
#             print("Enter valid whole number ")

# guess()

# Q13 Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"
# ANS:
# def grade(marks):
#     if(marks>=90):
#         return "A"
#     elif marks>=80:
#         return "B"
#     elif marks>=70:
#         return "C"
#     elif marks>=60:
#         return "D"
#     else:
#         return "F" 

# marks=[77,88,66,49,25,99,89,61,59]
# for i in marks:
#    print(f" {i} = {grade(i)}")
