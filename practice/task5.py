prices = list(map(int, input().split()))
k = int(input())
m = int(input())
discount = [p - (p // k) * m for p in prices]
print(prices)
print(discount)
