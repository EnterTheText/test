import random

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
aliens = []
for i in range(100):
    aliens.append(Alien(random.randint(0, 100), random.randint(0, 100), random.randint(1, 100)))
print(aliens)