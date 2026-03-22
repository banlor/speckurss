numbers = list(map(int, input().split()))
k = int(input())
result = [x for x in numbers if x % k == 0]
print(result)
