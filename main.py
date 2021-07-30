#imports
import random
import time


#Variables
correct_answers = 0
wrong_answers = 0

#functions
def statement_generator(statement, decoration):
  sides = decoration * 3
  statement = "{} {} {}".format(sides, statement,sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return " "

#Variable - User experience
statement_generator("welcome to mathAttack", "#")
print()
print(" ")

time.sleep(1)
user_previous_experience = input("Have you played math attack before? (y/n): ")

#lists
difficulty_levels = ["1","2","3"]




#Tutorial
input("Line #1 Tutorial")
input("Line #2 Tutorial")


#Variables - Difficulty Of Questions
while True:
  try:
    difficulty_levels = int(input("What level of difficulty would you like to play? 1/2/3: "))
  except ValueError:
    print("put in a real level ya dog")
  
  



#Amt of questions
  

#Questions & Answer Checking