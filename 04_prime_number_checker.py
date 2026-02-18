# Program: Check Prime Number and Print Factors

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    if len(factors) == 2:
        print("Prime")
    else:
        print("Not Prime")
        print("Factors:", factors)
