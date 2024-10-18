#1. while loop
n = int(input("Enter a number: "))

i = 1

while i <= n:
    print(i)
    i += 1

#2. for loop
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)

#3.
SECRET_NUMBER = 7
number = int(input("Enter a number: "))

while number != SECRET_NUMBER:
    print("Guess again!")
    number = int(input("Enter a number: "))

#4.
username = input("Enter username: ")

while not username:
    username = input("Enter username: ")

salary = float(input("Enter your salary: $"))

while salary < 0:
    print("Salary must be greater than 0$")
    salary = float(input("Enter your salary: $"))

print(f"{username.upper()}'s salary is: ${salary:.2f}")

#5.
total = 0
counter = 0
age = int(input("Enter your age: "))

while age > -1:
    total += age
    counter += 1







