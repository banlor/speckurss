n = int(input())
names = []
for i in range(n):
    names.append(input())

uni = []
for name in names:
    already = False
    for u in uni:
        if len(u) == len(name):
            already = True
            break
    if not already:
        uni.append(name)

print(names)
print(uni)
