s = "   .the     sky is   blue.  "
t = ""
i = len(s)-1
while i >= 0:
    st,e = -1,-1
    while s[i] == " " and i >= 0:
        i -= 1
    else:
        e = i
    while s[i] != " " and i >= 0:
        i -= 1
    else:
        st = i
    if st != -1 and e != 1:
        t += s[st:e+1]
print(t)




