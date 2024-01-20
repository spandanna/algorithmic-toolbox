def find_fibonacci(n, m):
    # TODO implement pisano period > magic ingredient
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n-1):
        new_current = previous + current
        previous, current = current % m if current >= m else current, new_current % m if new_current >= m else new_current
    return current


if __name__== "__main__":
    print(find_fibonacci(*map(int, input().split())))