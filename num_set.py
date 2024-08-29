numbers_set = {num for num in range(1, 101)}
print("Set of numbers from 1 to 100:")
for i, num in enumerate(sorted(numbers_set), start=1):
    print(f"{num:3}", end=' ')
    if i % 10 == 0:
        print()
