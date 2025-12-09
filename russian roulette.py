import random
ammo = [0 for i in range(6)]
ammo[random.randint(0, 5)] = 1
print(ammo)