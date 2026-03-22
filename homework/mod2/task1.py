line = input()
a = int(line[0:line.index(',')])
b_str = line[line.index(',') + 1:]
b = int(b_str)
print(a % b)
