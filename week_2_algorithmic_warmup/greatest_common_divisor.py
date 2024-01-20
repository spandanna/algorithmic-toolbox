def gcd(a,b):
    if b == 0:
        return a
    a_prime = a % b
    return gcd(b, a_prime)

if __name__ == "__main__":
    print(gcd(*map(int, input().split(' '))))