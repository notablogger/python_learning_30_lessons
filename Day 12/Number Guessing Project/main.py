import art
import random


print(art.logo)

NUMBER_TO_GUESS = random.randint(1, 100)
TURNS_MAP={"e":10, "h":5}
TURNS=TURNS_MAP[input("you want easy or hard?(e/h)\n")]
print(f"You have {TURNS} turns left\n")


def is_the_number(guess):
    if guess>NUMBER_TO_GUESS:
        print("Too high\n")
    elif guess<NUMBER_TO_GUESS:
        print("Too low\n")
    elif guess==NUMBER_TO_GUESS:
        print("You guessed the number, you win\n")
        return True
    return False

while not is_the_number(int(input("enter your guess?\n"))):
      TURNS -= 1
      print(f"You have {TURNS} turns left\n")
      if TURNS==0:
        print(f"Number of chances finish, you loose, the number was {NUMBER_TO_GUESS}\n")
        break