'''
NOTE: More Lists
'''
# The longest string
# strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
# longest = ""
# for i in strings:
#               if len(i) > len(longest):
#                       longest = i
# print(longest)

# Number of matching elements
# def count_matching_elements(my_matrix: list, element: int):
#               count = 0
#               for i in range(len(my_matrix)):
#                             for j in range(len(my_matrix[i])):
#                                           if element == my_matrix[i][j]:
#                                                         count += 1
#               return count
# m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
# print(count_matching_elements(m, 1))

def row_correct(sudoku: list, row_no: int) -> bool:
    # Create a list to track already seen numbers
    seen = []
    
    # Iterate through each value in the given row
    for value in sudoku[row_no]:
        if value != 0:  # Ignore zeros
            if value in seen:  # Check if value is already in the seen list
                return False
            seen.append(value)  # Add value to the seen list
    
    return True  # Return True if no duplicates are found




def column_correct(sudoku: list, column_no: int) -> bool:
    # Create a list to track already seen numbers
    seen = []
    
    # Iterate through each row to extract the column values
    for i in range(len(sudoku)):
        value = sudoku[i][column_no]
        if value != 0:  # Ignore zeros
            if value in seen:  # Check if value is already in the seen list
                return False
            seen.append(value)  # Add value to the seen list
    
    return True  # R

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    # Create a list to track already seen numbers
    seen = []
    
    # Iterate over the 3x3 block starting at (row_no, column_no)
    for i in range(row_no, row_no + 3):  # Loop through 3 rows
        for j in range(column_no, column_no + 3):  # Loop through 3 columns
            value = sudoku[i][j]
            if value != 0:  # Ignore zeros
                if value in seen:  # Check if value is already in the seen list
                    return False
                seen.append(value)  # Add value to the seen list
    
    return True  # Return True if no duplicates are found

        
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]       
# print(row_correct(sudoku, 0))
# print(row_correct(sudoku, 1))
# print(column_correct(sudoku, 0))
# print(column_correct(sudoku, 1))
# print(block_correct(sudoku, 0, 0))
# print(block_correct(sudoku, 1, 2))

'''
NOTE: References
id() find out the exact location that variable points to
IMPORTANT:  a= [1,2,3] b = a  b[1] = 4   print(a) => 1,4,3  any changes made to b will effect a , as b is a reference to a
to overcome this we should create a newlist
new list = []   for in in a : newlist.append(i)
OR new_list = a[:] OR new_list = list(a)   OR  new_list = a.copy()
IMPORTANT: When you pass a list as an argument to a function, you are passing a reference to that list. This means that the function can modify the list directly.
'''
# a = [1, 2, 3]
# print(id(a))
# b = "This is a reference, too"
# print(id(b))
# x = "Hello this is Mahdi"
# print(id(x))
# print("--------")
# number = 1
# print(id(number))
# number += 10
# print(id(number))
# a = 1
# print(id(a))
# b = 1
# print(id(b))
# list1 = [1, 2, 3, 4]
# list2 = list1
# list3 = list1[:]

# list1[0] = 10
# list2[1] = 20
# list3[2]= 30

# print(list1)
# print(list2)
# print(list3)

# Items multiplied by two
def double_items(numbers: list)-> list:
    newlist= []
    for i in numbers:
         newlist.append(i * 2)
    return newlist

numbers = [2, 4, 5, 3, 11, -4]
numbers_doubled = double_items(numbers)
# print("original:", numbers)
# print("doubled:", numbers_doubled)

def remove_smallest(numbers: list):
    
    smallest = min(numbers)
    numbers.remove(smallest)

numbers = [2, 4, 6, 10, 3, 5]
remove_smallest(numbers)
# print(numbers)

# Transpose a matrix
def transpose(matrix: list):
    # Iterate through the rows
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):  # Only iterate over the upper triangle of the matrix
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
              # print(matrix[i][j]) 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

# Output the transposed matrix
# print(matrix)

'''
NOTE: Dictionary
1. Each key can appear only once in the dictionary.
2. list cannot be used as a key BUT tuples can
3. A value can also be mapped to more than one key in the same dictionary.
for name in dictionary:
    print(f"{name} and {dictionary[name]}")    // {name} print KEY and {dictionary[name]} print VALUE
DEFINE VALUES TO DICTIONARIES: (dictionary with the values of types list -cause it has multiple values-)
years = [2002,1991,2024,2011]
cars ={}
SINGLE: cars[key] = value 
LIST: cars[key] = []      method: Append to a List Inside the Dictionary  => for i in years:  cars[key].append(int(i))
ACCESS VALUES IN DICTIONARIES:
for key, values in cars.items():
    newest = max(values)
    print(f"the key in the dict are {key} and the values of the dict are {values} and the most newest car is {newest}")
'''
my_dictionary = {
    "first":"Bmw",
    "last":"Zang",
    "age": 32
}
my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"
# print(my_dictionary)

# for word in my_dictionary:
    # print(word,": ", my_dictionary[word])

# word = input("Please type in a word: ")
# if word in my_dictionary:
    # print("Translation: ", my_dictionary[word])
# else:
    # print("Word not found")

#  Times ten
def times_ten(start_index: int, end_index: int)->dict:
    dicto = {}
    for i in range(start_index,end_index):
        dicto[i]=i*10
    return dicto
d = times_ten(3, 6)
# print(d)

# Factorials
def factorials(n: int)->dict:
    facto = {}
    fact = 1
    for i in range(1,n + 1):
        fact = fact * i
        facto[i] =  fact
    return facto
k = factorials(5)
# print(k[1])
# print(k[3])
# print(k[5]) 

#for key in my_dictionary:
# print("key:", key)
# print("value:", my_dictionary[key])

#  instead of above we use the below:

# for key, value in my_dictionary.items():
#     print("key:", key)
#     print("value:", value)

#  NOTE: when the values in key:value are LIST
# for key, value in groups.items():
#     print(f"words beginning with {key}:")
#     for word in value:
#         print(word)

# Histogram
# def histogram(my_list: str):
#     words = {}
#     for word in my_list:
#         if word not in words:
#             words[word] = 0
#         words[word] += 1

#     result = ""
#     for letter, count in words.items():
#         result += f"{letter}: {'*' * count}\n"

#     return result.strip()

# # Example usage
# print(histogram("abba"))


# Phone book, version 1
def phone_book():
    perons = {}
    
    while True:
        value = int(input("command (1 search, 2 add, 3 quit): "))
        
        if value == 1:  # Search 
            name = input("name: ")
            if name in perons:
                 print(f"{name}'s number: {perons[name]}")
            else:
                print(f"{name} not found")
       
        elif value == 2:  # Add
            name = input("name: ")
            number = int(input("number: "))
            perons[name] = number
            print("Ok")

        elif value == 3:
            print("quitting")
            break
        else:
            print("Invalid command, please try again.")

# phone_book()

# Phone book, version 2
def phone_book2():
    perons = {}
    
    while True:
        value = int(input("command (1 search, 2 add, 3 delete, 4 quit): "))
        
        if value == 1:  # Search 
            name = input("name: ")
            if name in perons:
                 for key, value in perons.items():
                     print(f"name: {key}")
                     for number in value:
                         print(number)
            else:
                print(f"{name} not found")
       
        elif value == 2:  # Add
            name = input("name: ")
            number = int(input("number: "))
            if name not in perons:
                perons[name] = []
            perons[name].append(number)
            print("Ok")
        
        elif value == 3: #Delete (other way for deletion is pop() deleted = staff.pop("David")) NOTE:pop also returns the value from the deleted entry.
            name = input("name to delete: ")
            print(f"{name} has been deleted")
            del perons[name]  # deleting the key pair values

        elif value == 4:
            print("quitting")
            break
        else:
            print("Invalid command, please try again.")

# phone_book2()

# delete in dictionary
# del staff['key']
# deleted = staff.pop('key') // Return also return the value from the deleted entry

# staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
# for key in staff:
#     del staff[key]
# print(staff)  
# del staff ['Alan']
# deleted = staff.pop('Jamal',None)
# print(staff)
# print(deleted)


# for word in my_dictionary:
    # print(word,": ", my_dictionary[word])

# Invert a dictionary
def invert(dictionary: dict):
    inverted = {value: key for key, value in dictionary.items()}
    dictionary.clear()  
    dictionary.update(inverted)

# invert(s)
# x = 0
# while x < 20:
#     my_dictionary[x] = x * 2

# for i in my_dictionary:
#     print(i) 

# list1 = ['ali','baba','jamshid']
# dic1 = {'ali': 2, 'baba': 3, 'jamshid':4}
# for i in list1:
#     print(i)
# for i in dic1:
#     print(i, ": ",dic1[i])
# for key, pair in dic1.items():
#     print(key, pair)

# person1 = {"name": "Pippa Python", "height": 154, "weight": 61, "age": 44}
# person2 = {"name": "Peter Pythons", "height": 174, "weight": 103, "age": 31}
# person3 = {"name": "Pedro Python", "height": 191, "weight": 71, "age": 14}

# # put all the dictionaries in a list
# people = [person1, person2, person3]

# for person in people:
#     print(person["name"])

# combined_height = 0
# for person in people:
#     combined_height += person["height"]

# print("The average height is", combined_height / len(people))

# Movie database
# def add_movie(database: list, name: str, director: str, year: int, runtime: int):
#     actor = {}
#     actor["name"] = name
#     actor["director"] = director
#     actor["year"] = year
#     actor["runtime"] = runtime
#     database = [actor]
#     for actor in database:
#         print(actor)
# detabase = []
# add_movie(detabase, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(detabase, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(detabase)

#Find movies
def find_movies(database: list, search_term: str):
    newList = []
    for name in database:
        if search_term.lower() in name["name"].lower():
            newList.append(name)
    return newList

database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
{"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
{"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]
my_movies = find_movies(database, "python")
# print(my_movies)

'''
NOTE: TUPLES
tupeles ()  lists [] 
tuples ()   list.append()
tuples[0]   list[0]
IMPORTANT There’s no need for a separate variable to create the tuple such as 
IMPORTANT tuples are imutable. should be mutate at initlization
IMPORTNANT tuples could be packed by () and unpakced by a,b = ()
cars = {}     cars[key] = (1,2)    by using () we already craeted a tupe without the need to define a name for it
'''
point = (10,20)
# point[0] = 10
# print(point)

# Create a tuple
def create_tuple(x: int, y: int, z: int):
    tup = (min(x, y, z), max(x, y, z), x + y + z)
    
    # tup = ()
    # tup[0] = min(x,y,z)
    # tup[1] = max(x,y,z)
    # tup[2] = sum(x,y,z)
    return tup
# print(create_tuple(5, 3, -1))

def oldest_person(people: list):
    
    oldest = people[0][1]
    for  i  in people:
        if oldest > i[1]:
            oldest = i[1]
    for i in people:    
        if i[1] == oldest:
            return i[0]
    
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]
# print(oldest_person(people))

# Older people
def older_people(people: list, year: int):
    result = []
    for i in people:
        if i[1] < year:
            result.append(i[0])
    return result
older = older_people(people, 1979)
# print(older)
# print( older_people(people, 1979))

a , b = 2 , 3
# print(a, b)


# Student database
# Student database
def add_student(students: dict, name: str):
    students[name] = []

def print_student(students: dict, name: str):
    # Check if the student exists in the dictionary
    if name in students:
        if not students[name]:  # If the list of completed courses is empty
            print(f"{name} has no completed courses.")
        else:
            courses = ', '.join([f"{course} (Grade: {grade})" for course, grade in students[name]])
            print(f"{name} has completed the following courses: {courses}")
    else:
        print(f"{name} is not in the database.")

def add_course(students: dict, name: str, course_and_grade: tuple):
    if name in students:
        # Unpack the tuple into course and grade
        course, grade = course_and_grade
        students[name].append((course, grade))  # Append the course and grade as a tuple
    else:
        print(f"{name} is not in the database.")

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")


