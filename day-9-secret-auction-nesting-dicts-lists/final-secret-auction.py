

more_bidders = True

def tally_bids(participants_log):
    highest_bid = 0
    highest_bidder = ''
    for key, value in bidders.items():
        if value > highest_bid:
            highest_bid = value
            highest_bidder = key
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

while more_bidders:
    print("Welcome to the secret auction program.")
    bidder_name = input("What is your name?\n")
    bidder_bid = round(float(input("What's your bid?\n")), 2)
    more_bidders_question = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    bidders = {}
    
    bidders[bidder_name] = bidder_bid

    if more_bidders_question == 'no':
        more_bidders = False
        tally_bids(participants_log=bidders)