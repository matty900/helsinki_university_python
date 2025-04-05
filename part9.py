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


room = Room()

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))
room.print_contents()

print()

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")

print()

room.print_contents()
