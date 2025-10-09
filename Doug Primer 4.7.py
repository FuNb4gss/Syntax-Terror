#Part 1
#2
try:
    raise BaseException("Base exception raised")
except BaseException as e:
    print(e)
#3
try:
    raise Exception("Was my BaseException not good enough for you?")
except Exception as e:
    print(e)
#4
import sys

try:
    sys.exit("DONT YOU RUN FROM THE LORD!")
except SystemExit as travel:
    print(travel)
#5
try:
    while True:
        pass
except KeyboardInterrupt:
    print("I. was. WORKING ON THAT...")
#6
try:
    1 / 0
except ArithmeticError as e:
    print(e)
#7
my_list = [1, 2, 3]
try:
    print(my_list[8008135])
except IndexError as e:
    print(e)
#8
my_dict = {"a": 1}
try:
    print(my_dict["b"])
except KeyError as e:
    print(e)
#9
try:
    "2" + 2
except TypeError as e:
    print(e)
#10
try:
    int("hello")
except ValueError as e:
    print(e)

#Part 2
#1
try:
    result = 1337 / 0
except ZeroDivisionError:
    print("Sorry, This isnt Idiocracy. You cant divide by zero")
#2
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except LookupError:
    print("Lookup error caught!")
except IndexError:
    print("Index error caught!")
#3
def risky_function():
    return 1 / 0

try:
    risky_function()
except ZeroDivisionError:
    print("Hmm.. Youve been caught RED-HANDED trying to divide by zero! What do you have to say for yourself?")
#4
def risky_function():
    raise ValueError("Oops!")

def handler():
    try:
        risky_function()
    except ValueError as e:
        print(f"Caught inside handler: {e}")

handler()

# Challenge Activity
import webbrowser
def Expedition():
    try:
        age = int(input("How old are you?: "))
    except ValueError:
        print("Im gonna need a numberical number here champ")
    
    if age < 0:
        raise ValueError("You havent been born yet. Are... are you even real?")
    elif 18 <= age <= 50:
        print(f"Congrats, You are {age} years old and eligible to go on the Expedition!")
        webbrowser.open("https://www.youtube.com/watch?v=tKjZuykKY1I&list=RDtKjZuykKY1I&start_radio=1")
    elif 50 < age <= 100:
        print("Well holy crap, do you have your AARP card yet?")
    else:
        print("Ok, not all of use can be cryogenically frozen and still look amazing...")

try:
    Expedition()
except ValueError as e:
    print(e)