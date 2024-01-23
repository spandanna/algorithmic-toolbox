def change(money):
    tens = money // 10
    fives = money % 10 // 5
    ones = money % 10 % 5
    return tens + fives + ones

if __name__ == '__main__':
    m = int(input())
    print(change(m))
