import art
import random
import game_data

a = random.choice(game_data.data)
b = random.choice(game_data.data)

print(art.logo)
score = 0


def print_message(item):
    print(f"{item["name"]}, a {item["description"]}, from {item["country"]}\n")


game_over = False


def print_followers_number(item1,item2):
    print(
        f"Number of followers {item1["name"]} and {item2["name"]} has are {item1["follower_count"]} and"
        f" {item2["follower_count"]}.\n")


while not game_over:
    if score > 0:
        a = b
        b = random.choice(game_data.data)
    print_message(a)
    print(art.vs)
    print_message(b)
    user_choice = input("Who has more followers? \n")
    print_followers_number(a, b)
    if "a" == user_choice:
        if a["follower_count"] > b["follower_count"]:
            score += 1
            print(f"You won\n total score now is {score}")
        else:
            game_over = True
            print(f"You lost, total score is {score}")
            break
    elif "b" == user_choice:
        if b["follower_count"] > a["follower_count"]:
            score += 1

            print(f"You won, total score now is {score}")
        else:
            game_over = True
            print(f"You lost, total score is {score}")
            break
    print("\n"*2)
