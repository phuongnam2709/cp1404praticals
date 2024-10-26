items = int(input("Number of items: "))
total_price = 0

for i in range(items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {items} items is ${total_price:.2f}")
