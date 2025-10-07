# Part 1
#1
Fruits = ("Strawberry", "Apple", "Banana", "Kiwi")
print(Fruits[1])
#2
print(Fruits[2:4])
#3
list_colors = ["Red", "Orange", "Yellow", "Green"]
tuple_colors = tuple(list_colors)
print(tuple_colors)
Farfanuggen = ("Shlamawamadingdong",)
print(type(Farfanuggen))
#4
#Farfanuggen[0] = 8008135
#we get a type error because tuples are immutable
#5
warkwark = ("never", "gonna", "give", "you", "up", ["never", "gonna", "let", "you", "down"],)
print(warkwark)
rickrolled = warkwark[5]
rickrolled.append("neven gonna run around and desert you")
print(warkwark)
#5 bonus
#you can change the tuple by setting the variable to a new tuple but you cant append the tuple
# warkwark.append("down") gives an error
warkwark = ("I believe in a thing called love")
print(warkwark)
#6
tuple_with_list = (1, [2, 3], 4)
list_with_tuple = [("a", "b"), ("c", "d")]
tuple_with_lisp = tuple_with_list[1]
tuple_with_lisp.append(8008135)
print(tuple_with_list)

# just wanted to see if you could add random as a field in a dictionary
import random
spells = {
    "Fireball": random.randint(1,15)
}
print(f"Fireball hits {spells['Fireball']} damage!")

#part 2
#1
fav_book = {
    "Name": "A Wizard of Earthsea",
    "Author": "Ursula K. Le Guin",
    "Genre": "Fantasy"
}
print(fav_book)

#2
fav_book["Pages"] = 205
del fav_book["Genre"]
print(fav_book)

#3
for key in fav_book:
    print(key, ": ", fav_book[key], sep="") # had to make it look purdy
#3 Bonus
for value in fav_book.values():
    print(value)

#4
