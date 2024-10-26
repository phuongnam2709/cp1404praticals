import random

def main():
    score = get_valid_score()
    print_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")

        print_menu()
        choice = input(">>> ").upper()

    print("Farewell")

def print_menu():
    print("\n(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score, please enter a score between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score

def determine_result(score):
    if score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * int(score))

main()
