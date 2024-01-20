def max_pairwise_prod_fast(arr):
    set_arr = sorted(arr, reverse=True)
    if len(set_arr) > 1:
        a, b = set_arr[:2]
    else:
        a , b  = 0, 0
    return a * b

def max_pairwise_prod_naive(arr):
    n = len(arr)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
            arr[first] * arr[second])
    return max_product
        
if __name__ == "__main__":
    x = int(input())
    arr = list(map(int, input().split(' ')))
    print(max_pairwise_prod_fast(arr))
