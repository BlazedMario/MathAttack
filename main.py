
 

print("\033[1;36;1m  \n")
#imports
import random
import time


#Variables
correct_answers = 0
wrong_answers = 0
yes_no_var = 0
#functions
def question_creator():
  global first_number
  global second_number
  if difficulty_of_questions == 1:

    first_number = random.randint(0,20)
    second_number = random.randint(0,20)
  elif difficulty_of_questions == 2:
    first_number = random.randint(0,50)
    second_number = random.randint(0,50)

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        global yes_no_var

        if response == "yes" or response == "y":
            response = "yes"
            yes_no_var = 0
            return response
            print("yes")
            
        elif response == "no" or response == "n":
            response = "no"
            yes_no_var = 1
            return response
        else:
            print("Please answer yes / no")

def num_check(question, low, high):
    error = "\033[1;31;1m""Please enter a whole number between " + str(low) + " and " + str(high) + "\n" + "\033[1;36;1m  \n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low <= response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

def statement_generator(statement, decoration):
  sides = decoration * 3
  statement = "{} {} {}".format(sides, statement,sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return " "

#Welcome
statement_generator("welcome to mathAttack", "☆")
print(" ")

#lists
difficulty_levels = ["1","2","3"]

#Tutorial
time.sleep(1)
yes_no("Have you played math attack before? (y/n): ")
if yes_no_var == 1:
  time.sleep(1)
  print(" ")
  input("tutorial line #1")
  input("tutorial line #2")
  input("tutorial line #3")
  print(" ")


#Difficulty Of Questions
difficulty_of_questions = num_check("How difficult would you like the questions to be? (1/2/3)", 1, 3)
time.sleep(1)
print(' ')
  
#Amt of questions
number_of_rounds = num_check("How many rounds would you like to play? (10 - 30): ", 10, 30)

#Feedback
statement_generator("You will play on difficulty level " + str(difficulty_of_questions), "-")
statement_generator("and you will play " + str(number_of_rounds) + " rounds", "-")
yes_no("are you ready to start?")
if yes_no_var == 0:
  print("hi")
  
#Questions & Answer Checking