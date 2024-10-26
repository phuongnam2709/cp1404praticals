numbers = [3, 1, 4, 1, 5, 9, 2]

# 1. numbers[0] - Expected value: 3
# 2. numbers[1] - Expected value: 1
# 3. numbers[2] - Expected value: 4
# 4. numbers[-1] - Expected value: 2
# 5. numbers[-2] - Expected value: 9
# 6. numbers[3:6] - Expected value: [1, 5, 9]
# 7. numbers[:3] - Expected value: [3, 1, 4]
# 8. numbers[3:] - Expected value: [1, 5, 9, 2]
# 9. numbers.count(1) - Expected value: 2
# 10. numbers.index(5) - Expected value: 4

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)