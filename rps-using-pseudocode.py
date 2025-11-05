import random

name = input("Enter your Name: ")

ai_name = "Computer"
ai_choices = ["paper", "paper", "paper"]

user_points = 0
computer_points = 0
round = 0
# max_round = 0
user_hand = None
computer_hand = None
winner = None

for x in range(3):
    print(f"Round {x+1}, fight!")
    round = x
    user_hand = None
    computer_hand = None

    user_ini = input("Type your hand: ")
    user_hand = user_ini.lower()
    computer_ini = random.choice(ai_choices)
    computer_hand = computer_ini.lower()

    if user_hand == "rock" and computer_hand == "scissors":
        user_points += 1
        print(
            f"{name.capitalize()} Won the Round! The score is now {name}  : {user_points} | {ai_name} : {computer_points}")
    elif user_hand == "paper" and computer_hand == "rock":
        user_points += 1
        print(
            f"{name.capitalize()} Won the Round! The score is now {name}  : {user_points} | {ai_name} : {computer_points}")
    elif user_hand == "scissors" and computer_hand == "paper":
        user_points += 1
        print(
            f"{name.capitalize()} Won the Round! The score is now {name}  : {user_points} | {ai_name} : {computer_points}")
    elif computer_hand == "rock" and user_hand == "scissors":
        computer_points += 1
        print(
            f"{ai_name.capitalize()} Won the Round! The score is now {name}  : {user_points} | {ai_name} : {computer_points}")
    elif computer_hand == "paper" and user_hand == "rock":
        computer_points += 1
        print(
            f"{ai_name.capitalize()} Won the Round! The score is now {name}  : {user_points} | {ai_name} : {computer_points}")
    elif computer_hand == "scissors" and user_hand == "paper":
        computer_points += 1
        print(
            f"{ai_name.capitalize()} Won the Round! The score is now {name}  : {user_points} | {ai_name} : {computer_points}")
    else:
        print(
            f"This round's a Tie! Both of you chose {user_hand.capitalize()}")
    print(
        f"You chose {user_hand.capitalize()}, Computer chose {computer_hand.capitalize()}")

    if round == 2:
        if user_points > computer_points:
            winner = name
            print(
                f"{name} Won the game! The Final Score is {user_points}:{computer_points}")
        elif computer_points > user_points:
            winner = ai_name
            print(
                f"{ai_name} Won the game! The Final Score is {user_points}:{computer_points}")
        else:
            winner = None
            print(
                f"It's a Tie! The Final Score is {user_points}:{computer_points}")

        play_again_ini = input(
            "Game Over! Do you want to play again? (Type Y/N): ")
        play_again = play_again_ini.lower()

        if play_again == "y":

        break
