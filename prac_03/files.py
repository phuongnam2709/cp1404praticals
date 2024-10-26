# 1: Ask for the user's name and write it to name.txt
name = input("Enter your name: ")
with open('name.txt', 'w') as name_file:
    name_file.write(name)

# 2: Read the name from name.txt and print a greeting
with open('name.txt', 'r') as name_file:
    name_from_file = name_file.readline().strip()  # Read the name and remove any extra whitespace
    print(f"Hi {name_from_file}!")

# 3: Create a text file called numbers.txt with specific numbers
with open('numbers.txt', 'w') as numbers_file:
     numbers_file.write('17\n42\n400\n')

# Task 4: Read the first two numbers from numbers.txt and print their sum
with open('numbers.txt', 'r') as numbers_file:
    first_number = int(numbers_file.readline().strip())  # Read the first number
    second_number = int(numbers_file.readline().strip())  # Read the second number
    total = first_number + second_number
    print(f"The total of the first two numbers is: {total}")

# Task 5: Calculate the total for all numbers in numbers.txt
total_sum = 0
with open('numbers.txt', 'r') as numbers_file:
    for line in numbers_file:
        total_sum += int(line.strip())  # Add each number to the total
print(f"The total of all numbers is: {total_sum}")
