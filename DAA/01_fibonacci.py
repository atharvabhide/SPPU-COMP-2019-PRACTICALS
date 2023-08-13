def fibRecursive(n):
    if n == 0 or n == 1:
        return 1
    return fibRecursive(n - 1) + fibRecursive(n - 2)

def fibIterative(n):
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c

if __name__ == "__main__":
    n = int(input("Enter a number-\n"))
    print("n'th fibonacci number by Recursive method: ", fibRecursive(n))
    print("n'th fibonacci number by Iterative method: ", fibIterative(n))