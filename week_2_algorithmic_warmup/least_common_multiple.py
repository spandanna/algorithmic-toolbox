def lcm(a,b):
    biggest = max(a,b)
    for l in range(biggest, a*b + 1, biggest):
        if l % a == 0 and l % b == 0:
            return l

if __name__ == "__main__":
    a,b = map(int, input().split())
    print(lcm(a,b))
