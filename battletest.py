import random
import sys
import datetime
import time





def two_handed_sword():
    attack = random.randint(15,30)
    return attack

def fireball():
    attack = random.randint(10,40)
    return attack


fire_magic = fireball()
phys_attack = two_handed_sword()

print(fire_magic)

def fireball_crit():
    return fire_magic * 0.10

print(fireball_crit())