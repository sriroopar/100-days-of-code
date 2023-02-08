import random

user_choice = int(input("What do you want to choose? Type 0 for Rock , 1 for Paper, 2 for Scissors?"))

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



if user_choice == 0 :
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

system_choice = random.randint(0,2)

if system_choice== 0 :
    print(rock)
elif system_choice == 1:
    print(paper)
else:
    print(scissors)

if user_choice == 0 and system_choice ==2:
    print("You Win")
elif user_choice ==2 and system_choice == 1:
    print("You Win")
elif user_choice == 1 and system_choice ==0:
    print("You Win")
else:
    print("You Lose")

