import random

def convert_to_int(card_val):
    card_val_conv = {'A': [1, 11], 'J': 10, 'Q': 10, 'K': 10}
    return card_val_conv[card_val]

class Deck:
    cards = [
                    ('H', 'A'), ('H', 2), ('H', 3), ('H', 4), ('H', 5), ('H', 6), ('H', 7), ('H', 8), ('H', 9), ('H', 10), ('H', 'J'), ('H', 'Q'), ('H', 'K'),
                    ('D', 'A'), ('D', 2), ('D', 3), ('D', 4), ('D', 5), ('D', 6), ('D', 7), ('D', 8), ('D', 9), ('D', 10), ('D', 'J'), ('D', 'Q'), ('D', 'K'),
                    ('S', 'A'), ('S', 2), ('S', 3), ('S', 4), ('S', 5), ('S', 6), ('S', 7), ('S', 8), ('S', 9), ('S', 10), ('S', 'J'), ('S', 'Q'), ('S', 'K'),
                    ('C', 'A'), ('C', 2), ('C', 3), ('C', 4), ('C', 5), ('C', 6), ('C', 7), ('C', 8), ('C', 9), ('C', 10), ('C', 'J'), ('C', 'Q'), ('C', 'K'),
                ]
    def __init__(self):
        self.cards = cards

    def shuffle_cards(self):
        return random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Card:
    def __init__(self, suit, val, name):
        self.suit = suit
        self.val = val
        self.name = name
    

class Hand:
    def __init__(self):
        self.cards = []

    def show(self):
        key = {'H': 'Hearts', 'D':'Diamonds', 'S': 'Spades', 'C': 'Clubs'}

        for card in cards:
            print(f'{card[1]} of {key[card[0]]}')

    def hand_sum(self, cards):
        sum = 0
        ace_count = 0
        for card in cards:
            if type(card[1]) is not int:
                if card[1] == 'A':
                    ace_count += 1
                else: 
                    sum += 10
            else:
                sum += card[1]

        if ace_count == 0 and sum <= 21:
            return sum
        if ace_count !=0 and sum <= 21:
            buffer = 21 - sum
            for a in range(ace_count):
                if sum + 11 <= 21:
                    sum += 11
                elif sum + 1 <=21:
                    sum += 1
                else:
                    return 'BUST!'
        return 'BUST!'

if __name__ == '__main__':
    d = Deck
    print(d.cards)

    d.shuffle_cards()