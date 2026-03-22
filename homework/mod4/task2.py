def fast_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_pow(a * a, n // 2)
    else:
        return a * fast_pow(a, n - 1)

parts = input().split()
a = int(parts[0])
n = int(parts[1])
print(fast_pow(a, n))
