import random
def shuffle_cards(cards):
    random.shuffle(cards)

class Test:
    cards = [1, 2, 3]
    

if __name__ == '__main__':
    t = Test
    print(t.cards)
    shuffle_cards(t.cards)
    print(t.cards)
