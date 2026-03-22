s = input()
result = ""
for ch in s:
    if ch != '-' and ch != '(' and ch != ')' and ch != ' ':
        result = result + ch
print(result)
