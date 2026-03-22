a = int(input())
p = a * 4
s = a * a
d = (2 * s) ** 0.5

p_str = str(int(p)) + ".00"
s_str = str(int(s)) + ".00"

d_rounded = int(d * 100 + 0.5) / 100
d_int = int(d_rounded)
d_frac = int(round((d_rounded - d_int) * 100))
if d_frac < 10:
    d_str = str(d_int) + ".0" + str(d_frac)
else:
    d_str = str(d_int) + "." + str(d_frac)

print(p_str + ", " + s_str + ", " + d_str)
