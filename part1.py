from math import sqrt
#  Print 
print("hello world")
# print("hello world2")
print("2 * 2  =  " , 2+ 2)
print(2+2)
#  Input
# name = input("what is your name: ")
# email = input("what is your email: ")
# address = input ("what is your address: ")
# print("Welome " + name)
# print("Your email address is: " + email)
# print("your living address is: " + address)
# varaible is a location to store some values
# change variable value
address = "77 king"
# print("hello " + name + " with email " + email + " with the address "+ address)
# f string    
age = 22 / 2
print(f"the result is {age}")
result = 10.8 * 25.2
print("The result is :\n" , result)
print(f"the result is {4/9}")

x = 3
y = 2

print(f"/ operator {x/y}")
print(f"/ operator {x*y}")
print(f"// operator {x//y}")
#  get input as the desired type such as int, float ...
# year = int(input("Which year were you born? "))
# print(f"Your age at the end of the year 2021: {2024 - year}" )

# Increasing the value of a variable & conditional statemenet
# number = 0
# number += int(input("First number: "))
# number += int(input("Second number: "))
# if number > 0:
#               print(f" {number} is positive")
# if number < 0:
#               print(f"{number} is negative ")
# else:
#               print(f"{number} is zero ")

# example 
# name  = input("please enter your name: ")
# if name == "Karmer":
#         soap = float(input("How many portions of soup? "))
#         print(f"total cost is: {soap * 5.90}")
# else:
#         print(f"Next please!")

#  example 2
# number  = int(input("please enter a number: "))
# if number < 1000:
#               print("the number is smaller than 1000")
#               if number < 100:
#                 print("the number is smaller than 100")
#                 if number < 10:
#                             print("the number is smaller than 10")
# else:
#         print("thank you!")

#  example 3
# temp  = int(input("please enter a temp: "))
# convert = (temp - 32) * 5/9
# print(f"{temp} degrees Fahrenheit equals to {convert} celciues ")
# if convert < 0:
#         print("Brr! It's cold in here!")

# example 4
# h_wage = float(input("please enter your hourly wage: "))
# h_worked = int(input("please enter your hourly worked: "))
# h_day = input("please enter day of the week: ")
# if str.lower(h_day) == "sunday":
#         daily_wage = (h_wage * 2) * h_worked
# else:
#         daily_wage = h_wage  * h_worked
# print(f"Daily wages {daily_wage} Euros")

#  example 5 (Loyalty bonus)
# points  = int(input("How many points are on your card? "))
# if points < 100:
#         points *= 1.10
#         print(f"You now have {round(points,2)} points")
# else:
#         points *= 1.15
#         print(f"You now have {round(points,2)} points")

# example 7 (quadratic equation)
print(sqrt(9))
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))
x = (-b + sqrt(b**2 - 4 * a * c )) / (2*a)
x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2*a)
print(f"the roots are {x:.2f} and {x2:.2f} ")


# example 7


