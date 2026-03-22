def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

parts = input().split()
a = int(parts[0])
b = int(parts[1])
print(gcd(a, b))
