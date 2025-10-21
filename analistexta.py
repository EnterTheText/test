f = open('alice.txt', encoding="utf8")
text = f.read()
s = {}
c = 0
for ch in text:
    if ch.lower() in s:
        s[ch.lower()] += 1
    else:
        s[ch.lower()] = 1
    c += 1
s = dict(sorted(s.items(), key=lambda x: x[1], reverse=True))
print(s)
for i in s:
    if ord(i) > 1072 and ord(i) < 1104: print(i, round(s[i]/c, 9)*100)