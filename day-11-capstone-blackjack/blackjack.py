
# or draw if even

# if dealer reveals a hand less than 17, they must take another card

# reqs/mechanics
# 2 to 10 count as face value
# j q k = 10
# ace = 1 or 11, if under 21 or over you can decide which value you want it to count as

# 11 counts as 11 until go over 21
# simpler: when a card is drawn its not removed from list
# no jokers
# unlimited deck size

import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playing = True

def deal_card():
    return random.choice(cards)

def check_winner(user_cards, dealer_cards):
    if sum(user_cards) == sum(dealer_cards):
        return f"The hand is a draw with the dealer and user's hand each totaling {sum(dealer_cards)}"
    elif sum(user_cards) > sum(dealer_cards) and sum(user_cards) <= 21:
        return f"User wins the hand with a total of {sum(user_cards)}, against the dealer with a hand of {sum(dealer_cards)}"
    elif sum(dealer_cards) > sum(user_cards) and sum(dealer_cards) <= 21:
         return f"Dealer wins the hand with a total of {sum(dealer_cards)}, against the user with a hand of {sum(user_cards)}"


user_to_play = input("Do you want to play a game of Blackjack?\nType 'yes' or 'no': ")


while playing:
    user_cards = []
    dealer_cards = []
    if user_to_play == 'no':
        playing = False
    elif user_to_play == 'yes':
        while len(user_cards) < 2 and len(dealer_cards) < 2:
            user_cards.append(deal_card())
            dealer_cards.append(deal_card())
        if 11 in user_cards and 10 in user_cards:
            print(f"You got black jack! {user_cards}")
        else:
            print(f"This is the player's hand:\n{user_cards[0]}, {user_cards[1]}")
            print(f"This is the dealer's first card:\n{dealer_cards[0]}")
            hit = True
            while hit:
                hit_or_hold = input("Type 'hit me' to get another card, type 'hold' to pass:\n")

                if hit_or_hold == 'hit me':
                    user_cards.append(deal_card())
                    print(f"Your next card is: {user_cards[len(user_cards) - 1]} for a total hand of {sum(user_cards)}")
                    if sum(user_cards) > 21:
                        if 11 in user_cards:
                            idx = user_cards.index(11)
                            user_cards[idx] = 1
                            print(f"The value of the ace has been adjusted from 11 to 1 to avoid busting the hand for a new total of: {sum(user_cards)}")
                        else:
                            print(f"You bust with a total hand of {sum(user_cards)}.")
                            playing = False
                            hit = False
                elif hit_or_hold == 'hold':
                    print(f"You are holding with a hand of {sum(user_cards)}")
                    print(f"The Dealer flips their remaining card for a current hand of: {sum(dealer_cards)}")
                    hit = False
                    dealer_hit = True
                    while dealer_hit:
                        if sum(dealer_cards) < 17 or sum(dealer_cards) <= sum(user_cards) and sum(dealer_cards) < 21:
                            dealer_cards.append(deal_card())
                            print(f"Dealer's next card is: {dealer_cards[len(dealer_cards) - 1]}, for a total hand of {sum(dealer_cards)}")
                            if sum(dealer_cards) > 21:
                                if 11 in dealer_cards:
                                    idx = dealer_cards.index(11)
                                    dealer_cards[idx] = 1
                                    print(f"The value of the ace has been adjusted from 11 to 1 to avoid busting the hand for a new total of: {sum(dealer_cards)}")
                                else:
                                    print(f"Dealer busts with a total hand of {sum(dealer_cards)}")
                                    playing = False
                                    dealer_hit = False
                        else:
                            dealer_hit = False
                            print(check_winner(user_cards, dealer_cards))
                            playing = False
                else:
                    playing = False 
                    print("Invalid input, you forfeit the hand")   
    else:
        print("Invalid input, you're booted")
        playing = False