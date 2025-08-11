class NumberStore:
    def __init__(self):
        self._data = []

    def insert(self, value):
        self._data.append(value)

    def search_first_index(self, target):
        for i, v in enumerate(self._data, start=1):
            if v == target:
                return i
        print("-1 🥹")

        from module5_mod import NumberStore

store = NumberStore()

while True:
    N_input = input("Enter Numbers. Positive Integer: ")
    if N_input.isdigit() and int(N_input) > 0:
        N = int(N_input)
        break
    else:
        print("🤬 Please enter a valid positive integer NOW!")

for i in range(1, N + 1):
    while True:
        num_input = input(f"Enter number #{i}: ")
        try:
            number = int(num_input)
            store.insert(number)
            break
        except ValueError:
            print("🤬 enter integer!")

while True:
    X_input = input("Enter the number to search: ")
    try:
        X = int(X_input)
        break
    except ValueError:
        print("🤬 enter integer!")

result = store.search_first_index(X)
print(result)