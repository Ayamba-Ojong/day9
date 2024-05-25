from replit import clear
# HINT: You can call clear() to clear the output in the console.
#Andy open replit to run this code else it gives an error

from bid_logo import logo

print(logo)
bids = {}
bidding_finish = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finish:
    name = input("What is your name? ")
    bid_price = int(input("What is your bid price? $"))
    bids[name] = bid_price
    other_bidders = input("Are there others who want to bid? Type 'yes' or 'no'\n")
    if other_bidders == "no":
        bidding_finish = True
        find_highest_bidder(bids)
    elif other_bidders == "yes":
        clear()
