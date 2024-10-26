sales = float(input("Enter sales: $"))

if sales < 1000:
    bonus = sales * 0.10
else:
    bonus = sales * 0.15

print(f"User's bonus: {bonus:.2f} $")