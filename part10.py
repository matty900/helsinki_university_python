import random
'''Class hierarchies'''
'''
 inheritance: A class can inherit the methods of another class. 
 In addition to these inherited methods a class can also contain methods which are unique to it.
class Person:

   def __init__(self, name: str, email: str):
       self.name = name
       self.email = email

   def update_email_domain(self, new_domain: str):
       old_domain = self.email.split("@")[1]
       self.email = self.email.replace(old_domain, new_domain)


class Student(Person): # to access the other class attributes we simply put their name in peranthesis

   def __init__(self, name: str, id: str, email: str, credits: str):
       self.name = name
       self.id = id
       self.email = email
NOTE: A derived class inherits all methods from its base class.Those methods are directly accessible in the derived class, 
unless they have been defined as private in the base class (with two underscores before the name of the method).
class Bookshelf(BookContainer):

   def __init__(self):
       super().__init__()

'''
# Laptop computer
class Computer:
              def __init__(self, model, speed):
                      self.model = model
                      self.speed = speed
              def __str__(self):
                      return f"{self.model}, {self.speed} MHz"
class LaptopComputer(Computer):
        def __init__(self, model, speed, weight):
                super().__init__(model, speed)
                self.weight = weight
        def __str__(self):
                return f"{super().__str__()}, {self.weight}kg"

# laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
# print(laptop)

# Game Museum
class ComputerGame:
        def __init__(self, name , company, year):
                self.name = name
                self.company = company
                self.year = year
class GameWarehouse:
        def __init__(self):
                self.computer_games = []
        def add_game(self,computergame:ComputerGame):
                self.computer_games.append(computergame)
        def list_games(self):
                return self.computer_games
class GameMuseum(GameWarehouse):
        def __init__(self):
                super().__init__()
        def add_game(self, computergame):
                 games = super().add_game(computergame)
        def list_games(self):
                games =  super().list_games()
                old_games = []   
                for game in games:
                        if game.year < 1990:
                                old_games.append(game)
                return old_games

        # museum = GameMuseum()
        # museum.add_game(ComputerGame("Pacman", "Namco", 1980))
        # museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
        # museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
        # for game in museum.list_games():
        #     print(game.name)
        

# Areas
class Rectangle:
        def __init__(self, length, width):
                self.length = length
                self.width = width
        def __str__(self):
                return f"rectangle {self.length} X {self.width}"
        def area(self):
                return self.width * self.length
class Square(Rectangle):
        def __init__(self, length): # by doing this we passed the parent class one arguemnt as two
                super().__init__(length,length)  
        def __str__(self):  # overriding the str for inherited class
                return f"square {self.length}x{self.width}"
        # No need to override the area function from base class 

# square = Square(4)
# print(square)
# print("area:", square.area())

# Word game

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                print("tie")
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
       def __init__(self, rounds):
              super().__init__(rounds)
       def round_winner(self, player1_word: str, player2_word: str):
                    if len(player1_word) > len(player2_word):
                           return 1
                    elif len(player1_word) < len(player2_word):
                           return 2
                    else:
                           pass
class MostVowels(WordGame):
         def __init__(self, rounds):
              super().__init__(rounds)
         def round_winner(self, player1_word: str, player2_word: str):
                    vowels = "aeiouAEIOU"
                    count1 = sum(1 for char in player1_word if char in vowels)
                    count2 = sum(1 for char in player2_word if char in vowels)
                    if count1 > count2:
                           return 1
                    elif count1 < count2:
                           return 2
                    else:
                           pass        
class RockPaperScissors(WordGame):
         def __init__(self, rounds):
              super().__init__(rounds)
         def round_winner(self, player1_word: str, player2_word: str):
                    result = 0
                    if player1_word == 'rock' and player2_word == 'scissors':
                           result = 1
                    elif player1_word == 'paper' and player2_word == 'rock':
                           result = 1
                    elif player1_word == 'scissors' and player2_word == 'paper':
                           result = 1
                    elif player1_word == 'scissors' and player2_word == 'rock':
                           result = 2
                    elif player1_word == 'rock' and player2_word == 'paper':
                           result = 2
                    elif player1_word == 'paper' and player2_word == 'scissors':
                           result = 2
                    else:
                           pass
                    return result

game = int(input("select the game: 1. default 2.longestWord 3.MostVowels 34.RockPaperScissors:\n"))     
if game == 1:
       p = WordGame(3)
elif game == 2:
       p = LongestWord(3)
elif game == 3:
       p = MostVowels(3)
elif game == 4:
       p = RockPaperScissors(4)
else:
       print("select the proper option ")                        
p.play()