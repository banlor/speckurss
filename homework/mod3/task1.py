vals = [int(x) for x in input().split()]
result = vals[0] + vals[1] + vals[2] - min(vals) - max(vals)
print(result)
