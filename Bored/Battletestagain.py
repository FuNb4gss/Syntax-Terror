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

def fireball_crit():
    crit = fire_magic * 0.10
    finish = crit + fire_magic
    return finish

def two_handed_crit():
    crit = phys_attack * 0.15
    finish = crit + phys_attack
    return finish

def advocate_health():
    health = 100
    return health

def player_health():
    health = 100
    return health

def advocate_magic_sword():
    attack = random.randint(5,20)
    return attack

def damage():
    




advocate_attack = advocate_magic_sword()
advocate_hp = advocate_health()
user = player_health()

print(f"{fire_magic}")
print(fireball_crit())

print(f"{phys_attack}")
print(two_handed_crit())

print("Welcome user, To the world of Valaria")
time.sleep(2)
print("In Valaria, we used to live in Harmony. There was no War. There was no magic. There was only peace")
time.sleep(2)
print("But then they...the Advocate's arrived from the heavens. They pillaged and burned our towns. We had no choice to fight back.")
time.sleep(2)
print("With that constant fighting we developed magic from the Earth. It was like she was helping us fight back.")
time.sleep(2)
print("Armed with our two-handed weaponry and our newly aquired knowledge of magic, We fought. We fought and drove back the Advocates. They still outnumber us 3 to 1 but, we continue to dwindle their numbers.")
time.sleep(2)

print("You user, are the Battlemage of Astoria. You see 2 Advocate's charge at you ready to battle. Get yourself ready!")
time.sleep(2)



