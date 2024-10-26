import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    quick_picks_count = int(input("How many quick picks? "))

    for _ in range(quick_picks_count):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in sorted(quick_pick)))


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    return quick_pick


main()
