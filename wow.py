import random
import matplotlib.pyplot as plt

class Alien:
    al_count = 0
    def __init__(self, x, y, p=100):
        self.x = x
        self.y = y
        self.p = p
        Alien.al_count += 1
    def hit(self, d=1):
        self.p -= d
    def is_alive(self):
        return self.p > 0

def u(_x, _y):
    global xy
    px, py = random.uniform(0, 100), random.uniform(0, 100)
    flag = True
    while flag:
        if (px, py) not in xy:
            flag = False
            xy.add((px, py))
        else:
            px, py = random.uniform(0, 100), random.uniform(0, 100)
    return aliens.
aliens = []
x = []
y = []
xy = set()
for i in range(100):
    aliens.append(Alien(random.randint(0, 100), random.randint(0, 100), random.randint(1, 100)))
print(aliens)