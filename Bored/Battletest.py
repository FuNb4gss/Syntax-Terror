import random
import sys
import time
import datetime

# Going to practice adding some multipliers into combat damage



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