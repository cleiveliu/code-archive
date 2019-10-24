# find primes
def find_prime(n):
    res = []
    for i in range(2, n + 1):
        if res != [] and any(i % x == 0 for x in res):
            continue
        res.append(i)
    return res
