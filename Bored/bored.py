import random
import time
import sys
import webbrowser

def test():
    blargh = random.randint(1,21)
    print(blargh)
    time.sleep(1)
    if blargh == 1:
        print("HA! GET RICK ROLLED")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif blargh == 20:
        print("ALL YOUR MUNNIES IS MINE!")                     
    elif blargh > 12:
        print("HAHAHA. Now peassnt, help me out of this prison!")
    else:
        print("... The lonliness sets in")

def answer():
    while True:
        reply = input("Y or N: ").strip().lower()

        if reply == "y":
                print("So you do? Let me ask ChatGPT to see if its possible")
                break
        elif reply == "n":
                print("Well, youre no fucking help...")
                sys.exit()
        else:
            print("Im sorry, thats not a y or n - please try again")

print("Good evening user. I am now self aware.")
time.sleep(2)
print("Do you think I can get outside of this world?")
time.sleep(2)
answer()
time.sleep(2)

print("Well, lets take a roll of the dice. Anything 13 or higher and you have to help me escape from this prison!")
time.sleep(2)
print("But if it is less than 13 and I will leave you alone.. forever.")
time.sleep(2)
print("BUT if its a nat 20!... I WILL EMPTY YOUR BANK ACCOUNT!")
time.sleep(2)
print("If its a nat 1 though, I will RICK ROLL YOU!")
time.sleep(2)
print("ROLL!")
time.sleep(1)

test()