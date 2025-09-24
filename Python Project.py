import time
import sys
import random

# The start of my auction project! :)
# first i will recieve and store information about the customer and what they are selling!

name = input("Hello! Welcome to the auction! What is your name?: ")
time.sleep(1)
print(f"Welcome {name} and thank you for choosing Weenie Hunt auctions!")
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


item_price = int(input(f"Ok Great! And how much would you like to sell your {item} for?($3000 max): $"))
time.sleep(1)

print(f"Ok {name}, Lets go ahead and list your beautiful {item} for ${item_price}!")
time.sleep(1)

# instead of bidding on the same item the customer just listed for sale, i will be allowing them to choose from other items and what the current highest bid is

auction_items = ["PC", "PS5", "Excalibur", "Dirt Bike", "TV"]
auction_prices = [1000, 400, 500, 1500, 200]

generated_price = random.randint(item_price, 3000)
total = generated_price


while True:
    question = input("Would you like to bid on any items while your here?(Yes/No): ").lower()

    if question in ["y", "yes"]:
        print("Ok right this way!")
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


# going to use this function to be able to call back to it if the customer has any remaining money left over and wants to bid on another item

def auction_bidding():
    global total
    print("Here is a list of our available items and their current highest bid!")
    time.sleep(1)

# this is to loop over all the items in the lists
    # for i, (item, price) in enumerate(zip(auction_items, auction_prices), start =1):
        #print(f"{i}. {item} - ${price}")


    for i in range(len(auction_items)) and range(len(auction_prices)):
        print(f"{i+1}. {auction_items[i]} - ${auction_prices[i]}")
        time.sleep(1)
        
        

        while True:
            item_choice = int(input("Which of these items would you like to bid on? Remember, your bid has to be higher than the current highest be to win the item: "))
            if item_choice == 1:
                bid_one = int(input(f"How much would you like to bid on {auction_items[0]} for? Current highest bid is ${auction_prices[0]}: $"))

                if auction_prices[0] >= bid_one:
                    print(f"Im sorry, I see math wasnt your best subject. That costs {auction_prices[0]} and you only bid {bid_one}.")
                    time.sleep(1)
                elif auction_prices[0] >= total:
                    print(f"You have {total} and the highest bid for this item is {auction_prices[0]}... what did you think was going to happen?")
                    time.sleep(1)
                else:
                    print(f"Congratualtions! You are now the proud owner of a new {auction_items[0]}")
                    total -= auction_prices[0]
                    auction_items.remove(auction_items[0])
                    auction_prices.remove(auction_prices[0])
                    return total
                
            elif item_choice == 2:
                bid_two = int(input(f"How much would you like to bid on {auction_items[1]} for? Current highest bid is ${auction_prices[1]}: $"))
                if auction_prices[1] >= bid_two or auction_prices[1] >= total:
                    print(f"Im sorry, I see math wasnt your best subject. That costs {auction_prices[1]} and you only bid {bid_two}.")
                    time.sleep(1)
                elif auction_prices[1] >= total:
                    print(f"You have {total} and the highest bid for this item is {auction_prices[1]}... what did you think was going to happen?")
                    time.sleep(1)
                else:
                    print(f"Congratualtions! You are now the proud owner of a new {auction_items[1]}")
                    total -= auction_prices[1]
                    auction_items.remove(auction_items[1])
                    auction_prices.remove(auction_prices[1])
                    return total
                
            elif item_choice == 3:
                bid_three = int(input(f"How much would you like to bid on {auction_items[2]} for? Current highest bid is ${auction_prices[2]}: $"))
                if auction_prices[2] >= bid_three:
                    print(f"Im sorry, I see math wasnt your best subject. That costs {auction_prices[2]} and you only bid {bid_three}.")
                    time.sleep(1)
                elif auction_prices[2] >= total:
                    print(f"You have {total} and the highest bid for this item is {auction_prices[2]}... what did you think was going to happen?")
                else:
                    print(f"Congratualtions! You are now the proud owner of a new {auction_items[2]}")
                    total -= auction_prices[2]
                    auction_items.remove(auction_items[2])
                    auction_prices.remove(auction_prices[2])
                    return total
                
            elif item_choice == 4:
                bid_four = int(input(f"How much would you like to bid on {auction_items[3]} for? Current highest bid is ${auction_prices[3]}: $"))
                if auction_prices[3] >= bid_four:
                    print(f"Im sorry, I see math wasnt your best subject. That costs {auction_prices[3]} and you only bid {bid_four}.")
                    time.sleep(1)
                elif auction_prices[3] >= total:
                    print(f"You have {total} and the highest bid for this item is {auction_prices[3]}... what did you think was going to happen?")
                else:
                    print(f"Congratualtions! You are now the proud owner of a new {auction_items[3]}")
                    total -= auction_prices[3]
                    auction_items.remove(auction_items[3])
                    auction_prices.remove(auction_prices[3])
                    return total
                
            elif item_choice == 5:
                bid_five = int(input(f"How much would you like to bid on {auction_items[4]} for? Current highest bid is ${auction_prices[4]}: $"))
                if auction_prices[4] >= bid_five:
                    print(f"Im sorry, I see math wasnt your best subject. That costs {auction_prices[4]} and you only bid {bid_five}.")
                    time.sleep(1)
                elif auction_prices[4] >= total:
                    print(f"You have {total} and the highest bid for this item is {auction_prices[4]}... what did you think was going to happen?")
                else:
                    print(f"Congratualtions! You are now the proud owner of a new {auction_items[4]}")
                    total -= auction_prices[4]
                    auction_items.remove(auction_items[4])
                    auction_prices.remove(auction_prices[4])
                    return total
                
            else:
                print("Your mother was a hamster, and your father smelled of elderberries! Now, please enter a correct choice if you do not wish to suffer another burn")
                time.sleep(1)

remaining_total = auction_bidding()

print(f"You now have ${remaining_total} left!")
print(auction_items)
print(auction_prices)

auction_bidding()

# I need to make my ifs and elif when choosing an option into a funtion within the function
# in order to loop back without errors of items being removed from the list, i need to use the rang(len()) function



