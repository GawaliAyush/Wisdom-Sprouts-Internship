
# # 1. DATA TYPES
# # 1. Find the data type of every value in a mixed list.
# # Ans:
# my_list = [10, 3.14, "Hello", True, 5+2j, None]

# for item in my_list:
#     print(item, ":", type(item))


# # # 2. Convert a nested list into a tuple of tuples.
# # # Ans:
# my_list = [[1, 2], [3, 4], [5, 6]]

# result = tuple(tuple(x) for x in my_list)

# print(result)


# # # 3. Remove all duplicate values from a mixed list while preserving the original order.
# # # Ans:
# my_list = [10, "apple", 20, "apple", 10, True, 20]

# result = []

# for item in my_list:
#     if item not in result:
#         result.append(item)

# print(result)



# # 2. OPERATORS

# # # 4. Check whether a number is a power of 2 using operators.
# # # Ans:
# n = int(input("Enter a number: "))

# if n > 0 and (n & (n - 1)) == 0:
#     print("Power of 2")
# else:
#     print("Not a power of 2")


# # # 5. Swap two numbers using bitwise XOR.
# # # Ans:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print("After swapping:")
# print("a =", a)
# print("b =", b)


# # # 6. Find whether a number is divisible by both 4 and 6 using logical operators.
# # # Ans:
# n = int(input("Enter a number: "))

# if n % 4 == 0 and n % 6 == 0:
#     print("Divisible by both 4 and 6")
# else:
#     print("Not divisible by both")


# # # 7. Calculate the total electricity bill using different unit rates.
# # # Ans:
# units = int(input("Enter electricity units: "))

# if units < 0:
#     print("Invalid units")
# elif units <= 100:
#     bill = units * 1.50
#     print("Total bill =", bill)
# elif units <= 200:
#     bill = 100 * 1.50 + (units - 100) * 2.50
#     print("Total bill =", bill)
# else:
#     bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4
#     print("Total bill =", bill)


# # 3. CONDITIONAL STATEMENTS
# # # 8. Check whether three sides can form a triangle.
# # # Ans:
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if (a > 0 and b > 0 and c > 0 and
#     a + b > c and a + c > b and b + c > a):
#     print("Valid triangle")
# else:
#     print("Invalid triangle")


# # # 9. Determine the type of triangle (Equilateral, Isosceles, Scalene).
# # # Ans:
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a <= 0 or b <= 0 or c <= 0 or a+b <= c or a+c <= b or b+c <= a:
#     print("Invalid triangle")
# elif a == b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")


# # # 10. Create a simple ATM menu (Withdraw, Deposit, Balance).
# # # Ans:
# balance = 5000

# while True:
#     print("\n1. Withdraw")
#     print("2. Deposit")
#     print("3. Balance")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         amount = float(input("Enter withdrawal amount: "))
#         if 0 < amount <= balance:
#             balance -= amount
#             print("Withdrawal successful")
#         else:
#             print("Insufficient balance or invalid amount")

#     elif choice == 2:
#         amount = float(input("Enter deposit amount: "))
#         if amount > 0:
#             balance += amount
#             print("Deposit successful")
#         else:
#             print("Invalid amount")

#     elif choice == 3:
#         print("Current balance:", balance)

#     elif choice == 4:
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice")


# # # 11. Calculate income tax based on different tax slabs.
# # # Ans:
# income = float(input("Enter annual income: "))

# if income < 0:
#     print("Invalid income")
# elif income <= 250000:
#     tax = 0
#     print("Income tax =", tax)
# elif income <= 500000:
#     tax = (income - 250000) * 0.05
#     print("Income tax =", tax)
# elif income <= 1000000:
#     tax = 250000 * 0.05 + (income - 500000) * 0.20
#     print("Income tax =", tax)
# else:
#     tax = 250000 * 0.05 + 500000 * 0.20 + (income - 1000000) * 0.30
#     print("Income tax =", tax)


# # # 12. Create a menu-driven calculator using if-elif.
# # # Ans:
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter your choice: "))

# if choice == 1:
#     print("Result =", a + b)
# elif choice == 2:
#     print("Result =", a - b)
# elif choice == 3:
#     print("Result =", a * b)
# elif choice == 4:
#     if b != 0:
#         print("Result =", a / b)
#     else:
#         print("Division by zero is not allowed")
# else:
#     print("Invalid choice")



# # 4. LOOPS

# # # 13. Print all prime numbers between 1 and n.
# # # Ans:
# n = int(input("Enter the value of n: "))

# for num in range(2, n + 1):
#     prime = True

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num, end=" ")


# # # 14. Find the factorial of a number using a loop.
# # # Ans:
# n = int(input("Enter a number: "))

# fact = 1

# if n < 0:
#     print("Factorial not defined for negative numbers")
# else:
#     for i in range(1, n + 1):
#         fact *= i

#     print("Factorial =", fact)


# # # 15. Print the Fibonacci series up to n terms.
# # # Ans:
# n = int(input("Enter number of terms: "))

# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# # # 16. Check whether a number is an Armstrong number.
# # # Ans:
# n = int(input("Enter a number: "))

# temp = n
# power = len(str(n))
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total += digit ** power
#     temp //= 10

# if n >= 0 and total == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


# # # 17. Reverse a number and check if it is a palindrome.
# # # Ans:
# n = int(input("Enter a number: "))

# temp = n
# reverse = 0

# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp //= 10

# print("Reversed number =", reverse)

# if n >= 0 and n == reverse:
#     print("Palindrome number")
# else:
#     print("Not a palindrome")


# # # 18. Find the Greatest Common Divisor (GCD) of two numbers.
# # # Ans:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# x, y = abs(a), abs(b)

# while y != 0:
#     x, y = y, x % y

# print("GCD =", x)


# # 5. FUNCTIONS

# # # 19. Write a function to check if a string is a palindrome.
# # # Ans:
# def palindrome(s):
#     s = s.lower()
#     return s == s[::-1]

# text = input("Enter a string: ")

# if palindrome(text):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # # 20. Write a function to count vowels and consonants in a string.
# # # Ans:
# def count_vowels_consonants(s):
#     vowels = 0
#     consonants = 0

#     for ch in s.lower():
#         if ch.isalpha():
#             if ch in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1

#     return vowels, consonants

# text = input("Enter a string: ")

# v, c = count_vowels_consonants(text)

# print("Vowels =", v)
# print("Consonants =", c)


# # # 21. Create a function to calculate simple and compound interest.
# # # Ans:
# def interest(p, r, t):
#     si = (p * r * t) / 100
#     amount = p * (1 + r / 100) ** t
#     ci = amount - p
#     return si, ci

# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time in years: "))

# si, ci = interest(p, r, t)

# print("Simple Interest =", si)
# print("Compound Interest =", ci)


# # # 22. Write a function to return all factors of a number.
# # # Ans:
# def factors(n):
#     result = []

#     for i in range(1, abs(n) + 1):
#         if n % i == 0:
#             result.append(i)

#     return result

# n = int(input("Enter a number: "))

# if n == 0:
#     print("Zero has infinitely many factors")
# else:
#     print("Factors =", factors(n))


# # # 23. Write a function to find the second-largest number in a list.
# # # Ans:
# def second_largest(lst):
#     unique = sorted(set(lst))

#     if len(unique) < 2:
#         return None

#     return unique[-2]

# numbers = [10, 20, 40, 30, 40, 50]

# result = second_largest(numbers)

# if result is None:
#     print("Second-largest element does not exist")
# else:
#     print("Second-largest =", result)


# # 6. LISTS
# # # 24. Merge two lists without duplicates.
# # # Ans:
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# result = list1.copy()

# for item in list2:
#     if item not in result:
#         result.append(item)

# print("Merged list =", result)


# # # 25. Find the second-largest and second-smallest elements.
# # # Ans:
# numbers = [10, 20, 5, 40, 30, 5, 40]

# unique = sorted(set(numbers))

# if len(unique) < 2:
#     print("Second-largest and second-smallest do not exist")
# else:
#     print("Second-smallest =", unique[1])
#     print("Second-largest =", unique[-2])


# # # 26. Rotate a list to the left by k positions.
# # # Ans:
# lst = [1, 2, 3, 4, 5]

# k = int(input("Enter rotation positions: "))

# if lst:
#     k = k % len(lst)
#     result = lst[k:] + lst[:k]
# else:
#     result = []

# print("Rotated list =", result)


# # 27. Separate even and odd numbers into two lists.
# # Ans:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even numbers =", even)
# print("Odd numbers =", odd)


# # 28. Find the common elements between two lists.
# # Ans:
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)

# print("Common elements =", common)


# # 7. TUPLES & SETS
# # 29. Count the frequency of each element in a tuple.
# # Ans:
# t = (1, 2, 3, 2, 1, 4, 2, 3)

# for item in dict.fromkeys(t):
#     print(item, ":", t.count(item))


# # 30. Find the union, intersection, and difference of two sets.
# # Ans:
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# print("Union =", A | B)
# print("Intersection =", A & B)
# print("Difference A-B =", A - B)
# print("Difference B-A =", B - A)


# # 31. Check whether one set is a subset of another.
# # Ans:
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}

# if A.issubset(B):
#     print("A is a subset of B")
# else:
#     print("A is not a subset of B")


# # 8. DICTIONARIES
# # # 32. Count the frequency of words in a sentence.
# # # Ans:
# sentence = input("Enter a sentence: ")

# words = sentence.lower().split()
# frequency = {}

# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1

# print("Word frequency:")

# for word, count in frequency.items():
#     print(word, ":", count)


# # 33. Create a dictionary from two lists (keys and values).
# # Ans:
# keys = ["name", "age", "city"]
# values = ["Rahul", 21, "Pune"]

# result = dict(zip(keys, values))

# print(result)


# # 34. Sort a dictionary by its values.
# # Ans:
# my_dict = {
#     "Apple": 50,
#     "Banana": 20,
#     "Mango": 80,
#     "Orange": 40
# }

# result = dict(sorted(
#     my_dict.items(),
#     key=lambda item: item[1]
# ))

# print("Sorted dictionary =", result)



# # 9. FILE HANDLING
# # 35. Read a text file and count the number of lines, words, and characters.
# # Ans:
# with open("sample.txt", "r") as file:
#     content = file.read()

# lines = content.splitlines()
# words = content.split()
# characters = len(content)

# print("Number of lines =", len(lines))
# print("Number of words =", len(words))
# print("Number of characters =", characters)


# # 36. Copy only the even-numbered lines from one file to another.
# # Ans:
# with open("input.txt", "r") as source:
#     lines = source.readlines()

# with open("output.txt", "w") as destination:
#     for i, line in enumerate(lines, start=1):
#         if i % 2 == 0:
#             destination.write(line)

# print("Even-numbered lines copied successfully")


# # 10. EXCEPTION HANDLING
# # 37. Handle invalid integer input using try-except.
# # Ans:
# try:
#     num = int(input("Enter an integer: "))
#     print("Number =", num)

# except ValueError:
#     print("Invalid input! Please enter an integer.")


# # 38. Handle file-not-found errors while reading a file.
# # Ans:
# try:
#     with open("sample.txt", "r") as file:
#         content = file.read()
#         print(content)

# except FileNotFoundError:
#     print("Error: File not found!")

# except PermissionError:
#     print("Error: Permission denied!")



# # 11. MODULES
# # 39. Create a random password generator using the random and string modules.
# # Ans:
# import random
# import string

# length = int(input("Enter password length: "))

# if length <= 0:
#     print("Password length must be positive")

# else:
#     characters = (
#         string.ascii_letters +
#         string.digits +
#         string.punctuation
#     )

#     password = ''.join(
#         random.choice(characters)
#         for i in range(length)
#     )

#     print("Generated password =", password)


# # 40. Use the datetime module to calculate the number of days between two dates.
# # Ans:
# from datetime import datetime

# date1 = input("Enter first date (DD-MM-YYYY): ")
# date2 = input("Enter second date (DD-MM-YYYY): ")

# d1 = datetime.strptime(date1, "%d-%m-%Y")
# d2 = datetime.strptime(date2, "%d-%m-%Y")

# difference = abs((d2 - d1).days)

# print("Number of days between dates =", difference)