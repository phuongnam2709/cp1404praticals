# 1 .
TAX_RATE = 0.09
price = float(input("Enter the item's price: $"))

tax_applicable = input("Does the item have GST? (y/n): ").strip().lower()

if tax_applicable == 'y':
    total_price = price * TAX_RATE
else:
    total_price = price

print(f"Total price is: ${total_price:.2f}")

# 2 .
gifts_num = int(input("Enter the number of gifts: "))
students_num = int(input("Enter the number of students: "))

gifts_per_student = gifts_num // students_num
leftover_gifts = gifts_num % students_num

print(f"Each student gets {gifts_per_student} gifts, and there are {leftover_gifts} gifts left over.")
