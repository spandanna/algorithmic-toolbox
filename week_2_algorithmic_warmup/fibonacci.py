def find_fibonacci(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n-1):
        previous, current = current, previous + current
    return current


if __name__== "__main__":
    print(find_fibonacci(int(input())))