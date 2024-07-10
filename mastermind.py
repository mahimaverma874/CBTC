import os
import time
import random

def hints(number, secret_number, length):

    hint_choice = random.choice(
        ['length', "bigg or small", "close or far"])
    diff = secret_number - number
    if hint_choice == 'bigg or small':
        if diff < 0:
            print("Secret Number is smaller than this.")

        else:
            print("Secret Number is bigger than this.")

    elif hint_choice == 'close or far':
        if diff > 10:
            print("You are really far to the left from the number.")

        elif -10 < diff < 10:
            print("You are really close to the number.")

        else:
            print("You are really far to the right from the number.")

    elif hint_choice == 'length':
        print(f"It is a {length-1} to {length+1} digits number.")

    return


def guess_number(secret_number, length, player, flag):
    attempts = 0
    print(f"{player} will guess the number now!")

    while flag:
        try:
            number = int(input("Enter a number: "))
            if number == secret_number:
                print(f"{player} guessed the number correctly.")
                print(f"Their number of attempts is:{attempts+1}\n")
                break

            else:
                attempts += 1
                if attempts < 10:
                    hint = hints(number, secret_number, length)
                    print(f"{10-attempts} hints left.\n")
                else:
                    print('No hints left now!!')
                if (type(flag) == int):
                    flag -= 1

        except Exception as e:
            print(e)
    return attempts


def set_word(player):
    while True:
        number = input(f"{player} has to enter a multidigit number: ")
        if number.isdigit():
            break

        else:
            print("Please enter valid number,")
    return int(number), len(number)


def play(player1, player2):
    secret_number, length = set_word(player1)
    os.system('cls')

    player2_attempts = guess_number(
        secret_number, length, player2, True)

    if player2_attempts == 0:
        print("They guess the number in first attempt so they win!!")
        print("Redirecting you to the home screen in 15 seconds.")
        time.sleep(15)
        return

    secret_number, length = set_word(player2)
    os.system('cls')

    player1_attempts = guess_number(
        secret_number, length, player1, player2_attempts)

    if player1_attempts == player2_attempts:
        print(
            f"{player1} couldn't guess the number in lesser attempts so, {player2} is the winner!!")
        print("Redirecting you to the home screen in 15 seconds.")
        time.sleep(15)
        return

    else:
        print(f"{player1} win!!")
        print("Redirecting you to the home screen in 15 seconds.")
        time.sleep(15)


if __name__ == "__main__":
    while True:
        os.system("cls")
        print("Welcome to the mastermind game!!")

        player1 = input("Enter Player 1 name:")
        player2 = input("Enter Player 2 name:")

        play(player1, player2)
