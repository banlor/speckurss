line = input()

first_space = -1
for i in range(len(line)):
    if line[i] == ' ':
        first_space = i
        break

second_space = -1
for i in range(first_space + 1, len(line)):
    if line[i] == ' ':
        second_space = i
        break

a = int(line[0:first_space])
b = int(line[first_space + 1:second_space])
c = int(line[second_space + 1:])

if a >= b and a >= c:
    if b >= c:
        print(b)
    else:
        print(c)
elif b >= a and b >= c:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if a >= b:
        print(a)
    else:
        print(b)
