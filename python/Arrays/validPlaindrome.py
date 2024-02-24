s = "A man, a plan, a canal: Panama"
t = ""
for char in s:
    if char.isalnum():
        t += char
t = t.lower()
print(t == t[::-1])