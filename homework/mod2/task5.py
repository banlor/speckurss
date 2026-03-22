s = input()

domains = []
current = ""
for ch in s:
    if ch == '.':
        domains = domains + [current]
        current = ""
    else:
        current = current + ch
domains = domains + [current]

i = len(domains) - 1
while i >= 0:
    print(domains[i])
    i = i - 1
