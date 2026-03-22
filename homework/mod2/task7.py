line = input()
comma_pos = -1
for i in range(len(line)):
    if line[i] == ',':
        comma_pos = i
        break

s = line[0:comma_pos]
symbol = line[comma_pos + 1:]

count = 0
for ch in s:
    if ch == symbol:
        count = count + 1
    else:
        break
print(count)
