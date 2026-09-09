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
asci_list=[rock,paper,scissors]

choices=["rock", "paper", "scissors"]
usr_input = int(input("Rock(1), Paper(2), Scissors(3)?"))
if usr_input < 1 or usr_input > 3:
    print("invalid choice")
else:
    user_choice = choices[usr_input - 1]
    print(f"user choice {user_choice}")
    print(asci_list[usr_input-1])

    system_choice = random.choice(choices)
    print(f"system choice {system_choice}")
    print(asci_list[choices.index(system_choice)])

    if user_choice == system_choice:
        print("It's a tie")

    elif user_choice=="rock" and system_choice=="paper":
        print("System win")
    elif user_choice == "rock" and system_choice == "scissors":
        print("User  win")

    elif user_choice=="scissors" and system_choice=="rock":
        print("System win")
    elif user_choice=="scissors" and system_choice=="paper":
        print("User win")

    elif user_choice=="paper" and system_choice=="rock":
        print("User win")
    elif user_choice=="paper" and system_choice=="scissors":
        print("System win")




