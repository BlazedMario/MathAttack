#imports
import random
import time

#Variables
correct_answers = 0
wrong_answers = 0
#Variable - User experience
user_previous_experience = input("Have you played math attack before? (y/n): ")

#lists
difficulty_levels = ["1","2","3"]

#functions

#Tutorial
input("Line #1 Tutorial")
input("Line #2 Tutorial")


#Variables - Difficulty Of Questions
try:
  difficulty = int(input("What level of difficulty would you like to play? 1/2/3: "))
except ValueError:
  print("put in a real level ya dog")
#Amt of questions


#Questions & Answer Checking