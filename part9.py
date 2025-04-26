'''Objects and references'''
# The fastest car


class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed


def fastest_car(cars: list):
    high_speed = cars[0].top_speed
    high_model = cars[0].make
    for car in cars:
        if car.top_speed > high_speed:
            high_speed = car.top_speed
            high_model = car.make
    return high_model


# car1 = Car("Saab", 195)
# car2 = Car("Lada", 110)
# car3 = Car("Ferrari", 280)
# car4 = Car("Trabant", 85)
# cars = [car1, car2, car3, car4]
# print(fastest_car(cars))

# Passing submissions


class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points


def passed(submissions: list, lowest_passing: int):
    passed_ones = []
    for submit in submissions:
        if submit.points >= lowest_passing:
            passed_ones.append(
                "examinee "+str(submit.examinee) + " points " + str(submit.points))
    return passed_ones


s1 = ExamSubmission("Peter", 12)
s2 = ExamSubmission("Pippa", 19)
s3 = ExamSubmission("Paul", 15)
s4 = ExamSubmission("Phoebe", 9)
s5 = ExamSubmission("Persephone", 17)
passes = passed([s1, s2, s3, s4, s5], 15)
# for passing in passes:
#     print(passing)

'''
is : used for checking if the two references refer to the exact same object
== : if the contents of the objects are the same
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 is list2) // False
print(list1 is list3)  // True
print(list1 == list2)  // True
1. if you need helper variables for use within a single method, the correct way to do it is without self
2. Objects as arguments to functions:  def change_name(student: Student): student.name = "Saul Student"
3. Create objects within functions: def new_student():     return Student(name, student_number)
NOTE:
Functions: These are independent blocks of code that perform specific tasks.
Methods: These are functions that are specifically defined within a class
Attribute: Variable inside a class
Variable: container in computer's memory.

4. Objects as arguments to methods:
'''
# Baby Centre


class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class BabyCentre:
    def __init__(self):
        self.weight = 0
        pass

    def weigh(self, person: Person):
        self.weight += 1
        return person.weight

    def feed(self, person: Person):
        person.weight += 1

    def weigh_ins(self):
        return self.weight


# baby_centre = BabyCentre()

# eric = Person("Eric", 1, 110, 7)
# peter = Person("Peter", 33, 176, 85)

# print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

# baby_centre.weigh(eric)
# baby_centre.weigh(eric)

# print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

# baby_centre.weigh(eric)
# baby_centre.weigh(eric)
# baby_centre.weigh(eric)
# baby_centre.weigh(eric)

# print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

# LunchCard and PaymentTerminal
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        check = amount < self.balance
        if self.balance > amount:
            self.balance -= amount
        return check


class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        lunch = 2.5
        if payment >= lunch:
            self.lunches += 1
            self.funds += 2.50
            return payment - lunch
        else:
            return 0.0

    def eat_special(self, payment: float):
        special = 4.3
        if payment >= special:
            self.specials += 1
            self.funds += 4.30
            return payment - special
        else:
            return 0.0
    
    def eat_lunch_lunchcard(self, card: LunchCard):
        lunch = 2.5
        if card.balance > lunch:
            self.lunches += 1
            card.balance -= lunch
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        special = 4.3
        if card.balance > special:
            self.specials += 1
            card.balance -= special
            return True
        else:
            return False
    
    def deposit_money_on_card(self, card: LunchCard, amount: float):
        self.funds += amount
        card.balance += amount

# exactum = PaymentTerminal()

# card = LunchCard(2)
# print(f"Card balance is {card.balance} euros")

# result = exactum.eat_special_lunchcard(card)
# print("Payment successful:", result)

# exactum.deposit_money_on_card(card, 100)
# print(f"Card balance is {card.balance} euros")

# result = exactum.eat_special_lunchcard(card)
# print("Payment successful:", result)
# print(f"Card balance is {card.balance} euros")

# print("Funds available at the terminal:", exactum.funds)
# print("Regular lunches sold:", exactum.lunches)
# print("Special lunches sold:", exactum.specials)


# An instance of the same class as an argument to a method
#  calling a method differs from calling a function. A method is attached to an object with the dot notation:
# NOTE: if the parameter in a method definition is of the same type as the class itself, 
# the type hint must be enclosed in quotation marks
#   def older_than(self, another: "Person"):   TRUE
#   def older_than(self, another: Person):     FALSE 

# Comparing properties
class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
    def bigger(self, another: "RealProperty"):
        return self.square_metres > another.square_metres
    def price_difference(self, compared_to:"RealProperty"):
        return abs((self.price_per_sqm * self.square_metres) - (compared_to.price_per_sqm * compared_to.square_metres))
    def more_expensive(self, compared_to:"RealProperty"):
        return self.price_per_sqm < compared_to.price_per_sqm
    

# central_studio = RealProperty(1, 16, 5500)
# downtown_two_bedroom = RealProperty(2, 38, 4200)
# suburbs_three_bedroom = RealProperty(3, 78, 2500)

# print(central_studio.bigger(downtown_two_bedroom))
# print(suburbs_three_bedroom.bigger(downtown_two_bedroom))
# print(central_studio.price_difference(downtown_two_bedroom))
# print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))
# print(central_studio.more_expensive(downtown_two_bedroom))
# print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))


''' Objects as attributes '''

# Pets
class Pet:
    def __init__(self, name : str , model: str):
        self.name = name
        self.model = model
    def __str__(self):
        return f"Pet(name='{self.name}', model='{self.model}')"
class Person:
    def __init__(self, name: str, pet : Pet):
        self.name = name
        self.pet = pet
    def __str__(self):
        return f"Person(name='{self.name}', pet={self.pet})"

# hulda = Pet("Hulda", "mixed-breed dog")
# levi = Person("Levi", hulda)
# print(levi)

# A box of presents
class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return f"Present{self.name} ({self.weight}kg)"

class Box:
    def __init__(self):
        self.box = []
        # self.tota_weight = []  Gives wrong answer
    
    def __str__(self):
        return f"{self.tota_weight}"

    def add_present(self, present: Present):
        self.box.append(present)
        # print(box)
        

    def total_weight(self):
        tota_weight = []   # local varibale is the answer
        for i in self.box:
            tota_weight.append(i.weight)
        return sum(tota_weight)

# book = Present("ABC Book", 2)

# box = Box()
# box.add_present(book)
# print(box.total_weight())

# cd = Present("Pink Floyd: Dark Side of the Moon", 1)
# box.add_present(cd)
# print(box.total_weight())

# The shortest person in the room

class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def __str__(self):
        return f"{self.name} {self.height}"
class Room:
    def __init__(self):
        self.persons= []
    
    def add(self,person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) > 0
    
    def print_contents(self):
        for person in self.persons:
            print(person)
            
        total_height = sum(person.height for person in self.persons)
        num_persons = len(self.persons)

        print(f"There are {num_persons} persons in the room, and their combined height is {total_height} cm")
        for person in self.persons:
            print(person)

    def shortest(self):
        if not self.persons:  
            return None
        shortest_person = self.persons[0] 
        for person in self.persons:
            if person.height < shortest_person.height:
                shortest_person = person
        return shortest_person.name 
    
    def remove_shortest(self): # Removing a person from the room (Need to be compeleted)
        if not self.persons:  
            return None
        shortest_person = self.persons[0] 
        for person in self.persons:
            if person.height < shortest_person.height:
                shortest_person = person
        self.persons.remove(shortest_person)
        return shortest_person


# room = Room()

# room.add(Person("Lea", 183))
# room.add(Person("Kenya", 172))
# room.add(Person("Nina", 162))
# room.add(Person("Ally", 166))
# room.print_contents()

# print()

# removed = room.remove_shortest()
# print(f"Removed from room: {removed.name}")

# print()

# room.print_contents()

''' ** Encapsulation **
In object oriented programming the term client refers to a program which uses a class, or instances of a class
Final goal:
1. the use of a class and/or objects is as simple as possible from the client's point of view
2. integrity of any object is preserved all time => direct access to class attributes(variables) is not possible. ONLY through it's methods(functions)
Hiding these attributes from clinet achieved by using __ to the beginning of the attribute name => 
class CreditCard:
    def __init__(self, number: str, name: str):
        self.__number = number  # encapsulation (this attribute is hidden)
        self.name = name
Getter  @property   and Setter @methodname.setter
'''
# Car
class Car:
    def __init__(self):
        self.__amount = 0
        self.__odometer = 0
    def fill_up(self):
            self.__amount = 60
    def drive(self, km):
        if km < self.__amount:
            self.__odometer += km
            self.__amount -= km
        else:
            self.__odometer = 60
            self.__amount = 0
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__amount} litres"
    
# car = Car()
# print(car)
# car.fill_up()
# print(car)
# car.drive(20)
# print(car)
# car.drive(50)
# print(car)
# car.drive(10)
# print(car)
# car.fill_up()
# car.fill_up()
# print(car)

# Recording
class Recording:
    def __init__(self, length):
        self.__length = length
    def __str__(self):     # Instead of __str__  we simply can use the instance 
        return f"{self.__length}"
    @property            # Getter
    def length(self): 
        return self.__length
    @length.setter       # Setter
    def length(self, length ):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("the length cannot be negative")

the_wall = Recording(43)
# print(the_wall)
# print(the_wall.length)
# the_wall.length = 44
# print(the_wall.length)



# NOTE: Encapsulation is mainly for hiding attributes from clinet and make them accessibe only thorugh getter and setters
# WITH ENCAPSULATION
class Player:
    def __init__(self,name, age):
        self.__name = name
        self.age = age
    @property   
    def name(self):
        return self.__name
     
    def __str__(self):
        return f"{self.__name} : {self.age}"
    
# plyer1 = Player("alice",22)
# print(plyer1.name)  # by removing getter name won't be displayed because of hidden feature of __name attribute
# print(plyer1)       # Yet, for displaying the whole instance of the class we need __str__  

# WITHOUT ENCAPSULATION
class Player:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
# plyer1 = Player("alice",22)  # can access the 
# print(plyer1.name)


# NOTE: the difference between def owner(self, owner): and   def add_entry(self, entry: str): 
# even though they both add value to private or encapsulated attributes
# is that : with setter we can assign a value like a normal attribute such as 
# : dairy.owner = "Mahdi" instead of diary.set_owner("")
class Diary:
    def __init__(self, owner: str):
        self.__owner = owner
        self.__entries = []

    @property
    def owner(self):
        return self.__owner

    @owner.setter   
    def owner(self, owner):
        if owner != "":
            self.__owner = owner
        else:
            raise ValueError("The owner may not be an empty string")

    def add_entry(self, entry: str):
        self.__entries.append(entry)

    def print_entries(self):
        print("A total of", len(self.__entries), "entries")
        for entry in self.__entries:
            print("- " + entry)

# Weather station
class WeatherStation:
    def __init__(self, station):
        self.station = station
        self.observations = []

    def add_observation(self, observation: str):
        self.observations.append(observation)

    def latest_observation(self):
        if self.observations:
            return self.observations[-1]
        else:
            return "nothing found"
    def number_of_observations(self):
        return len(self.observations)
    def __str__(self):
        return f"{self.station} , {len(self.observations)} observations"

# station = WeatherStation("Houston")
# station.add_observation("Rain 10mm")
# station.add_observation("Sunny")
# print(station.latest_observation())

# station.add_observation("Thunderstorm")
# print(station.latest_observation())

# print(station.number_of_observations())
# print(station)

''' Scope of methods 
the goal is to hiding the methods in the class as attributes in the encapsulation section
'''

# Service charge
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    def __service_charge(self):
        self.__balance -= self.__balance * 0.01

    def deposit(self, amount:float):
        self.__balance +=  amount
        self.__service_charge()

    def withdraw(self, amount:float):
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance


# account = BankAccount("Randy Riches", "12345-6789", 1000)
# account.withdraw(100)
# print(account.balance)
# account.deposit(100)
# print(account.balance)

'''Class attributes
class variable: 
class SavingsAccount:
    general_rate = 0.03
    1. defined within the class, but outside any mehtod definations,  
    2. it does not use self prefix.
    3. accessed through the name of the class SavingsAccount.general_rate
NOTE: class variable or methods are not attached to any instance of the class 
Class method (@classmethod):
cls in here is look like the self parameter
NOTE: The difference is that cls points to the class while self point to an instance of the class
    @classmethod
    def license_plate_valid(cls, plate: str):
        if len(plate) < 3 or "-" not in plate:
            return False
'''

# Postcodes
class City:
    # class variable
    postcodes = {"Helsinki": "00100", "Turku" : "20100" , "Tampere" : "33100", "Rovaniemi": "96100", "Oulu": "90100"}

# # ListHelper
# class ListHelper:
#     @classmethod
#     def greatest_frequency(cls, my_list: list):
#         for i in my_list:
#             for j in 
class ListHelper:
    def __init__(self):
        self. most_common_count = 0
        self. most_common_item = None
        self. appear_twice_item = None
        self.counts = {}
    @classmethod
    def greatest_frequency(cls,my_list: list):
        cls.counts = {}
        for number in my_list:
            if number in cls.counts:
                cls.counts[number] += 1
            else:
                cls.counts[number] = 1
        for key in cls.counts:
            if cls.counts[key] == 2:
                cls.appear_twice_item = key

    @classmethod
    def doubles(cls,my_list: list):
        for  key in cls.counts:
            if cls.counts[key]  > cls.most_common_count:
                cls.most_common_count = cls.counts[key] 
                cls.most_common_item = key

numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
# print(ListHelper.greatest_frequency(numbers))
# print(ListHelper.doubles(numbers))


# NOTE: These two methods are identical 
# for key in counts:
#     print(counts[key]) # value
# for key in counts:
#     print(key)  # key
# for key, value in counts.items():
#     print(key)
    # print(value)

# print(counts)


# FIRST WAY


# SECOND WAY
# for number, count in counts.items():
#     print(count)
#     if count > most_common_count:
#         most_common_count = count
#         most_common_item = number



'''More examples with classes
class default value of parameters
  class Student:
    def __init__(self, name: str, student_number: str, credits: int = 0, notes: str = ""):
NOTE: 
A) In order: student2 = Student("Sassy Student", "54321", 25)
B) IF the order not followed it should be named: student4 = Student("Sandy", "98765", notes="absent in academic year 20-21")
'''
# Item, Suitcase and Cargo hold
class Item:
    def __init__(self, name, weight ):
        self.__name = name
        self.__weight = weight
    
    # no using @property
    def name(self):
        return self.__name  
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.name()} {self.weight()}kg" # instead of self.name self.weight


class Suitcase:
    def __init__(self, max_weight):
        self.__max_weight = max_weight  # max weight allowed
        self.__current_weight = 0       # total weight so far
        self.__count = 0                # number of items added
        self.__items = [] 
        self.__heaviest = 0
        self.__heavy = []

    def add_item(self, item: Item):
        if self.__current_weight + item.weight() <= self.__max_weight:
            self.__items.append(item)
            self.__current_weight += item.weight()
            self.__count += 1
        if item.weight() > self.__heaviest:
            self.__heaviest = item.weight() 
            self.__heavy.append(item)
    
    def weight(self):
        return self.__current_weight

    def print_items(self):
         for item in self.__items:
            print(item)

    def heaviest_item(self):
        if self.__heavy:
            return self.__heavy[-1]
        else:
            return None
    
    def get_items(self): # Public method to access the list of items in another class (CargoHold class)
        return self.__items

            
    def __str__(self):
        if self.__count == 1 :
                 return f"{len(self.__items)} item ({self.__current_weight} kg)"
        else:
                return f"{len(self.__items)} items ({self.__current_weight} kg)"
        
class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.cargos = []
        self.cargo_count = 0
    def add_suitcase(self, suitcase: Suitcase):
        for  item in suitcase.get_items(): # use the public method from Item class to access the list of items
            self.cargos.append(item)
        self.__max_weight -= suitcase.weight()
        self.cargo_count += 1
    def __str__(self):
        for i in self.cargos:
            print(i)
        return f"{self.cargo_count} for {self.__max_weight}" 
    def print_items(self):
        for cargo in self.cargos:
            print(cargo)


book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()
