import time
import sys
import random

# The start of my auction project! :)
# first i will recieve and store information about the customer and what they are selling!

name = input("Hello! Welcome to the auction! What is your name?: ")
time.sleep(1)
print(f"Welcome {name} and thank you for choosing Weenie Hunt Auctions!")
time.sleep(1)

while True:
    question = input(f"Would you like to auction an item today?(Yes/No): ").lower()

    if question in ["y", "yes"]:
        item = input("What item is it that you are auctioning today?: ")
        break
    elif question in ["n", "no"]:
        print(f"Well {name}, wtf are you doing here? I think you're looking for Weenie Hunt Jr.")
        sys.exit()
    else:
        print("1001001 is a palindrome. In binary its equal to the number 73. I figured if you were gonna waste my time I could learn ya something today! Now, try again please.")
        time.sleep(1)
time.sleep(1)



while True:
    item_price = int(input(f"How much would you like to sell your {item} for? ($200min/$3000max): $"))
    if item_price < 200:
        print("We have a $200 min auction price")
        time.sleep(1)
        continue
    elif item_price > 3000:
        print("Here, let me get you your glasses 👓")
        time.sleep(1)
        continue
    else:
        break

print(f"Ok {name}, Lets go ahead and list your {item} for ${item_price}!")
time.sleep(1)

# instead of bidding on the same item the customer just listed for sale, i will be allowing them to choose from other items and what the current highest bid is

auction_items = ["PC", "PS5", "Excalibur", "Dirt Bike", "TV"]
auction_prices = [1000, 400, 500, 1500, 200]

generated_price = random.randint(item_price, 3000)

total = generated_price


while True:
    question = input("Would you like to bid on any items while your here?(Yes/No): ").lower()

    if question in ["y", "yes"]:
        print("Thats a bold move Cotton, lets see if it pays off!")
        time.sleep(1)
        break
    elif question in ["n", "no"]:
        print("Ok! Lets see what your item ends up selling for today!")
        time.sleep(1)
        print(f"Conratulations {name} your {item} sold to the highest bidder for ${generated_price}! We will see you next time!")
        print(generated_price)
        sys.exit()
    else:
        print("Sorry, I asked for a Yes or No. Not gibberish! Please try again")

print(f"Oh, look at that! While we were making our way to the bidding table your {item} sold!")
time.sleep(1)
print(f"Which means you now have ${total} to bid with!")
time.sleep(2)

won_items = []

# going to use this function to be able to call back to it if the customer has any remaining money left over and wants to bid on another item

def auction_bidding():
    global total
    global won_items
    

# this is to loop over all the items in the lists

    while True:
        print("Here is a list of our available items with their current highest bid")
        time.sleep(1)
        for i in range(len(auction_items)):
            print(f"{i+1}. {auction_items[i]} - ${auction_prices[i]}")
            time.sleep(1)

        try:
            item_choice = int(input("Which item would you like to bid on? (Enter number, or 0 to quit): "))
        except ValueError:
            print("Your mother was a hamster, and your father smelled of elderberries! Now, please enter a correct choice if you do not wish to suffer another burn")
            continue
        
        if item_choice == 0:
            if len(won_items) > 1:
                items_string = ", ".join(won_items[:-1]) + " and " + won_items[-1]
            else:
                items_string = won_items[0]
            print(f"Congratulations again on winning {items_string} today!")
            print("Thanks for using Wennie Hut Auctions today! We will see you again soon! *cough* hopefully not *cough* BYEE!!!!")
            sys.exit()
        if item_choice < 1 or item_choice > len(auction_items):
            print("Id agree with you, but then we'd both be wrong. Please input a correct choice")
            continue
        
        # this is going to remove the item that was selected
        item_index = item_choice - 1

        bid = int(input(f"How much would you like to be on {auction_items[item_index]}? Current highest bid is ${auction_prices[item_index]}: $"))

        if bid <= auction_prices[item_index]:
            print(f"Damn, I guess ill have to add Braille to my auctions lists because you clearly cant see that your bid isnt high enough...Try again")
        elif bid > total:
            print(f"That item is ${auction_prices[item_index]}, You only have {total}. Ill let you figure that out whats going on there 👍")
        else:
            print(f"Congratulations! You won {auction_items[item_index]} for ${bid}!!")
            time.sleep(2)
            total -= bid
            won_items.append(auction_items[item_index])
            del auction_items[item_index]
            del auction_prices[item_index]
            return total
        
# calling the function to start the bidding process       
auction_bidding()

# after first bid is made and is succesful here we will ask if they would like to bid again with knowing how much money they have remaining
while True:
    continue_bid = input(f"You now have ${total} left, would you like to bid on any of the other items?:(Y/N) ").lower()
    if continue_bid in ["y", "yes"]:
            bid_again = auction_bidding()
    elif continue_bid in ["n", "no"]:
        if len(won_items) > 1:
            items_string = ", ".join(won_items[:-1]) + " and " + won_items[-1]
        else:
            items_string = won_items[0]
        print(f"Congratulations again on winning {items_string} today!")
        print("Thanks for using Wennie Hut Auctions today! We will see you again soon! *cough* hopefully not *cough* BYEE!!!!")
        sys.exit()
    else:
        print("I see we are doing this whole 'I cant read' shit again...")
        continue


