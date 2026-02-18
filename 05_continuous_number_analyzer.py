# Program: Continuous Number Analyzer

numbers = []

while True:
    value = input("Enter number or type 'stop' to finish: ")

    if value.lower() == "stop":
        break

    try:
        numbers.append(int(value))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if numbers:
    total = sum(numbers)
    count = len(numbers)

    print("\nStatistics:")
    print("Count:", count)
    print("Sum:", total)
    print("Max:", max(numbers))
    print("Min:", min(numbers))
    print("Average:", total / count)
else:
    print("No numbers entered.")
