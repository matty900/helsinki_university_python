from math import sqrt

'''
WHILE TURE:
BREAK
'''
# Statement is part of the program which executes something 
# if name == "Anna":
#     print("Hi!")
#     number = 2
# it has print statement and an assignment statement

# A Block is a group of consecutive statements that are at the same level in the structure of the program
# An Expression is a bit of code that results in a determined data type
# When the program is executed, the expression is evaluated so that it has a value that can then be used in the program.
# Function: reusable block of code
# Data type: characteristics of any value present in the program.
# print(type(100))
# Syntax of a programming language determines how the code of a program should be written.

#  Debuging Fix the syntax
# number = int(input("Please type in a number: "))
# if number>100:
#         print("The number was greater than one hundred")
#         number -=  100
#         print("Now its value has decreased by one hundred")
#         print("Its value is now", number)
#         print(number, " must be my lucky number!")
#         print("Have a nice day!")

# Debuging Number of characters
# charac = input("Please enter a word: ")
# leng = len(charac)
# if leng >  1 :
#               print("There are ", leng," letters in the word banana")
# print("thank you")

# Typecasting
# number = float(input("please enter a number: "))
# whole = int(number)
# deci = number - whole
# print(whole)
# print(round(deci,2))

# More conditional left

# number1 = int(input("please enter the first number: "))
# number2 = int(input("please enter the second number: "))

# if number1 > number2:
#         print(number1 , "is bigger than" , number2)
# elif number2 > number1:
#         print(number2 , "is bigger than" , number1)
# else:
#         print("there is a tie")


# Nested conditions
# number = int(input("Please type in a number: "))

# if number > 0:
#     if number % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")
# else:
#     print("The number is negative or zero")


#  Loops while true break
#  TWO WAYS to break the a WHILE LOOP 

#  1 -> more efficinet and common
# while True:
#     password = int(input("please your password, (password is 1234): "))    
#     if password == 1234:
#         break
#     print(" you entered wrong password try again!")
# print("thank you")

#  2 -> less efficinet
# password_correct = True
# while password_correct:
#     password = int(input("Please enter your password (password is 1234): "))
#     if password == 1234:
#         password_correct = False
#     else:
#         print("You entered the wrong password. Try again!")
# print("Thank you")

#  Shall we continue?
# while True:
#     message = input("hi\n")
#     if message == 'no':
#         break
#     print("shall we continue?")
# print("okay then")

# Input validation
# while True:
#     value = int(input("enter a integer number(enter 0 to exit!): "))
#     if value < 0:
#         print("invalid number please enter a valid number")
#     if value > 0:
#         print(sqrt(value))
#     if value == 0:
#         break
# print("thank you for being with us")

# 
attempts = 0

# while True:
#     code = input("Please type in your PIN: ")
#     attempts += 1

#     if code == "1234":
#         success = True
#         break

#     # this is printed if the code was incorrect AND there have been less than three attempts
#     print("Incorrect...try again")

# if success:
    # print("Correct, it took you", attempts , "attemptepts" )


#  The next leap year
# while True:
#     year = int(input("please enter a year: "))
#     if year % 4 == 0:
#         print("the next leap year is", year + 4)
#     else:
#         print("the next leap year is", year + 1)
#     break

# Story
# word2 = ""
# while True:
#     word = input("please enter a word: ")
#     if word == 'end':
#         break
#     word2 += word + " "
#     print(word)
# print(word2)    

#  Story2
# word2 = ""
# while True:
#     word = input("please enter a word: ")
#     if word in word2:
#         break
#     word2 += word + " "
#     print(word)
# print(word2)  
# Working with numbers
track = 0
total = 0
positive = 0
negative = 0
while True:
    number = int(input("please enter a number: "))
    if number > 0:
        positive += 1
    if number < 0 :
        negative += 1
    if number  == 0:
        break
    track += 1
    total += number
print("number typed in ",track)
print("sum of numbers is ",total)
print("mean of numbers is ",total/track)
print("positive numbers ",positive)
print("negative numbers ",negative)



