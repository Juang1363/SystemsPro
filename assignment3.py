import time
def fibo_naive(n):
    if n < 2:
        return n
    return fibo_naive(n - 1) + fibo_naive(n - 2)
def fibo_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
    return memo[n]
start_time = time.time()
fibo_naive(40)
end_time = time.time()
elapsed_time_naive = end_time - start_time

start_time = time.time()
fibo_memo(40)
end_time = time.time()
elapsed_time_memo = end_time - start_time

print("Naive time: {} sec".format(elapsed_time_naive))
print("Memo time: {} sec".format(elapsed_time_memo))