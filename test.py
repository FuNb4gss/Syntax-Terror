def Wassabi():
    print("Hello, World!")
    
Wassabi()

def fanta(name):
    print(f"Do you want to {name}{name}?")
    
fanta("Fanta")


def gains(a, b):
    print(a + b)
    
gains(120, 200)

def diet_pepsi(diet, pepsi):
    return diet + pepsi

result = diet_pepsi(10, 20)
print(result)

def check_number(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return None

print(check_number(5)) #output should be "Positive"
print(check_number(-2)) #output should be None
print(check_number(0)) #output should be "Zero"

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(10)) # Output should be 3628800 (yes i did the math)
print(factorial(3)) # Output should be 6
print(factorial(100)) # Output Should be higher than my pea-brain can count <3

def countdown(number):
    while number > 0:
        print(number)
        number -= 1
    print("Blastoff! *insert fart sound here*")
    
countdown(5)

def countdown(number):
    if number <= 0:
        print("Blastoff! *insert fart sound here*")
    else:
        print(number)
        countdown(number - 1)

countdown(5)
