# Program: Find Largest, Smallest and Average of 5 Numbers

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = numbers[0]
smallest = numbers[0]
total = 0

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total += num

average = total / len(numbers)

print("\nResults:")
print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)
