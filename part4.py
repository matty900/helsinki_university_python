'''NOTE: More functions'''
# A square of hashes
# def line(b):
#      print("#" * b )
# # A box of hashes
# def has_boxes(b):
#         a = b
#         while b > 0:
#                line(a)
#                b -= 1
# has_boxes(5)

# A square
# def line(a, b):
#      print(a * b )
# # A box of hashes
# def has_boxes(a, b):
#         x = b
#         while b > 0:
#                line(a, x)
#                b -= 1
# has_boxes("Z",5)

# A triangle
# def line(b):
#      print("#" * b )
# # A box of hashes
# def has_boxes(b):
#         x = 1
#         while b > 0:
#                line(x)
#                x += 1
#                b -= 1
# has_boxes(6)

# A shape
# def line(a, b):
#      print(a * b )

# def has_boxes(a, b, c , d):
        
#         x = 1
#         while a > 0:
#                line(x, b)
#                x += 1
#                a -= 1
#         y = c
#         while c > 0:
#               line(y , d)
#               c -= 1
# has_boxes(6, "X", 3, "Z")

# # A spruce
# def spruce(a):
#        x = 1
#        z = a
#        while a > 0:
#               print((" "* a )+ (x * "*"))
#               x += 2
#               a -= 1
#        print((" "* z )+"*")
# spruce(5)

# The greatest number
# def greatest_number(a, b, c):
#               if a > b and a > c:
#                return a  
#               if b > a and b > c:
#                    return b
#               if c > a and c > b:
#                      return c 

# print(greatest_number(1,20, 12))

# def same_chars(a, b, c):
#        if a[b] == a[c]:
#               return True
#        return False
# print(same_chars("babba",1,3))

#  RETURN FUNCTION

# def first_word(a):
#        x = 0
#        while x < len(a):
#               if a[x] == " ":
#                      return a[:x]
#               x += 1

# def second_word(a):
#        x = 0
#        while x < len(a):
#               if a[x] == " ":
#                      return a[x + 1:]
#               x += 1

# def last_word(a):
#        x = len(a)- 1
#        while x > 0:
#               if a[x] == " ":
#                      return a[x + 1:] # x + 1 to remove the space
#               x -= 1    

# print(first_word("hello matti this is by by"))
# print(second_word("hello matti this is by by"))
# print(last_word("hello popoi popu"))

# # TYPE HINT

# def print_many_times(message : str, times : int):
#     while times > 0:
#         print(message)
#         times -= 1

# def ask_for_name() -> str:
#     name = input("Mikä on nimesi? ")
#     return name

'''NOTE:LISTS
list.append()  add to the end of th elist
list.insrt(2,12) add to location 2 the value 12
list.pop(2) remove at the index 2      list= [1,2,3,4]  =>  list= [1,2,4]
list.remove(2) remove value of item 2 in the list     list= [1,2,3,4]  =>  list= [1,3,4]
if x in list: print("exist)  check a existance of an item in a list 
list.sort()    change the original list
sorted(list)  do not modify the original list
max(lsit)    min(list)   sum(list)
while -> indifiniate loop , for -> definite loop 
Wwile - for - range(4) => 0,1,2,3 range (2,5) => 2,3,4 range(1,9,2) => 1,3,5,7
NOTE: Difference between for i in list[] AND for i in range(0,len(list))
THREE WAYS TO SHOW STRINGS
for i in string: print i
for in in range(0,len(string)): print(string[i])
x = 0  while x < len(string): print(string[x]) x+= 1
'''
# i = 0
# my_list = [1,2,4,5,6]
# my_list.append(3) # add item to the end of the list
# print(my_list[0])
# while i < len(my_list):
#         print(my_list[i])
#         i += 1
# for i in my_list:
#               print(i)

# Add items to a list
# count = int(input("How many items: "))
# items = []
# i = 0
# j = 1
# while i < count:
#         item = int(input(f'item{j}: '))
#         j += 1
#         count -= 1
#         items.append(item)
# print(items)

#  Addition and removal
# list = []
# while True:
#         selection = input("add or removal: ")
#         if selection == 'a':
#               list.append(len(list) + 1)
#               print(list)
#         if selection == 'r':
#               list.pop(-1)
#               print(list)
#         if selection == 'x':
#               print("Bye!")
#               break
 
# Same word twice
# list = []
# i = 1
# while i != 0:
#               word = input("Word ")
#               if word in list:
#                             print(f'you typed {len(list)} different words')
#                             print(f'you entered{list}')
#                             i = 0
#               else:
#                       list.append(word)


# List twice
# list = []
# item = 1
# while item != 0:
#               item = int(input("entere a number: "))
#               list.append(item)
#               print(list)
#               print(sorted(list))

# The length of a list

# def length(my_list : list) -> int:
#               return len(my_list)

# result = length([1,2,3,4,5])
# print(result)


# def mean(my_list : list ):
#         sum = 0
#         for i in my_list:
#                 sum += i
#         return sum // len(my_list) #could be /  for integer or // for float
# result = mean([1,2,3,4,5])
# print(result)

# def mean(my_list : list ):
#         return max(my_list) - min(my_list) 
# result = mean([1,2,3,4,5,20])
# print(result)

# name = input("please enter a name: ")
# for i in name:
#               print(i + "\n*")

# for i in range(1,5,3):
#         print(i)

# From negative to positive
# number = int(input("please enter a number: "))
# if number > 0:
#               j = 0 
#               j = -(number + 1)
#               for i in range(number, j, -1):
#                             print(i)
# if number < 0:
#          j = 0 
#          j = -(number - 1)
#          for i in range(number, j):
#                  print(i)

# convert range to a list
# numbers2 = range(2,7)
# numbers = list(range(2, 7))
# print(numbers2)
# print(numbers)

# List of stars
# def list_of_stars(my_list:list):
#               i = 0
#               while i < len(my_list):
#                       print("*" * my_list[i])
#                       i += 1
# print(list_of_stars([1,2,3,4]))


# # Anagrams
# a = "mahdi"
# b = "amhdi"
# anagrams = True
# anagrams1 = 0
# for i in range(0,len(a),1):
#         if a[i] in b:
#                anagrams1 += 1
#         else:
#                anagrams1 -= 1
# if anagrams1 == len(b):
#         print(True)
# else:
#         print(False)

# Anagrams (easy way)
# def anagrams(str1, str2):
#     # Sort both strings and compare
#     return sorted(str1) == sorted(str2)
# print(anagrams("tame", "meta"))  # True
# print(anagrams("tame", "mate"))  # True
# print(anagrams("tame", "team"))  # True
# print(anagrams("tabby", "batty"))  # False
# print(anagrams("python", "java"))  # False

# #  Palindrome
# def palindromes(word: str) -> bool:
#     """
#     Checks if the given string is a palindrome.
#     """
#     # A string is a palindrome if it equals its reverse
#     return word == word[::-1]


# while True:
#         user_input = input("Please type in a palindrome: ")
#         if palindromes(user_input):
#             print(f"{user_input} is a palindrome!")
#             break
#         else:
#             print("That wasn't a palindrome")

# # The sum of positive numbers
# def sum_of_positives(ingeges:list):
#               sum = 0
#               for i in ingeges:
#                       if i < 0:
#                               continue
#                       else:
#                               sum += i

#               return sum
# print(sum_of_positives([1,-2,3,9,-8]))

# # Even numbers
# def even_numbers(ingeg : list):
#         listic = []
#         for i in ingeg:
#                 if i % 2 == 0:
#                         listic.append(i)
#         return listic
# print(even_numbers([1,2,3,4,5,6,7,8,9,-2]))

# # The sum of lists
# def list_sum(integ1 : list , integ2 : list)->list:
#         i = 0
#         newest = []
#         while i < len(integ1):
#                 newest.append(integ1[i] + integ2[i])
#                 i += 1
#         return newest
# a = [1, 2, 3]
# b = [7, 8, 9]
# print(list_sum(a,b))

# # Distinct numbers
# def distinct_numbers(integ1: list) -> list:
#     """
#     Returns a sorted list of distinct numbers from the input list.
#     """
#     newlist = []  # List to store distinct numbers
#     for num in integ1:
#         if num not in newlist:
#             newlist.append(num)
#     return sorted(newlist) 

# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list))

# def length_of_longest(x :list)-> int:
# def length_of_longest(mylist :list):
#               my_list = ["first", "second", "fourth", "eleventh"]
#               for i in my_list:
#                             long = my_list[0]
#                             if len(i) > len(long):
#                                     best = len(i)
#               return best
# my_list = ["first", "second", "fourth", "eleventh"]
# result = length_of_longest(my_list)
# print(result)
                        
# # The shortest in the list
# def shortest(mylist :list):
#               my_list = ["first", "second", "fourth", "eleventh"]
#               for i in my_list:
#                             short = my_list[0]
#                             if len(i) < len(short):
#                                     short = i
#               return short
# my_list = ["first", "second", "fourth", "eleventh"]
# result = shortest(my_list)
# print(result)

# All the longest in the list (NOT completed)
# my_list = ["first", "second", "fourth", "eleventh"]
# newlist = []
# long = my_list[0]
# for i in my_list:
#               if len(i) > len(long):
#                       long = i
#               elif len(i) == len(long):
#                       longest = i
# newlist.append(long,longest)
# print(newlist)

'''
NOTE: Print statement formatting
print("hello" + 37) DON'T WORK   print("hello" + str(37)) WORK
print("Hi", name, "your age is", age, "years", sep="\n")   sep="" stands for seperator
print(f"The number is {number:.2f}")
is in for Regex cna be used
isupper() return true if string consists of only upper case characters
NOTE: print("XYZ".isupper())   / TRUE
is_it_upper = "Abc".isupper()  / FALSE (THIS METHOD IS WRONG)
'''
# name = "Mahdi"
# age = 33
# print("Hi", name, "your age is", age, "years", sep="\n") 

# print("Hi ", end="")
# print("there!")            
# print(f"Hi {name} your age is {age} years")
# number = 1/3
# print(f"The number is {number:.2f}")


# names =  [ "Steve", "Jean", "Katherine", "Paul" ]
# for name in names:
#   print(f"{name:15} centre {name:>15}")

'''
 NOTE: More strings and lists
 NOTE: Strings are immutable
'''
# Slicing
# my_string = "exemplary"
# my_list = ["Hi", "there", "example", "one more"]
# print(my_string[::-1])

#  Everything reversed
# def everything_reversed(my_list : list) -> list:
#               list2= []
#               for i in my_list:
#                       list2.append(i[::-1])
#               return list2[::-1]
# my_list = ["Hi", "there", "example", "one more"]
# print(everything_reversed(my_list))

# More methods for lists and strings
#  Count  (Return the number of times the value  appears in the list)
# my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
# print(my_string.count("ch"))
# my_list = [1,2,3,1,4,5,1,6]
# print(my_list.count(1))
# # Replace
# my_string = "Hi there"
# new_string = my_string.replace("Hi", "Hey")
# print(new_string)

# Most common character (not throughly completed)
# srin = "abcdbde"
# max = 0
# newList= []
# pepe = ""
# max = srin.count(srin[0])
# # newList.append(srin[0])
# for i in srin:
#               if srin.count(i) > max:
#                       max = srin.count(i)
#                       pepe = i
#               else:
#                       pepe = srin[0]
# if len(pepe) > 0:
#         newList.append(pepe)
# print(str(newList))
# print(srin.count('e'))

# No vowels allowed
# def no_vowel(name : str) -> str:
#         new_name = ""
#         for i in name:
#                 if i not in "aeiou":
#                         new_name += i
#         return new_name
# my_string = "this is an example"
# print(no_vowel(my_string))

# No shouting allowed
# print("XYZ".isupper())

# is_it_upper = "Abc".isupper()
# print(is_it_upper)

# No shouting allowed
# def no_shouting(shout : list) -> list:
#               newList = []
#               for i in shout:
#                       if not i.isupper():
#                             newList.append(i)
#               return newList
# my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
# pruned_list = no_shouting(my_list)
# print(pruned_list)

# Neighbours in a  (NOT COMPLETED. chellenging)

# PROJECT: Grade statistics
total = input("Exam points and exercises completed: ")
splited = total.split(" ")
points = int(splited[0])
excercises = int(splited[1])
print(points)
print(excercises)



