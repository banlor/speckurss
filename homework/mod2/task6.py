s = input()
ones = 0
zeros = 0
for ch in s:
    if ch == '1':
        ones = ones + 1
    elif ch == '0':
        zeros = zeros + 1

if ones == zeros:
    print("yes")
else:
    print("no")
