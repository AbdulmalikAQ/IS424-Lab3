numbers = []

for _ in range(10):
    numbers.append(int(input("Enter number: ")))

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)