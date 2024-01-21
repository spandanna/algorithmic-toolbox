def find_survivor(n, k):
    rebels = list(range(n))
    kill = k-1
    remaining = n
    for _ in range(n -1):
        rebels.pop(kill)
        kill += k - 1
        remaining -= 1
        if kill >=remaining:
            kill = kill % remaining
    return rebels[0]

if __name__== "__main__":
    print(find_survivor(*map(int, input().split())))