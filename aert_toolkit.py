# Name - Arpit Patni
# Roll No - 2501730111
# AERT - Data Structures Unit 1

# Stack

class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) == 0:
            return "Stack empty"
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return "Stack empty"
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


# Factorial

def fact(n):
    if n < 0:
        return "Not defined for negative"
    if n == 0:
        return 1
    return n * fact(n - 1)


# Fibonacci

count1 = 0
count2 = 0

def fib1(n):
    global count1
    count1 += 1

    if n <= 1:
        return n
    return fib1(n - 1) + fib1(n - 2)


def fib2(n, d):
    global count2
    count2 += 1

    if n in d:
        return d[n]

    if n <= 1:
        d[n] = n
    else:
        d[n] = fib2(n - 1, d) + fib2(n - 2, d)

    return d[n]


# Tower of Hanoi

def hanoi(n, s, a, d, st):
    if n == 1:
        st.push(f"Move disk 1 from {s} to {d}")
        return

    hanoi(n - 1, s, d, a, st)
    st.push(f"Move disk {n} from {s} to {d}")
    hanoi(n - 1, a, s, d, st)


# Binary Search

def bsearch(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return bsearch(arr, key, low, mid - 1)
    else:
        return bsearch(arr, key, mid + 1, high)


# Main

def main():

    print("FACTORIAL TESTS")
    print("fact(0) =", fact(0))
    print("fact(1) =", fact(1))
    print("fact(5) =", fact(5))
    print("fact(10) =", fact(10))

    print("\nFIBONACCI TESTS")

    for n in [5, 10, 20, 30]:
        global count1, count2
        count1 = 0
        count2 = 0

        print("\nFor n =", n)

        r1 = fib1(n)
        print("Naive =", r1)
        print("Naive calls =", count1)

        r2 = fib2(n, {})
        print("Memo =", r2)
        print("Memo calls =", count2)

    print("\nTOWER OF HANOI (n=3)")

    st = Stack()
    hanoi(3, "A", "B", "C", st)

    for move in st.data:
        print(move)

    print("\nBINARY SEARCH TESTS")

    arr = [1, 3, 5, 7, 9, 11, 13]

    print("Search 7:", bsearch(arr, 7, 0, len(arr) - 1))
    print("Search 1:", bsearch(arr, 1, 0, len(arr) - 1))
    print("Search 13:", bsearch(arr, 13, 0, len(arr) - 1))
    print("Search 2:", bsearch(arr, 2, 0, len(arr) - 1))

    empty = []
    print("Search in empty list:", bsearch(empty, 5, 0, -1))


if __name__ == "__main__":
    main()
