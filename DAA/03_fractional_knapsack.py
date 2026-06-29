class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(w, arr):
    for item in arr:
        if item.weight <= 0:
            raise ValueError(f"Item weight must be positive, got {item.weight}")
    arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
    finalValue = 0.0
    for item in arr:
        if w >= item.weight:
            finalValue += item.profit
            w -= item.weight
        else:
            finalValue += item.profit * (w/item.weight)
            break
    return finalValue

if __name__ == "__main__":
    try:
        n = int(input("Enter number of items-\n"))
        if n <= 0:
            print("Error: Number of items must be positive.")
            exit(1)
        arr = []
        for i in range(n):
            profit = int(input("Enter profit of item " + str(i + 1) + "-\n"))
            weight = int(input("Enter weight of item " + str(i + 1) + "-\n"))
            arr.append(Item(profit, weight))
        w = int(input("Enter capacity of knapsack-\n"))
        if w < 0:
            print("Error: Knapsack capacity cannot be negative.")
            exit(1)
        print("Maximum value in knapsack: ", fractionalKnapsack(w, arr))
    except ValueError as e:
        print(f"Error: Invalid input - {e}")