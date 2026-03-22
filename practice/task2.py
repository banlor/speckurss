n = int(input())
nums = list(range(n, n * n + 1))
roots = [x ** 0.5 for x in nums]
print(nums)
print(roots)
