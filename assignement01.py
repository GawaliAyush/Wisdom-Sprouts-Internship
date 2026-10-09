# 1) Check if a number is positive, negative, or zero.
# num=int(input("Enter the number"))

# if num>0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# else:
#     print("Zero")


# 2) Check whether a number is even or odd.
# num=int(input("Enter the number"))

# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")


# 3) Find the greater of two numbers.
# num1=int(input("Enter 1st number"))
# num2=int(input("Enter 2nd number"))

# if(num1>num2):
#     print(f"Number {num1} is greater than Number {num2} ")
# else:
#     print(f"Number {num2} is greater than Number {num1} ")


# 4)Find the greatest of three numbers.
# num1=int(input("Enter 1st number"))
# num2=int(input("Enter 2nd number"))
# num3=int(input("Enter 3rd number"))

# if(num1>=num2 and num1>=num3 ):
#     print(f"Number {num1} is greater among all")
# elif(num2>=num1 and num2>=num3 ):
#     print(f"Number {num2} is greater among all")
# else:
#     print(f"Number {num3} is greater among all")


# 5) Check if a person is eligible to vote (age ≥ 18).
# age=int(input("Enter your age"))

# if age>=18:
#     print("Your are eligible to vote")
# else:
#     print("Your are not eligible to vote")


# 6) Check whether a year is a leap year.
# year=int(input("Enter the year"))

# if year%4==0:
#     print(f"{year} is an leap year")
# else:
#     print(f"{year} is not an leap year") 
   

# 7) Check if a character is a vowel or consonant.
# char=input("Enter the character")

# if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
#     print("Entered Character is an vowel")
# else:
#     print("Entered character is not an vowel")


# 8) Check whether a number is divisible by 5 and 11.
# num=int(input("Enter an number"))

# if(num%5==0 and num%11==0):
#     print("Yes")
# else:
#     print("No")


# 9) Check if a number is a multiple of both 3 and 7.
# num=int(input("Enter an number"))

# if(num%3==0 and num%7==0):
#     print("Yes")
# else:
#     print("No")


# 10) Assign grades based on marks:
# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# Below 60: F

# marks=int(input("Enter the marks"))

# if(marks>=90 and marks<=100):
#     print("GRADE A")
# elif(marks>=80 and marks<=89):
#     print("GRADE B")
# elif(marks>=70 and marks<=79):
#     print("GRADE C")
# elif(marks>=60 and marks<=69):
#     print("GRADE D")
# else:
#     print("FAILED")


# 11) Check if a character is uppercase or lowercase.
# char=input("Enter the Character")
# if(char==char.lower()):
#     print("LOWER")
# else:
#     print("UPPER")


# 12) Find whether the entered alphabet is a vowel using if-elif.
# char=input("Enter an alphabet")

# if(char=='a' or char=="A"):
#     print("YES")
# elif(char=='e' or char=="E"):
#     print("YES")
# elif(char=='i' or char=="I"):
#     print("YES")
# elif(char=='o' or char=="O"):
#     print("YES")
# elif(char=='u' or char=="U"):
#     print("YES")
# else:
#     print("NO")


# 13) Check if three sides can form a triangle.

# a = int(input("Enter first side"))
# b = int(input("Enter second side"))
# c = int(input("Enter third side"))

# if a + b > c and a + c > b and b + c > a:
#     print("Triangle is possible")
# else:
#     print("Triangle is not possible")

# 14) Determine the type of triangle (Equilateral, Isosceles, Scalene).

# a = int(input("Enter first side"))
# b = int(input("Enter second side"))
# c = int(input("Enter third side"))

# if a + b > c and a + c > b and b + c > a:
#     if a == b and b== c:
#         print("Equilateral Triangle")
#     elif a == b or b == c or a == c:
#         print("Isosceles Triangle")
#     else:
#         print("Scalene Triangle")
# else:
#     print("Not a valid triangle")

# 15) Find the largest among four numbers.
# num1=int(input("Enter 1st Number"))
# num2=int(input("Enter 2nd Number"))
# num3=int(input("Enter 3rd Number"))
# num4=int(input("Enter 4th Number"))


# if(num1>=num2 and num1>=num3 and num1>=4):
#     print(f"{num1}  is greater")
# elif(num2>=num1 and num2>=num3 and num2>=4):
#     print(f"{num2}  is greater")
# elif(num3>=num1 and num3>=num2 and num3>=4):
#     print(f"{num3}  is greater")
# else:
#     print(f"{num3}  is greater")



# 16) Check whether a number is a three-digit number.
# num=int(input("Enter an number"))

# if(num>=100 and num<=999):
#     print("Entered number is an 3 digit number")
# else:
#     print("Entered number is not an 3 digit number")


# 17) Calculate electricity bill using slab rates.

# units = int(input("Enter electricity units: "))

# if units < 0:
#     print("Invalid units")
# elif units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + (units - 100) * 7
# else:
#     bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# if units >= 0:
#     print("Electricity bill = Rs", bill)




# 18) Calculate income tax based on income slabs.

# income = float(input("Enter annual income: "))

# if income < 0:
#     print("Invalid income")
# elif income <= 300000:
#     tax = 0
# elif income <= 700000:
#     tax = (income - 300000) * 0.05
# else:
#     tax = 20000 + (income - 700000) * 0.10

# if income >= 0:
#     print("Income tax = Rs", tax)


# 19) Check if a student passes (minimum 35 marks in each subject).

# num1 = int(input("Enter marks in 1st subject: "))
# num2 = int(input("Enter marks in 2nd subject: "))
# num3 = int(input("Enter marks in 3rd subject: "))

# if num1 >= 35 and num2 >= 35 and num3 >= 35:
#     print("Student is Pass")
# else:
#     print("Student is Fail")


# 20) Find whether a number is within a given range.

# num = int(input("Enter a number: "))
# low = int(input("Enter lower limit: "))
# high = int(input("Enter upper limit: "))

# if low > high:
#     print("Invalid range")
# elif num >= low and num <= high:
#     print("Number is within the range")
# else:
#     print("Number is outside the range")


# 21) Build a simple calculator using if-elif-else (+, -, *, /).

# num1 = float(input("Enter 1st Number: "))
# op = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter 2nd Number: "))

# if op == "+":
#     print("Result =", num1 + num2)
# elif op == "-":
#     print("Result =", num1 - num2)
# elif op == "*":
#     print("Result =", num1 * num2)
# elif op == "/":
#     if num2 != 0:
#         print("Result =", num1 / num2)
#     else:
#         print("Cannot divide by zero")
# else:
#     print("Invalid operator")


# 22) Check if a year is a century leap year.

# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Century leap year")
# else:
#     print("Not a leap year")


# 23) Determine the season based on the month number.

# month = int(input("Enter month number (1-12): "))

# if month>=2 and month<=5:
#     print("Summer")
# elif month >=6 and month<=9:
#     print("Monsoon")
# elif month >=10 and month<=12 or month==1:
#     print("Winter")
# else:
#     print("Invalid month")


# 24) Find the number of days in a month.

# month = int(input("Enter month number (1-12): "))
# year = int(input("Enter year: "))

# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     print("31 days")
# elif month==4 or month==6 or month==9 or month==11:
#     print("30 days")
# elif month == 2:
#     if year % 4 == 0 or:
#         print("29 days")
#     else:
#         print("28 days")
# else:
#     print("Invalid month")


# 
# 25) Check whether a password meets minimum conditions.

# password = input("Enter a password: ")

# if len(password) < 8:
#     print("Password must contain at least 8 characters")
# elif password.isalpha():
#     print("Password must contain digits also")
# elif password.isdigit():
#     print("Password must contain alphabets also")
# else:
#     print("Password is valid")



# 26) Determine ticket price based on age category.

# age = int(input("Enter age: "))

# if age < 0:
#     print("Invalid age")
# elif age < 5:
#     print("Ticket is free")
# elif age <= 17:
#     print("Ticket price = Rs 100")
# elif age < 60:
#     print("Ticket price = Rs 200")
# else:
#     print("Ticket price = Rs 120")


# 27) Calculate discount based on purchase amount.

# amount = float(input("Enter purchase amount: "))

# if amount < 0:
#     print("Invalid amount")
# elif amount < 1000:
#     discount = 0
# elif amount < 5000:
#     discount = amount * 0.10
# else:
#     discount = amount * 0.20

# if amount >= 0:
#     print("Discount = Rs", discount)
#     print("Final amount = Rs", amount - discount)


# 28) Check if a person is eligible for a driving license.

# age = int(input("Enter age: "))

# if age < 0:
#     print("Invalid age")
# elif age >= 18 :
#     print("Eligible for driving license")
# else:
#     print("Not eligible for driving license")


# 29) Create a login system with username and password validation.

# correct_username = "admin"
# correct_password = "python123"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == correct_username and password == correct_password:
#     print("Login successful")
# elif username != correct_username:
#     print("Incorrect username")
# else:
#     print("Incorrect password")


# 30) Create a menu-driven calculator using if-elif-else.

# while True:
#     print("\n1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         num1 = float(input("Enter 1st number: "))
#         num2 = float(input("Enter 2nd number: "))
#         print("Result =", num1 + num2)

#     elif choice == 2:
#         num1 = float(input("Enter 1st number: "))
#         num2 = float(input("Enter 2nd number: "))
#         print("Result =", num1 - num2)

#     elif choice == 3:
#         num1 = float(input("Enter 1st number: "))
#         num2 = float(input("Enter 2nd number: "))
#         print("Result =", num1 * num2)

#     elif choice == 4:
#         num1 = float(input("Enter 1st number: "))
#         num2 = float(input("Enter 2nd number: "))
#         if num2 != 0:
#             print("Result =", num1 / num2)
#         else:
#             print("Cannot divide by zero")

#     elif choice == 5:
#         print("Exiting program")
#         break

#     else:
#         print("Invalid choice")
