import matplotlib.pyplot as plt

def func(p):
    m = 0
    while p != 1:
        if p % 2 == 0: p /= 2
        else: p = p * 3 + 1
        m += 1
    return m


k = int(input())
c = 0
x = []
y = []
for n in range(3, k+1):
    for i in range(2, n+1):
        if n % i == 0: c += 1
    if c == 1:
        x.append(n)
        y.append(func(n))
    c = 0
print("x:", *x)
print("y:", *y)

plt.plot(x, y, marker="o")

x = []
y = []
for l in range(1, k+1):
    x.append(l)
    y.append(func(l))

print("\nx:", *x)
print("y:", *y)
plt.plot(x, y, color="red", marker='.')
plt.show()