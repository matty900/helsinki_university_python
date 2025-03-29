# import math
from math import *
import string
import fractions
from random import shuffle , randint, seed, sample
from datetime import datetime, timedelta
import csv
import json
import urllib.request
import string_helper

# randint() print random int  - suffle() shuffle any data structure - choice() randomly picked item from a data structure
# sample ()
'''
# NOTE: three ways to define a list of number
#1 number_pool = list(range(1, 41))  // More efficinet and faster
#2 number_pool = [] for i in range(1,41):  number_pool.append(i) 
#3  list comperhenstino 
instead of 
words = []    # traditinoal way
string = "this is what!!" 
for words in string:
        if words not it string.punctiation:
                words.append()
        "".join(words)
SIMPLY SAY:
 filtered_chars = [char for char in string if char not in punctuation]  # List comprehension
"".join(filtered_chars)

# Analogy
List comprehension: [fruit for fruit in basket if fruit.is_ripe()]

fruit (first one): This is like saying, "Put this fruit..."
for fruit in basket: "...from the basket..."
if fruit.is_ripe(): "...only if it's ripe."

NOTE: Modules
MATH MODULE
STRING MODULE usaully use like:
for char in my_string:
              if char in string.whitespace:    // or any other string
                            print('number of spaces')  // or anything
FRACTION MODULE
'''

# print(math.sqrt(4))   // this is used with import math
# print(math.log(2,3))  // this is used with import math
# print(sqrt(4))        // this is used with from math import *
# print(log(8,2))       // this is used with from math import *

def hypotenuse(leg1: float, leg2: float):
              return sqrt(pow(leg1,2)+ pow(leg2,2))
# print(hypotenuse(3,4))

# Special characters
def separate_characters(my_string: str):
        punci = []
        lower = []
        upper = []
        count = 0
        parts = (punci,lower,upper)
        
        for char in my_string:
                if char in string.punctuation:
                            punci.append(char)
                elif char in string.ascii_lowercase:
                            lower.append(char)
                elif char in string.ascii_uppercase:
                            upper.append(char)
                elif char in string.whitespace:
                        count += 1
        print(f'There are {count} spaces in the string')
        return parts
# sections = separate_characters("Olé!!! Hey, are ümläüts wörking?")
# print(sections[0])
# print(sections[1])
# print(sections[2])


# letter = "this is bar lkdlkd sld sd"
# letter = letter.split()
# print(letter)
# one_line = " ".join(letter)
# one_line = one_line.split()
# print(one_line)
# # one_line = one_line.split()
# # letter2 = letter.replace("\n", ",")
# for i in one_line:
#         for j in i:
#               print(j)

# Fractions
def fractionate(amount: int) -> list:
        numbers  = []
        for i in range (amount):
                numbers.append(fractions.Fraction(numerator= 1, denominator=amount))
        return numbers
# print(fractionate(5))

number_pool = list(range(1, 41))
weekly_draw = sample(number_pool, 7)
# print(weekly_draw)


# print("The result of the throw:", random.randint(1, 6))
def lottery_numbers(amount: int, lower: int, upper: int)-> list:
        new_list = []
        for i in range(amount):
                new_rnd = randint(lower, upper)
                new_list.append(new_rnd)
        return new_list
# print(lottery_numbers(7,1,40))

# Password generator, part 1
def generate_password(round: int) -> str:
        words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        shuffle(words)
        chosen_words = ",".join(words[0:round]).replace(",", "")
        return chosen_words
        
# for i in range(10):
#     print(generate_password(8))

# Password generator, part 2
def generate_strong_password(round: int, second : bool, third : bool) -> str:
        chosen_passwords = []
        words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        shuffle(words)
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        shuffle(numbers)
        characters = ["!", "?","=","+","-","(",")","#"]
        shuffle(characters)
        
        chosen_passwords.extend(words)
        if second:
                chosen_passwords.extend(numbers)
        if third:
                chosen_passwords.extend(characters)
        shuffle(chosen_passwords)

        chosen_final = ",".join(chosen_passwords[0:round]).replace(",", "")
        return chosen_final

# for i in range(10):
#     print(generate_strong_password(8, True, True))


# Random words
def words(n: int, beginning: str) -> list:
        selected = []
        words = []
        with open("words.txt") as filee:
                for line in filee:
                        line = line.strip()
                        if line.startswith(beginning):
                                selected.append(line)
        if len(selected) < n:
                raise ValueError("Not enough words starting with '{}'".format(beginning))
        
        shuffle(selected)
        return selected[0:n]

# try:
#     result = words(5, "ga") # Example that might raise ValueError
#     print(result)
# except ValueError as e:
#     print(f"Error: {e}")

'''
NOTE: Times and dates
# Formating times and dates 
# strftime : formatting the string representation of a datetime object (string formating time)
# strptime : parse a datetime object from a string given by the user (string parse time)
# substrction dates works but addition is difference and should be done with timedelta
time_now = datetime.now()
midsummer = datetime(2021, 6, 26)

difference = midsummer - time_now
print("Midsummer is", difference.days, "days away") 

HOWEVER difference = midsummer +  time_now WON'T WORK


'''
# my_time = datetime.now()  # displaying current time
# print("Day: ",my_time.day)
# print("Month: ",my_time.month)
# print("Year: ",my_time.year)

#  A timedelta object represents a duration, the difference between two datetime or date instances.
# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) -> All arguments are optional and default to 0

# How old
# day = int(input("enter your age day: "))
# month = int(input("enter your age month: "))
# year = int(input("enter your age year: "))
# timenow = datetime.now()
# birthday = datetime(year,month,day)
# difference  = timenow - birthday  # datetime substraction result is timedelta object (only access to number of days NOT years)
# print(birthday)
# print(difference) # could be devided to 365 for years



my_time = datetime.now()
# print(my_time.strftime("%d,%m,%Y, %H ,%M"))

# Screen time (STILL NEED SOME WORK 90% DONE)
def screen_time():
        # file_name = input("filename: ")
        starting_date = input("Starting date: ")
        start_date_formated = datetime.strptime(starting_date, "%d.%m.%Y")
        day = int(input("How many days: "))
        one_week = timedelta(days=day)
        end_date = start_date_formated + one_week
        end_date_formated = datetime.strftime(end_date, "%d.%m.%Y")
        print(f"Time period : {start_date_formated} - {end_date_formated}")
        print("Please type in screen time in minutes on each day (TV computer mobile):")
        n = 1
        total_mitunes = 0
        with open("late_june.txt", "a") as my_file:
                 my_file.write(f"Time period : {start_date_formated} - {end_date_formated}")
        for i in range(day):
                now = timedelta(days=n)
                difference = start_date_formated + now
                miutes = input(f"screenn time {difference}: ")
                miutes = miutes.replace(" ", "/")
                n += 1
                with open("late_june.txt", "a") as my_file:
                        my_file.write(f"Total minutes: :{total_mitunes}")
                        my_file.write(f"{miutes}\n")

       
        # for i in range(day):
        #          inputs = input(f"{start_date_formated}")
        #          with open("late_june.txt", "w") as my_file:

# screen_time()

'''
DATA PROCESSING
# READING CSV FILE AND SAVE THEM AS LIST
# READING JSON FILES AND ACCESS THE KEY VALUES IN DICTIONARY
# 
'''
# with open("grades.csv") as my_file:
        # for line in csv.reader(my_file, delimiter=";"): 
        #         print(line) # separates the contents of each line into a list using the delimiter ;
        
        # for line in my_file:
        #         line  = line.strip().replace(";", " ")
        #         new = line.split() # work the same as csv.reader()
        #         print(new)

# with open("courses.json") as my_file:
#         data = my_file.read()

# courses = json.loads(data)
# # print(courses)
# for course in courses:
#         print(course["name"])

# Handling JSON files
def print_persons(filename: str):
        with open(filename) as my_file:
                persn = my_file.read()
        persons = json.loads(persn)
        for person in persons:
                print(person["name"], person["age"], tuple(person["hobbies"]))

# print_persons("courses.json")
# 

# my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses ")
# print(my_request.read())   

# Who cheated (should work on it)
# def cheaters() -> list:

# with open("start_times.csv") as my_file:
#         with open("submissions.csv") as my_file2:
#                 for line in csv.reader(my_file , delimiter=";"):
#                         name1 = line[0]
#                         time1 = datetime.strptime(line[1],'%H:%M')
#                         for line2 in csv.reader(my_file2 , delimiter=";"):
#                                 name2 = line2[0]
#                                 time2 = datetime.strptime(line[1],'%H:%M')
#                                 print(name2)
#                         print(name1)

'''
OWN MODULES
'''
# String helper

my_string = "Well hello there!"

# print(string_helper.change_case(my_string))

p1, p2 = string_helper.split_in_half(my_string)

# print(p1)
# print(p2)
                      
m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
# print(m2)    

'''
More python features
'''
# onditional expression (ternary operator)
x = 11
# print("even" if x%2 == 0 else "odd")
y = x + 1 if x%2 == 0 else x - 1
# print(y)

# An "empty" blocK
def testing():
    pass

# Loops with else blocks
# default parameter value
def say_hello(name="Mahdi"):
        print(name)
say_hello()

# Your own programming language
