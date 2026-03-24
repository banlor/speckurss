import re

text = input()

year = r"20\d{2}"
month = r"(?:0[1-9]|1[0-2])"
day = r"(?:0[1-9]|[12]\d|3[01])"
hours = r"(?:[01]\d|2[0-3])"
minutes = r"[0-5]\d"
seconds = r"[0-5]\d"

pattern = year + "-" + month + "-" + day + r"\s" + hours + ":" + minutes + ":" + seconds
dates = re.findall(pattern, text)
for d in dates:
    print(d)
