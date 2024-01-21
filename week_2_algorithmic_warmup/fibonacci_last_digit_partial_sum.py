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

def find_fibonacci_partial_sum(n, m):
    if n <= 1:
        return n
    previous, current = 0, 1
    if m <=1:
        s = 1
    else:
        s = 0
    for i in range(2, n+1):
        previous, current = current , previous + current
        if i >= m:
            s += current

    return s
if __name__== "__main__":
    m, n = map(int, input().split())

    p = find_pisano_period(10)
    diff = n-m
    n = n%p # find new smaller n given the repeating sequence of the modulo
    m = m%p # same for m
    if n < m: # need to make sure modulo n is bigger than modulo m so add on a period if it's not
        n += p
    print(find_fibonacci_partial_sum(n, m) % 10) # return modulo of fibonacci sum