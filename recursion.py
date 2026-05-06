def fibonnaci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def compareTo(s1, s2):
    if s1 == "" and s2 == "":
        return 0

    if s1 == "":
        return -1

    if s2 == "":
        return 1

    if s1[0] < s2[0]:
        return -1

    if s1[0] > s2[0]:
        return 1

    return compareTo(s1[1:], s2[1:])


def main():
    print("Testing fibonnaci:")
    print("fibonnaci(1):", fibonnaci(1))
    print("fibonnaci(2):", fibonnaci(2))
    print("fibonnaci(6):", fibonnaci(6))
    print("fibonnaci(10):", fibonnaci(10))

    print("\nTesting gcd:")
    print("gcd(48, 18):", gcd(48, 18))
    print("gcd(100, 25):", gcd(100, 25))
    print("gcd(17, 13):", gcd(17, 13))

    print("\nTesting compareTo:")
    print("compareTo('apple', 'banana'):", compareTo("apple", "banana"))
    print("compareTo('apple', 'apple'):", compareTo("apple", "apple"))
    print("compareTo('banana', 'apple'):", compareTo("banana", "apple"))


if __name__ == "__main__":
    main()