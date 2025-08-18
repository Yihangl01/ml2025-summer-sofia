n = int(input("How many training points? "))
k = int(input("K value? "))

x_values = []
y_values = []

print(f"\nOkay, give me {n} points:")
for i in range(n):
    print(f"Point {i+1}:")
    x = float(input("  x: "))
    y = float(input("  y: "))
    x_values.append(x)
    y_values.append(y)

test_x = float(input("\nWhat x value do you want to predict y for? "))

if k > n:
    print(f"Oh! k={k} is bigger than your {n} training points!")
else:
    distances_and_ys = []
    for i in range(n):
        distance = abs(x_values[i] - test_x)
        distances_and_ys.append([distance, y_values[i]])
    
    distances_and_ys.sort()
     
    total = 0
    for i in range(k):
        total = total + distances_and_ys[i][1]
    
    prediction = total / k
    
    print(f"\nPrediction: y = {prediction}")

print(f"\nYour training data was:")
for i in range(n):
    print(f"  ({x_values[i]}, {y_values[i]})")
