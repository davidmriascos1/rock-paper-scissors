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
player_choice = int(input("Choose between: Rock(0), Paper (1), Scissors (2). \n"))
computer_choice = random.randint(0, 2)
#Conditional for Rock
if player_choice == 0 and computer_choice == 2:
    print(f"{rock}you won")
    print(f"{scissors} computer lost")
elif player_choice == 0  and computer_choice == 1 :
    print(f"{rock}you lost")
    print(f"{paper}computer won")
elif player_choice == 0  and computer_choice == 0 :
    print(f"{rock} draw")
    print(f"{rock} draw")
#conditional for paper
if player_choice == 1  and computer_choice == 0 :
    print(f"{paper}you won")
    print(f"{rock}computer lost")
elif player_choice == 1 and computer_choice == 2:
    print(f"{paper}you lost")
    print(f"{scissors}computer won")
elif player_choice == 1 and computer_choice == 1  :
    print(f"{paper} draw")
    print(f"{paper} draw")
#conditional for scissors
if player_choice == 2 and computer_choice == 1:
    print(f"{scissors}you won")
    print(f"{paper}computer lost")
elif player_choice == 2 and computer_choice == 0:
    print(f"{scissors}you lost")
    print(f"{rock}computer won")
elif player_choice == 2 and computer_choice == 2:
    print(f"{scissors} draw")
    print(f"{scissors} draw")
#else:
    #print("you didn't type between 0-2, you lose")
