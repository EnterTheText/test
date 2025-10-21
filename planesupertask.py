import random
p = {}
s = {}
for i in range(10):
    p[i] = i
    s[i] = -1
s[random.randint(0, 9)] = 0
for i in range(1, 10):
    if s[p[i]] == -1:
        s[i] = i
    else:
        n = random.randint(1, 9)
        while s[n] != -1:
            n = random.randint(1, 9)
        s[n] = i
print(s)