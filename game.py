import random
import sys
import math


def check_score_from_file(name):
    with open("rating.txt", "r") as score_file:
        current_score = 0
        for line in score_file:
            if name in line:
                temp = line.split(sep=" ")
                current_score = int(temp[1])
    return current_score


def define_rules(all_arr, user_cho):
    arr_after = []
    arr_before = []
    flag = 0
    for item in all_arr:
        if item == user_cho:
            flag = 1
        elif flag == 0:
            arr_before.append(item)
        else:
            arr_after.append(item)
    return arr_after + arr_before


user_name = input("Enter your name: ")
print("Hello,", user_name)
score = check_score_from_file(user_name)
all_possibilities = input()
if not all_possibilities:
    all_possibilities = ['rock', 'paper', 'scissors']
else:
    all_possibilities = list(all_possibilities.split(sep=','))
print("Okay, let's start")
while 1:
    user_choice = input()
    computer_choice = random.choice(all_possibilities)

    temp_possibilities = define_rules(all_possibilities, user_choice)
    lose_possibilities = []
    for i in range(math.ceil(len(temp_possibilities) / 2)):
        lose_possibilities.append(temp_possibilities.pop())
    win_possibilities = temp_possibilities
    if user_choice in all_possibilities:
        if computer_choice == user_choice:
            print(f"There is a draw ({computer_choice})")
            score += 50
        elif computer_choice in lose_possibilities:
            print(f"Well done. The computer chose {computer_choice} and failed")
            score += 100
        elif computer_choice in win_possibilities:
            print("Sorry, but the computer chose", computer_choice)
    elif user_choice == '!rating':
        print("Your rating:", score)
    elif user_choice == '!exit':
        print("Bye!")
        sys.exit()
    else:
        print("Invalid input")































