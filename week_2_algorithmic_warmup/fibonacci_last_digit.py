def find_fibonacci_last_digit(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n-1):
        previous, current = current % 10, (previous + current) % 10
    return current


if __name__== "__main__":
    print(find_fibonacci_last_digit(int(input())))