# ############################################Tip calculator ###############################################
import random

# print("Welcome to the tip calculator.")
# bill = int(input("What was the total bill? $"))
#
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# tip_as_percent = tip / 100
#
# ammount = tip_as_percent * bill
# total_bill = bill + ammount
# no_of_people = int(input("How many people to split the bill? "))
#
# cash = total_bill/no_of_people
#
# message = round(cash, 2)
# print(f"Each person should pay ${message}")
#

################################################ Years remaining ###########################################

#
# age = int(input("What is your current age? "))
#
#
# years_remaining = 90 - age
#
#
# year = 365 * years_remaining
#
# month = 12 * years_remaining
#
# week = 52 * years_remaining
#
# print(f"You have {year} days, {week} weeks and {month} months left till 90 years old")
#

#######################################################love project#################################################



#
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
#
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
#
# true = t + r + u + e
#
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
#
# love = l + o + v + e
#
# score = str(true) + str(love)
#
# if int(score < 10) or int(score > 90):
#     print(f"Your score is {score}, you go together like coke and mentos.")
#
# elif int(score <= 50) and int(score >= 40):
#     print(f"Your score is {score}, you are alright together")
#
# else:
#     print(f"Your score is {score}")





###################################################treasure island#################################################

#
#
# print("Welcome to Treasure Island.\nYour mission is to find the treasure. ")
# goTo = input('You are at a crossroad. Where do you want to go? Type "left" or "right"\n ').lower()
#
# if goTo == "left":
#     lake = input('You come to a lake, There is an Island in the middle of the lake. Type "wait" to wait for a boat. Type "Swim" to swim across\n').lower()
#     if lake == "wait":
#         door = input("You arrive at the Island unharmed. There is a house with 3 doors. One red, One yellow and One blue. Which colour do you chose?\n").lower()
#         if door == "red":
#             print("The room is full of fire. Game Over!")
#
#         elif door == "yellow":
#             print("You found the treasure. Congratulations!")
#
#         elif door == "blue":
#             print("You entered a room full of beasts. Game Over!")
#         else:
#             print("You chose a door that does not exist. Game Over!")
#     else:
#         print("You drowned, Game Over")
# else:
#     print("Game Over!")
#



####################################################### Tails or Heads Exercise######################################

# import random
#
#
# test_seed = int(input("Create a seed number:  "))
# random.seed(test_seed)
#
# random_side = random.randint(0, 1)
#
# if random_side == 0:
#     print("Heads")
# else:
#     print("Tails")
#


################################################### Who's paying?######################################################

#
# import random
#
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
#
# namesAsCSV = input("Give me everybody's names, separated by a comma. ")
# names = namesAsCSV.split(", ")
# num_items = len(names)
# payer = names[random.randint(0, num_items - 1)]
#
# print(f"The person that will pay the money is {payer}")
#





#######################################################Treasure Map#####################################################

# import random
#
# row1 = ["☐", "☐", "☐"]
# row2 = ["☐", "☐", "☐"]
# row3 = ["☐", "☐", "☐"]
#
# map = [row1, row2, row3]
#
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure?  ")
#
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# map[vertical - 1][horizontal - 1] = "X"
#
#
# print(f"{row1}\n{row2}\n{row3}")



############################################### Rock, Paper, Scissors##################################################
# import random
# from ascii import rock, paper, scissors
#
#
# game_images = [rock, paper, scissors]
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
# print(game_images[user_choice])
#
# computer_choice = random.randint(0, 2)
# print(f"Computer chose:")
# print(game_images[computer_choice])
#
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw")


##########################################################Average heights###########################################
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# total_heights = 0
# for height in student_heights:
#     total_heights += height
# print(total_heights)
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
#
# average_height = round(total_heights/number_of_students)
# print(average_height)





#######################################################Highest Score#################################################
#
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
#
# max_score = 0
# for score in student_scores:
#     if score >= max_score:
#         max_score == score
# highest_score = score
# print(f"The highest score in the class is: {highest_score}")
#

#######################################################Adding evens exercise#########################################
#
# even_number = 0
# for i in range(0, 10, 2):
#     even_number += i
# print(even_number)





#####################################################Fizz Buzz Exercise###########################################
#
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)




####################################################Password Generator##########################################
# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#
# password = ""
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char
#
# for sym in range(1, nr_symbols + 1):
#     random_sym = random.choice(symbols)
#     password += random_sym
#
# for num in range(1, nr_numbers + 1):
#     random_num = random.choice(numbers)
#     password += random_num
# print(password)




# Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# password_list = []
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password_list.append(random_char)
#
# for sym in range(1, nr_symbols + 1):
#     random_sym = random.choice(symbols)
#     password_list.append(random_sym)
#
# for num in range(1, nr_numbers + 1):
#     random_num = random.choice(numbers)
#     password_list.append(random_num)
#     random.shuffle(password_list)
#
# password = ""
# for char in password_list:
#     password += char
# print(f"This is your password: {password}")
#
#

###########################################################Hangman Project###############################################
#
# import random
#
#
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
#
#
#
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# lives = 6
#
# display = []
# for _ in range(word_length):
#     display += "_"
#
#
# end_of_game = False
#
# while not end_of_game:
#
#     user_guess = input("Guess a letter: ").lower()
#
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == user_guess:
#             display[position] = letter
#     print(display)
#
#     if user_guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#
#     if "_" not in display:
#         end_of_game = True
#         print("You win")
#
#
#     print(stages[lives])





# #################################################################Paint Area calculator############################################
#
# import math
#
# def paint_calc(height, width, cover):
#     number_of_can = (height * width)/cover
#     total = math.ceil(number_of_can)
#     print(f"You'll need {total} cans of paint")
#
# test_h = int(input("Height of the wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height= test_h, width= test_w, cover=coverage)
#



#######################################################Prime Number Checker#####################################
#
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number - 1):
#         if number % i == 0 :
#             is_prime = False
#     if is_prime:
#             print("It's a prime number")
#     else:
#             print("It's not a prime number")
#
# n = int(input("Check this number: "))
# prime_checker(number=n)
#
#
#


########################################################Caesar Cipher################################################

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Reorganised code
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"Here's the {cipher_direction}d result: {end_text}")
#
#
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#
#     shift = shift % 25
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#
#     result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if result == "no":
#         should_continue = False
#         print("Goodbye")

# Unorganized code
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decoded text is {cipher_text}")
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)
# else:
#     print("Try again")


####################################################Grading Program#################################################

#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
#
# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score >= 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)
#




##################################################Days in Month####################################################
#
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month():
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month -1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)




###############################################       Calculator         ###########################################

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbols = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_functions = operations[operation_symbols]
        answer = calculation_functions(num1, num2)

        print(f"{num1} {operation_symbols} {num2} = {answer}")
        if input(f"Type 'y' to calculating with answer {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()










