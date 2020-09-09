# My solution for the sailor / coconut problem
# https://www.youtube.com/watch?v=U9qU20VmvaU

def rec(n, i=0):
    if n % 5 != 1:
        return False
    while i < 5:
        a = (n - 1) / 5
        n -= a
        i += 1
        rec(n, i)
    return n


for k in range(1000000):
    if k % 5 == 1:
        result = rec(k)
        if result % 5 == 0:
            print(k - 5)
