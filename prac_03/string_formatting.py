name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

print(f"My {name} was first made in {year} (that's right, {year}!)")

print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")

numbers = [1, 19, 123, 456, -25]

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# TODO 1: Use f-string formatting to produce the output:
print(f"{year} {name} for about ${cost:,.0f}!")

# TODO 2: Using a for loop with the range function and f-string formatting,
for i in range(11):
    print(f"2 ^ {i:<2} is {2 ** i:>4}")
