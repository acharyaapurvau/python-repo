from os import system

auction_details = {}
more_bidders = True

while more_bidders:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction_details[name] = bid

    more = input("Are there more bidders? Yes or No: ").lower()
    if more == "yes":
        system("cls")  # or system("clear") on Mac/Linux
    else:
        more_bidders = False
        print("Auction over!")

# Determine highest bidder
max_bid = 0
max_bidder = ""

for bidder in auction_details:
    if auction_details[bidder] > max_bid:
        max_bid = auction_details[bidder]
        max_bidder = bidder

print(f"The highest bidder is {max_bidder} with a bid of ${max_bid}.")
