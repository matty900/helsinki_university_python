import math
'''
WITH for reading files
NOTE: WITH is like WITH clause in SQL
Python: WITH open(file) AS fileName
SQL : WITH tanbleName AS (......)
read() method is useful for printing out the contents of the entire file,

SLICE () 
Extracts a portion of a sequence (like a list, string, or tuple) using slicing syntax
Purpose: Selecting specific characters from a string or sublists from a list.

SPLIT() string.split(separator, maxsplit) =>>>     STRING TO LIST
Splits a string into a list of substrings based on a specified delimiter. 
Purpose: Parsing CSV data or breaking a sentence into words eg: words = text.split(",")

JOIN()  "#".join(myTuple)            =>>>        LIST OR TUPLE TO STRING
Combines elements of a sequence (like a list) into a single string, using a specified delimiter.
Purpose: Creating a CSV row or joining words into a sentence eg: print(" ".join(words))

REPLACE()
To modify a string by replacing specific substrings with another value without altering the original string (since strings in Python are immutable).
Purpose: Formatting data, correcting typos, or standardizing texrt eg:      line = line.replace("\n", "")

STRIP() method to remove extra whitespace
instead of using line.replace("\n", "") we can simply use line.sprip()

IN AND === difference
== should exactly match the searched string such as cake == cake 
IN is proper to check if the search term in a substring of any line. 


'''

with open("example.txt") as new_file:
    contents = new_file.read() # OR the commented method 
    # print(contents)
    # print(new_file.read())

with open("example.txt") as filee:
    for line in filee:
        line = line.replace("\n", "") # we need this because Python's print() function adds its own newline character after printing the line.
        # print(line)

# Largest number
with open("numbers.txt") as new_file:
    maxi = 0
    for line in new_file:
        line = line.replace("\n", "")
        newInt  = int(line)
        if newInt > maxi:
            maxi = newInt
    # print(maxi)

text = "monkey,banana,harpsichord"
words = text.split(",")
# for word in words:  # or the commented method to be in one line 
    # print(word)
# print(" ".join(words)) 

# with open("totals.csv") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         parts = line.split(";")
#         # print(parts)
#         # name = parts[0]
#         # totals = parts[1:]
#         # print("Name:", name)
#         # print("totals:", totals)

# Fruit market
def read_fruits(getter):
    friuts = {}
    with open(getter) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            # friuts = {parts[0]: parts[1]}   this method is wrong cause only the last added witll remaini
            friuts[parts[0]] = parts[1]
    for key in friuts:
        print("key:", key)
        print("value:", friuts[key] )
    # print(friuts)
# read_fruits("friuts.csv")

# Matrix
def matrix_max(in_file):
    numers = []
    maxim = 0
    with open(in_file) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for i in parts:
                numers.append(int(i))
        for x in numers:
            if x > maxim:
                maxim = x
    print(maxim)

def matrix_sum(in_file):
    numers = []
    sumim = 0
    with open(in_file) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for i in parts:
                numers.append(int(i))
        for x in numers:
            sumim += x
    print(sumim)

def row_sum(in_file):
    numers = []
    sumim = 0
    with open(in_file) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            print(parts)
        #     for i in parts:
        #         numers.append(int(i))
        # for x in numers:
        #     sumim += x
    # print(sumim)


# matrix_sum("matrix.txt")
# row_sum("matrix.txt")    // needs to work on
# matrix_max("matrix.txt")

# Course grading, part 1
def grading(in_file1, in_file2):
    totals= {}
    with open(in_file1) as new_file1:
        for line in new_file1:
            line = line.replace("\n", "")
            parts1 = line.split(';')
            if parts1[0] == 'id':
                continue
            totals[parts1[0]] = parts1[1:3]
 
    
    excercises = {}
    with open(in_file2) as new_file2:
        for line in new_file2:
            parts = line.split(';')
            if parts[0] == 'id':
                continue
            excercises[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7]) 
    
    for id , name in totals.items():
        if id in excercises:
            excers = excercises[id]  # refers to the value associated with the key
            print(f"{' '.join(name)} {excers}")
    
# grading("students.csv", "excercises.csv")


# Course grading, part 2
def grading(in_file1, in_file2, in_file3):
    totals = {}
    with open(in_file1) as new_file1:
        for line in new_file1:
            line = line.strip()
            parts1 = line.split(';')
            if parts1[0] == 'id':
                continue
            totals[parts1[0]] = parts1[1:3]
 
    excercises = {}
    with open(in_file2) as new_file2:
        for line in new_file2:
            parts = line.strip().split(';')
            if parts[0] == 'id':
                continue
            excercises[parts[0]] = (
                int(parts[1]) + int(parts[2]) + int(parts[3]) +
                int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])
            )

    exams = {}        
    with open(in_file3) as new_file3:
        for line in new_file3:
            parts3 = line.strip().split(';')
            if parts3[0] == 'id':
                continue
            exams[parts3[0]] = int(parts3[1]) + int(parts3[2]) + int(parts3[3])
        
    for id, name in totals.items():
        if id in excercises:
            if id in exams:
                excers = excercises[id]
                exas = exams[id]
                percent = excers / 40
                value = int(percent * 1000 / 100)
                total  = value + exas

                if total > 0 and total <= 14:
                     print(f"{' '.join(name)} {0}")
                if total > 14 and total <= 17:
                     print(f"{' '.join(name)} {1}")
                if total > 17 and total <= 20:
                     print(f"{' '.join(name)} {2}")
                if total > 20 and total <= 23:
                     print(f"{' '.join(name)} {3}")
                
# grading("students.csv", "excercises.csv","exams.csv")

# Course grading, part 3
def grading(in_file1, in_file2, in_file3):
    totals = {}
    with open(in_file1) as new_file1:
        for line in new_file1:
            line = line.strip()
            parts1 = line.split(';')
            if parts1[0] == 'id':
                continue
            totals[parts1[0]] = parts1[1:3]
 
    excercises = {}
    with open(in_file2) as new_file2:
        for line in new_file2:
            parts = line.strip().split(';')
            if parts[0] == 'id':
                continue
            excercises[parts[0]] = (
                int(parts[1]) + int(parts[2]) + int(parts[3]) +
                int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])
            )

    exams = {}        
    with open(in_file3) as new_file3:
        for line in new_file3:
            parts3 = line.strip().split(';')
            if parts3[0] == 'id':
                continue
            exams[parts3[0]] = int(parts3[1]) + int(parts3[2]) + int(parts3[3])
    print(f"name                        exec_nhbr  exec_pts  exam_pts   total_pts    grade")
    for id, name in totals.items():
        if id in excercises:
            if id in exams:
                excers = excercises[id]
                exas = exams[id]
                percent = excers / 40
                value = int(percent * 1000 / 100)
                total  = value + exas
                grade = 0
                if total > 0 and total <= 14:
                     grade = 0
                if total > 14 and total <= 17:
                     grade = 1
                if total > 17 and total <= 20:
                     grade = 2
                if total > 20 and total <= 23:
                    grade = 3
                # print(f"{' '.join(name):25}")
                print(f"{' '.join(name):30} {excers:<10} {value:<10} {exas:<10} {total:<10} {grade}")
                
# grading("students.csv", "excercises.csv","exams.csv")

# Spell checker   (NOT COMPLETED)
# def spell_chek(x = input("Please enter some words: ")):
#     words = {}
#     words = x.split(" ")
#     with open("wordlist.txt") as new_file:
#         for line in new_file:
#             parts = line.strip()
#             words[]
#             # print(line)
#             if x == line:
#                 print("this is YES")
#             # print(line)
#     # print(x)

# spell_chek()

# Recipe search
def search_by_time(filename: str, time: int):
    receipt = []
    numbers = []
    max  = 0
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            if line: #  Only append non-empty lines
                receipt.append(line)
        for item in receipt:
            if item.isdigit():
                numbers.append(int(item))
        max  = time - numbers[0]
        print(max)
        for elem in numbers:
            print(elem - time)
            if elem - time < max:
                max = elem

    print(numbers)
    print(max)
    # print(receipt)

# search_by_time("recipes.txt", 20)


def search_by_name(filename: str, word: str):
    matches = []  # To store lines matching the search term
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line and word.lower() in line.lower():  # Case-insensitive substring match
                matches.append(line)
    
    # Print matching lines
    if matches:
        print("Matches found:")
        for match in matches:
            print(match)
    else:
        print("No matches found.")

# Test the function
# search_by_name("recipes.txt", "cake")


# def search_by_time(filename: str, times: str):
#     matches = []  # To store lines matching the search term
#     with open(filename) as new_file:
#         for line in new_file:
#             line = line.strip()  # Remove leading/trailing whitespace
#             if line and times  :  # Case-insensitive substring match
#                 matches.append(line)
    
#     # Print matching lines
#     if matches:
#         print("Matches found:")
#         for match in matches:
#             print(match)
#     else:
#         print("No matches found.")

# # Test the function
# search_by_time("recipes.txt", 20)


def search_by_time(filename: str, prep_time: int):
    found_recipes = []  # To store matching recipes with their preparation time

    with open(filename) as new_file:
        lines = new_file.readlines()

    # Iterate through the lines, grouping recipe name and preparation time
    for i in range(len(lines)):
        lines[i] = lines[i].strip()  # Strip whitespace
        if lines[i].isdigit():  # Check if the line is a preparation time
            time = int(lines[i])  # Convert to integer
            if time <= prep_time:  # Check if it meets the condition
                recipe_name = lines[i - 1]  # The recipe name is the line before
                found_recipes.append(f"{recipe_name}, preparation time {time} min")

    return found_recipes

# Test the function
# found_recipes = search_by_time("recipes.txt", 20)

# for recipe in found_recipes:
#     print(recipe)


'''City bikes'''
def get_station_data(filename: str):
    stations = {}
    locations = ()
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip() # line.replace or line.strip(this method is easier)
            words = line.split(";")
            # print(words)
            if words[0] == 'Longitude':
                continue
            longitude = float(words[0])
            latitude = float(words[1])
            stations[words[3]] = (longitude,latitude)  # no need a tuple always have a name
    return stations

def distance(stations: dict, station1: str, station2: str):
    # access to the dict VALUES => dict[KEY]
    coord1 = stations[station1]
    coord2 = stations[station2]

    lon1,lat1 = coord1
    lon2, lat2 = coord2

    x_km = (lon1 - lon2) * 55.26  
    y_km = (lat1 - lat2) * 111.2   

    distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km


stations = get_station_data("bikes.csv")  # should call this before the other function to be called
d = distance(stations, "Kaivopuisto", "Laivasillankatu")
# print(f"Distance: {d:.2f} km")


"""
NOTE: WRITING FILES
with open("newfile.txt", "w") as new_file:  # the file will be created in the directory
with open("newfile.txt", "a") as new_file:  # append to the end of the existing file. don't overwrite it 
    new_file.write("this file is created for the purpose of training in Jan 16th 2025")
    CLEANING FILES
with open("file_to_be_cleared.txt", "w") as my_file: 
    pass
open('file_to_be_cleared.txt', 'w').close()
    DELETING FILES
import os
os.remove("unnecessary_file.csv")

"""

with open("newfile.txt", "w") as new_file:
    new_file.write("this file is created for the purpose of training in Jan 16th 2025\n")
    new_file.write("This is the second line\n")
    new_file.write("This is the last line\n")

# Inscription
def inscription():
    c = input("What is the file name: ")
    d = input("what should be written in it: ")
    with open(c , "w") as my_file:
        my_file.write(d)
# inscription()

coders = []
coders.append(["Eric", "Windows", "Pascal", 10])
coders.append(["Matt", "Linux", "PHP", 2])
coders.append(["Alan", "Linux", "Java", 17])
coders.append(["Emily", "Mac", "Cobol", 9])
line = ""
for coder in coders:
    for value in coder:
        line += f"{value};"
line = line[:-1]
# print(line+"\n")



# Filtering the contents of a file

def filter_solutions():
    names = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            line = line.strip()
            line = line.split(";")
            names.append(line)
    
    for elem in names:
        operation = elem[1]  # e.g., "2+5"
        result = int(elem[2])  # e.g., 7
        
        # Parse numbers and operator from the operation string
        num1 = int(operation[0])  # First number (e.g., 2)
        operator = operation[1]  # Operator (e.g., "+")
        num2 = int(operation[2])  # Second number (e.g., 5)
        
        # Perform the operation
        if operator == "+":
            calculated = num1 + num2
        elif operator == "-":
            calculated = num1 - num2
        else:
            print(f"Unsupported operator: {operator}")
            continue
        
        # Compare the calculated result with the given result
        if abs(calculated) == result:
            print(f"{elem[0]}")  # Print the name

# filter_solutions()

# Store personal data
def store_personal_data(person: tuple):
    result = ' '.join(str(person)) + '\n'
    # result = ' '.join(map(str, person)) + '\n' OR using this one to remove the commas in the csv file
    with open("people.csv", "a") as my_file:
        my_file.write(result)
    # print(person)

store_personal_data(("Paul Paulson", 37, 175.5))
store_personal_data(("Andrew Huberman", 23, 170))

'''
Handling data in a CSV format
'''

# Word search

import re

def find_words(search_term: str):
    matches = []

    with open("words.txt") as new_file:
        for line in new_file:
            word = line.strip()
            
            # Handle asterisk at the start
            if search_term.startswith("*"):
                term = search_term[1:]
                if word.endswith(term):
                    matches.append(word)

            # Handle asterisk at the end
            elif search_term.endswith("*"):
                term = search_term[:-1]
                if word.startswith(term):
                    matches.append(word)

            # Handle dot wildcard (use regex)
            elif "." in search_term:
                regex_pattern = "^" + search_term.replace(".", ".") + "$"
                if re.match(regex_pattern, word):
                    matches.append(word)

            # Handle exact match
            else:
                if word == search_term:
                    matches.append(word)
    
    return matches

# Example usage
# print(find_words("*vokes"))

# Dictionary stored in a file (80% done by me)
def dictionaries():
    entry = 0
    while entry != 3:
        
        entry = int(input("1 - Add word, 2 - Search, 3 - Quit "))
        
        if entry == 1:
            english = input("The word in English: ")
            french = input("The word in French: ")
            tuple = (english, french)
            
            with open("dictionary.txt", "a") as my_file:
                my_file.write(str(tuple) + "\n")  # Add a newline for each entry
        
        elif entry == 2:
            found = False
            search = input("Search term: ")
            
            with open("dictionary.txt", "r") as my_file:  # Open in read mode
                for line in my_file:
                    line = line.strip()  # Remove any leading/trailing whitespace
                    if line:  # Ensure the line is not empty
                        try:
                            english, french = eval(line)  # Convert the string back to a tuple
                            if search.lower() in english.lower() or search.lower() in french.lower():
                                print(f"English: {english}, French: {french}")
                                found = True
                        except:
                            continue  # Skip lines that can't be parsed as tuples
            
            if not found:
                print("No such word exists!")
        
        elif entry == 3:
            print('Bye!')
        
        else:
            print("Invalid entry. Please try again.")

# dictionaries()
            
'''
# Handling errors #
try:

except:

OR (raising exception)

if n < 0 : raise 
'''
def read_input(message, num1, num2):
    
    while True:
        
        try:
            number = input(f'{message} , {int(num1)} , {int(num2)} : ')
            numbers = int(number)
            if numbers > num1 and numbers < num2:
                return numbers
            else:
                print("You must type in an integer between 5 and 10: ")
            
        except ValueError:
            print("You must type in an integer between 5 and 10: ")

# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)


# Parameter validation
def new_person(name: str, age: int):
    person = (name,33)
    if age < 150:
        raise ValueError("The input was negative: " + str(age))
    if len(name) > 40 and len(name) < 2:
        raise ValueError("The input was negative: " + str(name))
    return person

# new_person('ali',120)

# Incorrect lottery numbers ( NOT COMPLETED)

def filter_incorrect():
    try:
        with open("lottery_numbers.csv") as new_file:
            for line in new_file:
                line = line.strip()
                line = line.replace(",", " ")
                line = line.replace(";", " ")
                
                parts = line.split()
                pattern = r"^-?\d+$"
                weeks = parts[0]
                week_format = (parts[1])
                week_numbers = parts[2:]
                one, two, three, four, five, six, seven = week_numbers
                print(one)
                # print(type(week_numbers))

                # if re.fullmatch(pattern, week_numbers):
                #     print(week_numbers)
             
    except ValueError:
         pass 
print("something went wrong")

# filter_incorrect()


# breaing = int(input("thithis "))
# if type(breaing) is int :
#                     raise ValueError("The week number is incorrect:" )

'''
NOTE:
number = 
i = 0

1- for i in range
'''

def input_from_user(how_many: int):
    # how_many = int(input("How many numbers do you want to enter? "))  # Ask for 'how_many'
    print(f"Please type in {how_many} numbers:")
    numbers = []

    for i in range(how_many):
        number = int(input(f"Number {i+1}: "))
        numbers.append(number)

    return numbers

input_from_user(3)

listi =[1,3,4,20,1]
print(sum(listi))