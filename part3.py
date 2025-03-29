''''
number -> Initialisation
WHILE number < 10 -> condition
number += 1  -> updating variable
'''

'''
STRINGS:
word = input("Enter your name")
len(word)
print(word[index])
print(word.rjust(20, "*"))
print(word[:4]) Half open intervals
if "a" in word  (NOTE: in returns boolean value)
word.find("t")  (NOTE: find either the first index found or -1)

'''

'''
More loops: 
two condition in loop
while sum < 100:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    sum += number
print (f"The sum is {sum}")

Nested loop:

'''

# number = int(input("Please type in a number: "))

# while number <= 10:
#     print(number)
#     number += 1

# print("Execution finished.")

# Print even numbers
# number1 = 2
# number2 = 30
# while number1 < number2:
#     if number1 % 2 == 0:
#         print(number1)
#     number1 += 1

# fix the code
# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number != 0:
#     print(number)
#     number -= 1
# print("Now!")

# number = int(input("Please type in a number: "))
# while number < 100 and number % 5 != 0:
#     print(number)
#     number += 3

# Numbers
# number = int(input("Please type in a number: "))
# number2 = 1
# while number2 != number:
#               print(number2)
#               number2 += 1
    
# Powers of two
# number = int(input("please enter a number "))
# number2 = 1
# while number2 < number:
#                 if number2 == 1:
#                         print(number2)
#                 number2 = number2 * 2
#                 if number2 <= number:
#                     print(number2)

#  Powers of base n
# number = int(input("please enter a number "))
# base = int(input("please enter the base "))

# number2 = 1
# while number2 < number:
#                 if number2 == 1:
#                         print(number2)
#                 number2 = number2 * base
#                 if number2 <= number:
#                     print(number2)

#  The sum of consecutive numbers, version 2 (Perfectly done!!)
# limit = int(input("please enter a number "))
# addup = 0
# result = 0
# verdict = ""
# while limit > result:
#               result += addup
#               addup += 1
#               verdict += f"{result} + "
#         #       print(result)
# print(f"The consecutive sum: {verdict} = {result} ")

n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

# word = "  7   "
# print(word*3)

# word = input("pleas enter a word: \n")
# # times = int(input("enter number of times: "))
# print("-"*len(word))
# print(word[-1])


# End to beginning

# word = input("pleas enter a word: \n")
# number = 0
# index = -1
# while number < len(word):
#     print(word[index])
#     number += 1
#     index -= 1

# Second and second to last characters
# word = input("pleas enter a word: \n")
# if word[1] == word[-2]:
#     print("The second and the second to last characters are ", word[1])
# else:
#     print("The second and the second to last characters are different")

# A rectangle of hashes
# height = int(input("height: "))
# width = int(input("width: "))
# number = 0
# while number < height:
#     print("#"*width)
#     number += 1

# Right-aligned
# string = input("Please type in a string: ")
# print(string.rjust(20, "*"))
# print(string[:4])
# print(string[4:])

# Substrings, part 2
# string = input("Please type in a string: ")
# posi = 0
# zero = -2
# while posi < len(string):
#     if zero == -2:
#         print(string[-1])
#     print(string[zero:-1])
#     zero -= 1
#     posi += 1

#  Does it contain vowels
# string = input("please enter string: ")
# if "a" in string:
#     print("a is in", string)    
# else:
#     print("nothing found")

# Find the first substring
# word = input("please type a word: ")
# character = input("please type a character: ")
# index = word.find(character)
# number = 0
# while True:
#     if character in word:
#           number += 1
#           break
# print(word[index:index + 3])


# Find all the substrings

# word = input("Word: ")
# while True:
#     if len(word) == 0:
#         break
#     print(word)
#     word = word[2:]


# The second occurrence
# string = input("Enter the string: ")
# substring = input("Enter the substring: ")

# # Initialize variables to track occurrences
# index = 0  # Starting index for searching
# count = 0  # Count occurrences

# while index < len(string):
#     # Find the next occurrence of the substring
#     index = string.find(substring, index)
    
#     if index == -1:  # No more occurrences found
#         break
    
#     count += 1  # Increment occurrence count
    
#     if count == 2:  # Second occurrence found
#         print(f"The second occurrence of '{substring}' is at index {index}.")
#         break
    
#     # Move index forward to avoid overlapping occurrences
#     index += len(substring)

# if count < 2:
#     if count == 0:
#         print(f"The substring '{substring}' does not occur in the string.")
#     else:
#         print(f"The substring '{substring}' does not have a second occurrence.")


# 

sum = 0
# number = 0

# # First method (MINE)
# while number != -1:
#     number = int(input("Please type in a number, -1 to exit: "))
#     if number != -1:
#         sum += number
# print(sum)

# # second method
# while True:
#     number = int(input("Please type in a number, -1 to exit: "))
#     if number == -1:
#         break
#     sum += number
# print (f"The sum is {sum}")

#  Third version 
# while sum < 100:
#     number = int(input("Please type in a number, -1 to exit: "))
#     if number == -1:
#         break
#     if number > 20:
#         continue
#     sum += number
# print (f"The sum is {sum}")

# Nested loops

# while True:
#     number = int(input("Please type in a number: "))
#     if number == -1:
#         break
#     while number > 0:
#         print(number)
#         number -= 1

# limit = int(input("Please type in a number: "))
# i = 0
# while i < limit:
#     print(i)
#     i += 2

# Multiplication
# number = int(input("enter a positive integer number: "))
# mult = 0
# j = 1
# i = 1
# while i <= number:
#     while j <= number:
#         mult = i * j
#         print(f"{i} * {j} = {mult}")
#         j +=1
#     j = 1
#     i += 1

# First letters of words (NOT SOLVED)

# letter = input("Please enter something in sentence: ")
# space = len(letter)
# number = 0
# while number < space:
#     print(letter)
#     number += 1


# # Factorial
# number = int(input("enter a integer number: "))
# factorial =  number
# n = 1
# while True:
#     if number <= 0:
#         print("Thank you bye!!")
#         break
#     while number != n:
#         factorial *= (number - n)
#         n += 1
#     print(factorial)
#     break

# Flip the pairs (NOT FULLY COMPLETED)
# number = int(input("enter a integer number: "))
# posi = 1
# addi = 0
# while posi <= number:
#               posi += 1
#               print(posi)
#               posi -= 1
#               print (posi)
#               addi += 2
#               posi += addi
# print(number)

# 1 2 3 4  - 1 2 3
# 6 5 4 3  - 5 4 3
# Taking turns
# number = int(input("enter a integer number: "))
# posi = 1
# addi = 0
# while posi <= number:
#               print(posi)
#               if posi != number:   
#                 print(number)  
#               posi += 1
#               number -= 1


'''NOTE: FUNCTIONS'''
#  Seven brothers
# def mean(a, b, c):
#               print(f"the mean is {(a + b + c) / 3}")
# mean(2, 4, 6)

# def print_many_times(text, times):
#         print(f"{text * 5 }")

# print_many_times("hi\n",3)

# A square of hashes
# def hash_square(lengt):
#         print((("#" * lengt) + "\n") * lengt)
#         # print(f"{('#' * lengt) * lengt}  {'#' * lengt}")
# hash_square(5)

# Chessboard 
# number = 10
# def chessboard(size):
#         for i in range(size):
#             print(("10" * (size // 2) + "1" * (size % 2)) if i % 2 == 0 else ("01" * (size // 2) + "0" * (size % 2)))
#         # print(f"{('#' * lengt) * lengt}  {'#' * lengt}")
# chessboard(10)



