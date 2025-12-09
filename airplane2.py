import random
yes = 0
nope = 0
for i in range(1000):
    airplane = {}
    apass = list(range(100))
    sits = list(range(100))
    fp = random.choice(apass)
    fs = random.choice(sits)
    airplane[fp] = fs
    apass.remove(fp)
    sits.remove(fs)
    np = len(apass)
    for i in range(np):
        rp = random.choice(apass)
        if rp in sits:
            rs = rp
            airplane[rp] = rs
        else:
            rs = random.choice(sits)
            airplane[rp] = rs
        apass.remove(rp)
        sits.remove(rs)
        if i == np-1:
            if airplane[rp] == rp:
                yes += 1
            else:
                nope += 1
print(yes/(yes+nope))

