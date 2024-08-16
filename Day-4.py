#Rock Paper Scissors Game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
x=[rock,paper,scissors]
user_input=int(input())
print(x[user_input])
random_input=random.randint(0,2)
print(random_input)
print(x[random_input])
if (user_input==0 and random_input==2):
    print("You wins!")
elif (user_input==2 and random_input==1):
    print("You wins!")
elif (user_input==1 and random_input==0):
    print("you wins!")
elif(user_input==random_input):
    print("Draw")
else:
    print("You loose")
