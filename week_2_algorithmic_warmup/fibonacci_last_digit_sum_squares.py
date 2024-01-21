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

def find_fibonacci_sum_squares(n):
    """
    sum of squares == fibonacci(n) * fibonacci(n+1)
    """
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current , previous + current
    
    return previous * current
if __name__== "__main__":
    n = int(input())
    p = find_pisano_period(10)
    n = n%p # find new smaller n given the repeating sequence of the modulo
    print(find_fibonacci_sum_squares(n) % 10) # return modulo of fibonacci sum