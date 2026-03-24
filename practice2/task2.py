import re

text = input()

local_part = r"[a-zA-Z0-9+_\-#.]+"
domain_part = r"[a-zA-Z0-9.\-]+"
pattern = local_part + "@" + domain_part

emails = re.findall(pattern, text)
for e in emails:
    print(e)
