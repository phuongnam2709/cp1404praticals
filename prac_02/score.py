import random

def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))

    result = determine_result(score)
    print(f"Result: {result}")

    # Generate a random score and print its result
    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score: {random_score} - Result: {random_result}")

def determine_result(score):
    if score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
