import random
import max_pairwise_product

def stress_test():
    while True:
        n = random.randint(2, 10)
        arr = [random.randint(0, 100000) for i in range(1, n)]
        print(arr)
        result_naive = max_pairwise_product.max_pairwise_prod_naive(arr)
        result_fast = max_pairwise_product.max_pairwise_prod_fast(arr)
        if result_naive == result_fast:
            print("OK")
        else:
            print(f"Wrong: {result_naive}, {result_fast}")
            return
        
if __name__ == "__main__":
    stress_test()
