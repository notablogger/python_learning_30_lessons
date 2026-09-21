import random
import art

cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def choose_a_card():
    return random.choice(cards_list)

def calculate_score(cards):
    sum=0
    for card in cards:
        sum+=card
    return sum

def print_cards_and_score(who, cards, final):
    print(f"{who}{final} cards {cards} current score: {calculate_score(cards)}")

def check_for_ace(user_cards):
    if 11 in user_cards:
        user_cards[user_cards.index(11)]=1
    return user_cards

def is_blackjack(cards):
    if calculate_score(cards)==21:
        return True
    else:
        cards=check_for_ace(cards)
        if calculate_score(cards) == 21:
            return True
    return False


def play_black_jack():
    user_cards = []
    computer_cards = []

    user_cards.append(choose_a_card())
    computer_cards.append(choose_a_card())
    user_cards.append(choose_a_card())
    computer_cards.append(choose_a_card())

    print_cards_and_score("user", user_cards, "")
    print(f"Computer's first card is {computer_cards[0]}")

    if is_blackjack(user_cards):
        print_cards_and_score("user", user_cards, " final")
        print_cards_and_score("computer", computer_cards, " final")
        print("user wins")
        return
    elif is_blackjack(computer_cards):
        print_cards_and_score("computer", computer_cards, " final")
        print_cards_and_score("user", user_cards, " final")
        print("computer wins")
        return

    user_choice="y"

    while user_choice=="y":
        user_choice=input("Type 'y' to get another card, type 'n' to pass: \n")

        if user_choice=="y":
            user_cards.append(choose_a_card())
            print_cards_and_score("user", user_cards, "")
            print(f"Computer's first card is {computer_cards[0]}")
        if calculate_score(user_cards)>21:
            user_cards= check_for_ace(user_cards)
            if calculate_score(user_cards) > 21:
                user_choice="n"
            else:
                print_cards_and_score("user", computer_cards, " replaced")

    print_cards_and_score("user", user_cards, " final")

    while calculate_score(computer_cards)<17:
        computer_cards.append(choose_a_card())

    print_cards_and_score("Computer", computer_cards, " final")

    user_final_score=calculate_score(user_cards)
    computer_final_score=calculate_score(computer_cards)
    if user_final_score==computer_final_score:
        print("Draw")
    elif user_final_score>21:
        print("you lose")
    elif computer_final_score>21:
        print("you Win")
    elif user_final_score>computer_final_score:
        print("you win")
    else:
        print("you lose")

user_want_to_play="y"
while user_want_to_play=="y":
    print("\n"*30)
    print(art.logo)
    play_black_jack()
    user_want_to_play=input("Type 'y' to play blackjack or type 'n' to stop: ")