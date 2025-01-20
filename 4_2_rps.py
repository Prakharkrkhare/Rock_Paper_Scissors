import random

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

user=int(input("enter yur choice rock paper scissor (0,1,2) respectively : "))
if user<0 or user>2:
    print("enter as valid choice")
else:
    value="Nothing"
    choose=["rock","paper","scissors"]
    art=[rock,paper,scissors]
    computer=random.choice(choose)
    if user==0:
        value="rock"
    elif user==1:
        value="paper"
    elif user==2:
        value="scissors"
    print(f"you chose {choose[user]}\n {art[user]}")
    print(f"computer chooses {computer}\n {art[choose.index(computer)]}")
    if value==computer:
        print("game tied, no-one wins")
    elif (value=="rock" and computer=="scissors") or (value=="paper" and computer=="rock") or (value=="scissors" and computer=="paper"):
        print("you win !")
    else:
        print("computer wins !")
