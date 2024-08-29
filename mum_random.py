import random
random_numbers = [random.randint(100, 500) for _ in range(50)]
unique_numbers = set(random_numbers)
unique_count = len(unique_numbers)
print("Random numbers (50 numbers):")
for i in range(0, len(random_numbers), 10):
    print(random_numbers[i:i+10])
print("\nUnique numbers (sorted):")
unique_numbers_sorted = sorted(unique_numbers)
for i in range(0, len(unique_numbers_sorted), 10):
    print(unique_numbers_sorted[i:i+10])

print("\nCount of unique numbers:", unique_count)
