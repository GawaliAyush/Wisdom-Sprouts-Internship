# 1. Write a Python program to check whether a number is even or odd.
# Ans:
# n = int(input("Enter a number: "))

# if n % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


# 2. Write a program to find the largest of three numbers.
# Ans:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest =", a)
# elif b >= a and b >= c:
#     print("Largest =", b)
# else:
#     print("Largest =", c)


# 3. Write a program to check whether a given number is prime.
# Ans:
# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not a prime number")
# else:
#     prime = True

#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             prime = False
#             break

#     if prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")


# 4. Write a program to print the Fibonacci series up to n terms.
# Ans:
# n = int(input("Enter number of terms: "))

# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# 5. Write a program to find the factorial of a number using a loop.
# Ans:
# n = int(input("Enter a number: "))

# fact = 1

# if n < 0:
#     print("Factorial is not defined for negative numbers")
# else:
#     for i in range(1, n + 1):
#         fact *= i

#     print("Factorial =", fact)


# 6. Write a program to reverse a string without using [::-1].
# Ans:
# s = input("Enter a string: ")

# reverse = ""

# for ch in s:
#     reverse = ch + reverse

# print("Reversed string =", reverse)


# 7. Write a program to check whether a string is a palindrome.
# Ans:
# s = input("Enter a string: ")

# reverse = ""

# for ch in s:
#     reverse = ch + reverse

# if s == reverse:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# 8. Write a program to count the number of vowels and consonants in a string.
# Ans:
# s = input("Enter a string: ")

# vowels = 0
# consonants = 0

# for ch in s.lower():
#     if ch.isalpha():
#         if ch in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("Vowels =", vowels)
# print("Consonants =", consonants)


# 9. Write a program to find the sum of all elements in a list.
# Ans:
# numbers = [10, 20, 30, 40, 50]

# total = 0

# for num in numbers:
#     total += num

# print("Sum =", total)


# 10. Write a program to find the largest and smallest element in a list without using max() or min().
# Ans:
# numbers = [10, 5, 30, 2, 50, 15]

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest =", largest)
# print("Smallest =", smallest)


# 11. Write a program to remove duplicate elements from a list.
# Ans:
# numbers = [1, 2, 3, 2, 4, 1, 5, 3]

# result = []

# for num in numbers:
#     if num not in result:
#         result.append(num)

# print("List without duplicates =", result)


# 12. Write a program to count how many times each element appears in a list using a dictionary.
# Ans:
# numbers = [1, 2, 3, 2, 1, 4, 2, 3]

# frequency = {}

# for num in numbers:
#     frequency[num] = frequency.get(num, 0) + 1

# print("Element frequency:")

# for key, value in frequency.items():
#     print(key, ":", value)


# 13. Write a program to find the second-largest number in a list.
# Ans:
# numbers = [10, 20, 40, 30, 50, 40]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# if len(unique) < 2:
#     print("Second-largest number does not exist")
# else:
#     largest = unique[0]
#     second = None

#     for num in unique:
#         if num > largest:
#             second = largest
#             largest = num
#         elif second is None or (num > second and num != largest):
#             second = num

#     print("Second-largest =", second)


# 14. Write a program to sort a list without using sort() or sorted().
# Ans:
# numbers = [5, 2, 8, 1, 9, 3]

# n = len(numbers)

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print("Sorted list =", numbers)


# 15. Write a function that accepts a list of numbers and returns a list containing only the even numbers.
# Ans:
# def even_numbers(lst):
#     result = []

#     for num in lst:
#         if num % 2 == 0:
#             result.append(num)

#     return result

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# print("Even numbers =", even_numbers(numbers))


# 16. Write a program to find the frequency of each character in a string.
# Ans:
# s = input("Enter a string: ")

# frequency = {}

# for ch in s:
#     frequency[ch] = frequency.get(ch, 0) + 1

# for key, value in frequency.items():
#     print(key, ":", value)


# 17. Write a program to check whether two strings are anagrams of each other.
# Ans:
# s1 = input("Enter first string: ").lower()
# s2 = input("Enter second string: ").lower()

# s1 = s1.replace(" ", "")
# s2 = s2.replace(" ", "")

# if sorted(s1) == sorted(s2):
#     print("Anagrams")
# else:
#     print("Not anagrams")


# 18. Write a program to find all duplicate values in a list.
# Ans:
# numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]

# duplicates = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Duplicate values =", duplicates)


# 19. Write a program that takes a sentence and finds the longest word.
# Ans:
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# if len(words) == 0:
#     print("No words found")
# else:
#     longest = words[0]

#     for word in words:
#         if len(word) > len(longest):
#             longest = word

#     print("Longest word =", longest)
#     print("Length =", len(longest))


# 20. Create a simple student marks program that:
#     1. Accepts marks for 5 subjects.
#     2. Calculates the total and percentage.
#     3. Assigns a grade and displays whether the student passed or failed.
# Ans:
# marks = []

# for i in range(5):
#     mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
#     marks.append(mark)

# if any(mark < 0 or mark > 100 for mark in marks):
#     print("Invalid marks")

# else:
#     total = sum(marks)
#     percentage = total / 5

#     print("Total marks =", total)
#     print("Percentage =", percentage, "%")

#     if any(mark < 35 for mark in marks):
#         print("Result: FAIL")
#         print("Grade: F")

#     else:
#         print("Result: PASS")

#         if percentage >= 90:
#             print("Grade: A+")
#         elif percentage >= 80:
#             print("Grade: A")
#         elif percentage >= 70:
#             print("Grade: B")
#         elif percentage >= 60:
#             print("Grade: C")
#         elif percentage >= 50:
#             print("Grade: D")
#         else:
#             print("Grade: E")