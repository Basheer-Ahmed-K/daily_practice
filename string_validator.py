s = input()
l = m = n = o = p = q = False
for c in s:
    if c.isalnum():
        l = True
    if c.isalpha():
        m = True
    if c.isdigit():
        n = True
    if c.islower():
        o = True
    if c.isupper():
        p = True
print(f"{l}\n{m}\n{n}\n{o}\n{p}")
