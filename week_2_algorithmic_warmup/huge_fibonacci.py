def find_pisano_period(m):
    """The pisano period is the length of the repeating sequence of fibonacci % m.
    """
    i = 2
    cur = 0
    while True:
        cur = find_fibonacci(i) % m
        if cur == 0 and find_fibonacci(i + 1) % m == 1:
            break
        i += 1
    return i
            
def find_fibonacci(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n-1):
        previous, current = current , previous + current
    return current


if __name__== "__main__":
    n, m = map(int, input().split())
    p = find_pisano_period(m)
    n = n%p # find new smaller n given the repeating sequence of the modulo
    print(find_fibonacci(n) % m) # return modulo of fibonacci number