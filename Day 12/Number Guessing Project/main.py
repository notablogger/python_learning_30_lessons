import art
import random


print(art.logo)

number_to_guess = random.randint(1,100)
turns_map={"e":10,"h":5}
turns=turns_map[input("you want easy or hard?(e/h)\n")]
print(f"You have {turns} turns left\n")


def is_the_number(guess):
    if guess>number_to_guess:
        print("Too high\n")
    elif guess<number_to_guess:
        print("Too low\n")
    elif guess==number_to_guess:
        print("You guessed the number, you win\n")
        return True
    return False

while turns > 0 and not is_the_number(int(input("enter your guess?\n"))):
      turns -= 1
      print(f"You have {turns} turns left\n")

if turns==0:
    print(f"Number of chances finish, you loose, the number was {number_to_guess}\n")