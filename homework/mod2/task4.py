s = input()

is_nat = True
if len(s) == 0:
    is_nat = False
else:
    for ch in s:
        if ch < '0' or ch > '9':
            is_nat = False
            break
    if is_nat and int(s) <= 0:
        is_nat = False

if not is_nat:
    print("Неверный ввод")
else:
    n = int(s)

    def to_base(num, base):
        if num == 0:
            return "0"
        digits = "0123456789ABCDEF"
        result = ""
        while num > 0:
            result = digits[num % base] + result
            num = num // base
        return result

    bin_s = to_base(n, 2)
    oct_s = to_base(n, 8)
    hex_s = to_base(n, 16)
    print(bin_s + ", " + oct_s + ", " + hex_s)
