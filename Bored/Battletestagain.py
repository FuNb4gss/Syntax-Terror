import random
import time

user_hp = 100
advocate_hp = 100

# damage rolls

def two_handed_sword():
    return random.randint(15,30)

def fireball():
    return random.randint(10,40)

def advocate_attack():
    return random.randint(5,20)

# Crit system

def roll_crit(damage, chance, multiplayer=1.5):
    if random.random() < chance:
        return int(damage * multiplayer), True
    return damage, False

# Player attack

def battlemage_attack():
    phys = two_handed_sword()
    fire = fireball()

    phys, phys_crit = roll_crit(phys, 0.15)
    fire, fire_crit = roll_crit(fire, 0.10)

    total = phys + fire

    print(f"You strike for {phys} physical damage", end="")
    if phys_crit:
        print(" (CRITICAL!)", end="")
    print()

    print(f"You unleash {fire} fire damage", end="")
    if fire_crit:
        print(" (CRITICAL!)", end="")
    print()

    print(f"➡ Total damage dealt: {total}\n")

    return total

def intro():
    story = [
        "Welcome, traveler, to the world of Valaria.",
        "Once, we lived in harmony. No war. No magic. Only peace.",
        "Then the Advocates descended from the heavens.",
        "They burned our towns. We were forced to fight back.",
        "From the earth, we learned magic — and with steel and flame, we endured."
    ]

    for line in story:
        print(line)
        time.sleep(2)

intro()

print("\nYou are the BattleMage of Astoria")
print("Two Advocates charge at you!\n")
time.sleep(2)

damage = battlemage_attack()
advocate_hp -= damage

print(f"Advocate has {advocate_hp} Hp remaining.")
