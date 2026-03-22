line = input()

words = []
current = ""
for ch in line:
    if ch == ' ':
        if current != "":
            words = words + [current]
            current = ""
    else:
        current = current + ch
if current != "":
    words = words + [current]

result = ""
for w in words:
    result = result + w[len(w) - 1]
print(result)
