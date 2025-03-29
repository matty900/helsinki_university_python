import math
from fractions import Fraction
from datetime import date
dir(Fraction)
'''
Objects and methods
.value() - .find() - .count() - 
NOTE: strings in Python are immutable. This does not apply to all methods, however. Python lists are mutable

MODULE, CLASS, OBJECT, ATTRIBUTE, METHOD, VARIABLE

from datetime import date // datetime MODULE , date CLASS

xmas_eve = date(2020, 12, 24) // xmas_eve OBJECT of class
midsummer = date(2020, 6, 20)  // midsummer OBJECT of class

# calling a method
weekday = xmas_eve.isoweekday()

# accessing a variable
my_month = xmas_eve.month

# print only the month attribute of both objects
print(xmas_eve.month)  // ATTRIBUTE of the object
print(midsummer.month)
'''
name = "In Search of Lost Typing"
author = "Marcel Pythons"
year = 1992

book1 = {"name": name, "author": author, "year": year}
book2 = {"name": "alex", "author": "alex", "year": 1721}
# print(book1["name"])
# print(book2["name"])
# for i in book1:
#         print(book1[i])
#         print(i)

#  Instead of methods above using .values() to print values in an object
# for value in book1.values():
# print(value)

# print("Irreverent Irises in Islington".count("I"))
# print("Irreverent Irises in Islington".find("I"))


def smallest_average(person1: dict, person2: dict, person3: dict):
    sum = 0
    sum = person1["result1"] + person1["result2"] + person1["result3"]
    if person2["result1"] + person2["result2"] + person2["result3"] < sum:
        result = person2
    elif person3["result1"] + person3["result2"] + person3["result3"] < sum:
        result = person1
    else:
        result = person1
    return result


person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))

my_matrix = [[1, 2], [3, 4]]


def row_sums(my_matrix: list):
    for i in my_matrix:
        total = sum(i)
        i.append(total)


my_matrix = [[1, 2], [3, 4]]
row_sums(my_matrix)
# print(my_matrix)
# Fraction class from the module fractions
frac = Fraction(3, 4)
# print(frac)


# List of years
def list_years(dates: list):
    dates = []
    dates = [int(date1.year), int(date2.year), int(date3.year)]
    dates.sort()
    print(dates)


date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

# years = list_years([date1, date2, date3])
# print(years)

# Shopping list  (not accessible)

'''
NOTE: CLASS

1. Definfing class : strcuture of the class (attributes)
2. Defining methods: methods(functions) of the class 
'''

'''1'''


class BankAccount:
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner


# peter_account = BankAccount()
# The data attributes are available only through the object they are attached to. print(balance) Cause an error
# peter_account.owner = "peter parker"
# peter_account.balance = 5.0
# INSTEAD of above method we use the following method
peters_account = BankAccount(100, "Peter Python")
paulas_account = BankAccount(20000, "Paula Pythons")
# print(paulas_account.balance)
# print(peters_account.balance)

# Book
# Book = {
#                 "name" : "Art of fucking ",
#                 "author" : "Mark Manson",
#                 "genre" : "self-help",
#                 "year" : "2013"
#         }
# for key in Book:
#         print(Book[key])
# print(Holy)


class Book:
    name = None

    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)


# print(f"{python.author}: {python.name} ({python.year})")
# print(f"The genre of the book {everest.name} is {everest.genre}")

# Define class: Pet
class Pet:
    def __init__(self, name, species, year_of_birth):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth


def new_pet(name: str, species: str, year_of_birth: int):
    return Pet(name, species, year_of_birth)


fluffy = new_pet("Fluffy", "dog", 2017)
# print(fluffy.name)
# print(fluffy.species)
# print(fluffy.year_of_birth)

# The Older Book


def older_book(book1: Book, book2: Book):
    if book1.year < book2.year:
        print(f"{book1.name}is older, it was published it {book1.year}")
    elif book1.year > book2.year:
        print(f"{book2.name}is older, it was published it {book2.year}")
    else:
        print(f'{book1.name} and  {book2.name}were published in {book2.year}')
# older_book(python, everest)
# older_book(python, norma)

# Books of a genre


def books_of_genre(books: list, genre: str):
    new_books = []
    for book in books:
        if genre in book.genre:
            new_books.append(book)
    return new_books


books = [python, everest, norma, Book(
    "The Snowman", "Jo Nesbø", "crime", 2007)]
# print("Books in the crime genre:")
# for book in books_of_genre(books, "crime"):
#     print(f"{book.author}: {book.name}")


'''Defining methods
Class: attributes (data) & methods (functions)'''
# Decreasing counter


class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1
        else:
            self.value = 0

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.original_value
# Part 1
# counter = DecreasingCounter(80)
# counter.print_value()
# counter.decrease()
# counter.print_value()
# counter.decrease()
# counter.print_value()
# counter.decrease()
# counter.print_value()
# counter.reset_original_value()
# counter.print_value()

# First and last name


class Person:
    def __init__(self, initial_name: str):
        self.original = initial_name
        self.name = initial_name

    def return_first_name(self):
        words = self.original.split(" ")
        return words[0]

    def return_last_name(self):
        words = self.original.split(" ")
        return words[1]
    # def print_name(self):
    #        print("name:", self.name)
# peter = Person("Peter Pythons")
# print(peter.return_first_name())
# print(peter.return_last_name())

# Statistics on numbers


class NumberStats:
    def __init__(self):
        self.added = 0
        self.numbers = 0
        self.sum = 0

    def add_number(self, number: int):
        self.added += 1
        self.sum += number

    def count_numbers(self):
        return self.added

    def get_sum(self):
        if self.sum > 0:
            return self.sum
        else:
            return 0

    def average(self):
        if self.added > 0:
            mean = self.sum / self.added
            return mean
        else:
            return 0


# stats = NumberStats()
# # stats.add_number(3)
# # stats.add_number(5)
# # stats.add_number(1)
# # stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())

'''More examples of classes'''
# Stopwatch


class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

    def tick(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
# watch = Stopwatch()
# for i in range(100):
#     print(watch)
#     watch.tick()

# Clock


class Clock:
    def __init__(self, init_hours, init_mitues, init_seconds):
        self.hours = init_hours
        self.minutes = init_mitues
        self.seconds = init_seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def tick(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1
                if self.hours >= 24:
                    self.hours = 0
# clock = Clock(23, 59, 55)
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)

# LunchCard


class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        lunch_price = 2.60
        if self.balance > lunch_price:
            self.balance -= lunch_price

    def eat_special(self):
        special_price = 4.60
        if self.balance > special_price:
            self.balance -= special_price

    def deposit_money(self, deposit):
        if deposit < 0:
            raise ValueError("Deposit amount cannot be nagative")
        self.balance += deposit

    def balancing(self):
        return f"{self.balance}"


# peter = LunchCard(20)
# grace = LunchCard(30)
# peter.eat_special()
# grace.eat_lunch()
# print(f"peter: {peter.balancing()}")
# print(f"grace: {grace.balancing()}")
# peter.deposit_money(20)
# grace.eat_special()
# print(f"peter: {peter.balancing()}")
# print(f"grace: {grace.balancing()}")


# Series
class Series:
    def __init__(self, name: str, seasons: int, genre_list: list):
        self.name = name
        self.seasons = seasons
        self.genres = ", ".join(genre_list)
        self.ratings = []

    def __str__(self):
        if not self.ratings:
            return f"{self.name} ({self.seasons} seasons) \ngenres: {self.genres}\nno ratings"
        else:
            average = sum(self.ratings) / len(self.ratings)
            return f"{self.name} ({self.seasons} seasons) \ngenres: {self.genres}\n{len(self.ratings)} ratings, average {average:.1f} points"

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)


def minimum_grade(rating: float, series_list: list):
    if rating in series_list:
        return True


s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)
