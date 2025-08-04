N = int(input("Enter Positive Integer: "))

numbers = []
for i in range(N):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

X = int(input("Enter the number to search for (X): "))
if X in numbers:
    print(f"{X} is present in the list.")
else:
    print("-1 🥹")