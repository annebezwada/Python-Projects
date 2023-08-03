# card class

#global variable
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13,
          'Ace': 14}

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        #values lookup that corresponds to global variable
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit 
    
two_hearts = Card("Hearts", "Two")
#print (two_hearts)

three_of_clubs = Card("Clubs", "Three")
#print (values[three_of_clubs.rank])

#print out the rank value (2) based on values dictionary specified above
#print (values[two_hearts.rank])

#print (two_hearts.value == three_of_clubs.value)

#Deck class
#Instantiate a new deck
    #Create all 52 Card objects
    #Hold as a list of Card objects
#Shuffle a Deck through a medthod call
    #Random library shuffle() function
#Deal cards from the Deck object
    #Pop method from Cards list

class Deck:
    
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        #pop() method removes item at specfified index
        return self.all_cards.pop()
        

new_deck = Deck()
#bottom_card = new_deck.all_cards[-1]
#print(bottom_card)

new_deck.shuffle()
mycard = new_deck.deal_one()
print(mycard)
#print(new_deck.all_cards[-1])
print(len(new_deck.all_cards))


#Player Class
    #Used to hold a player's current list of cards
    #add or remove cards from their "hand" (list of Card objects)
    #be able to add a single card or multiple cards to list - one method call
    #translate a Deck/Hand of cards w/ a top and bottom to a Python list
    #use pop(), append (add), extend (takes a list amnd merges it with existing list) methods


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            #For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
new_player = Player("Andrew")
new_player.add_cards(mycard)
print(new_player.all_cards[0])

new_player.add_cards([mycard, mycard,mycard])
print(new_player)

new_player.remove_one()
print(new_player)

#Game logic - P1
# 1. Create 2 instances in Player Class - Player One & Player Two, New Deck 
# while game_on --> card == card
# while at_war (2 can happen at the same time)
# game_one = False --> Winner!

#GAME SETUP - P2
player_one = Player("One")
player_two = Player("Two")

#created new deck and shuffled it
new_deck = Deck()
new_deck.shuffle()

#split the deck between the players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#set a variable just to have the game continue until someone loses
game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")

# PLAYER ONE
    if len(player_one.all_cards) == 0:
        print ('Player One, out of cards! Player Two wins!')
        game_on = False
        break
# PLAYER TWO
    if len(player_two.all_cards) == 0:
        print ('Player Two, out of cards! Player One wins!')
        game_on = False
        break

    # START A NEW ROUND
    #starts of empty
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    #checking to see if players cards are >, <, or = each other - P3
    # while at_war

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print("Plater One unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Plater Two unable to declare war")
                print("PLAYER ONE WINS!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

