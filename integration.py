# Zach D'Alessandro
# Integration Project
# Statistics calculator for class
# https://www.geeksforgeeks.org/factorial-in-python/

import math

#Selection screen for each function
def intro_menu():


    print("Welcome!")
    print("Main Menu")
    print(" 1. Deck of cards probability calculator")
    print(" 2. Permutations calculator")
    print(" 3. Combination calculator")
    print(" 4. Statistics quiz")


#Calculator for probability in a standard deck of cards
def prob_cards(cards_tested):


    loop_zero = 1
    while loop_zero > 0:
        # number of cards being sampled
        cards = 52
        print("This calculator is used to find the probability that you choose"
              " a certain card within a standard deck of cards.")
        probability_cards = cards_tested / cards
        print(str(round(probability_cards, 2)) + " or")
        print(str(round(probability_cards * 100)) + "%")
        return


# calculating Permutations
def perm():


    loop_one = 1
    while loop_one >= 0:
        n_variable_one = int(input("Please enter the n variable that comes "
                                   "before the P for permutation. "))
        k_variable_one = int(input("Please enter the k variable that "
                                   "comes after the P for permutation. "))
        permutations = math.factorial(n_variable_one) / math.factorial(k_variable_one)
        print(permutations)


# calculating combinations
def combination():


    loop_two = 1
    while loop_two > 0:
        print("Note: n must be larger than k")
        n_variable_two = int(input("Please enter the n variable that comes "
                                   "before the C for Combination. "))
        k_variable_two = int(input("Please enter the k variable that comes "
                                   "after the C for Combination. "))
        permutations_combinations = math.factorial(n_variable_two) / math.factorial(n_variable_two - k_variable_two)
        combination = permutations_combinations / math.factorial(k_variable_two)
        print(combination)


# Stats quiz with score
def quiz():


#score is to add score based on correct answers or no points on incorrect
# answers
    score = 0
    print("I hope you've studied because you are about to be quizzed!")
    print("Note: Use graphing calculator for test practice.")
    print("what is the probability you draw a spade?")
    print("Answer choices:")
    print("a) 25%")
    print("b) 30%")
    print("c) 12%")
    print("d) 24%")
    answer_q1 = str(input("Enter your answer here: "))
    if answer_q1 == "a":
        print("Correct!")
        score = score + 1
        print("Score =", score)
    else:
        print("Sorry that was not the correct answer, it was actually 25%")
        print("Score =", score)

    print("What is the probability you draw an ace?")
    print("Answer choices:")
    print("a) 5%")
    print("b) 15%")
    print("c) 8%")
    print("d) 3%")
    answer_q1 = str(input("Enter your answer here: "))
    if answer_q1 == "c":
        print("Correct!")
        score += 1
        print("Score =", score)
    else:
        print("Sorry that was not the correct answer, it was actually 8%")
        print("Score =", score)

    print("Calculate the permutation if n = 12 and k = 7")
    print("Answer choices:")
    print("a) 11457")
    print("b) 54126")
    print("c) 10200")
    print("d) 95040")
    answer_q1 = str(input("Enter your answer here: "))
    if answer_q1 == "d":
        print("Correct!")
        score += 1
        print("Score =", score)
    else:
        print("Sorry that was not the correct answer, it was actually 95040")
        print("Score =", score)

    print("Calculate the permutation if n = 17 and k = 8")
    print("Answer choices:")
    print("a) 980179200")
    print("b) 780866899")
    print("c) 909877905")
    print("d) 679897649")
    answer_q1 = str(input("Enter your answer here: "))
    if answer_q1 == "a":
        print("Correct!")
        score += 1
        print("Score =", score)
    else:
        print("Sorry that was not the correct answer, it was actually"
              " 980179200")
        print("Score =", score)

    print("Calculate the combination if n = 12 and k = 9")
    print("Answer choices:")
    print("a) 400")
    print("b) 220")
    print("c) 334")
    print("d) 206")
    answer_q1 = str(input("Enter your answer here: "))
    if answer_q1 == "b":
        print("Correct!")
        score += 1
        print("Score =", score)
    else:
        print("Sorry that was not the correct answer, it was actually 220")
        print("Score =", score)

    print("What is the probability you draw a king")
    print("Answer choices:")
    print("a) 6%")
    print("b) 8.4%")
    print("c) 7.6%")
    print("d) 7.2%")
    answer_q1 = str(input("Enter your answer here: "))
    if answer_q1 == "b":
        print("Correct!")
        score += 1
        print("Score =", score)
    else:
        print("Sorry that was not the correct answer, it was actually 220")
        print("Score =", score)

#main function for all previously defined functions in order to execute them
def main():


    intro_menu()
    main_one = int(input(
        "Enter the number corresponding to the calculator you"
        " would like to use: "))

    if main_one == 1:
        cards_tested = int(input("Please enter total number of cards that fit "
                                 "within the given requirement. "))
        prob_cards(cards_tested)


    elif main_one == 2:
        perm()

    elif main_one == 3:
        combination()

    elif main_one == 4:
        quiz()


main()