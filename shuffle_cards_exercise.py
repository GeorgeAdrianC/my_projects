import random

"""Card shuffle generator."""

def create_deck():
    numbers = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    suit = ["s","h","d","c"]
    pack = []
    counter = 0    
    while counter < 104:
        for nr in numbers:
            for st in suit:
                pairs = nr + st
                counter += len(pairs)                 
                pack.append(pairs)
    return pack                

def shuffle():
    pack = create_deck()
    shuffled_pack = []
    counter = 0
    while counter < 104:        
        shuffled_card = random.choice(pack)
        counter += len(shuffled_card)
        shuffled_pack.append(shuffled_card)
    return shuffled_pack
           
print(f"This is the deck :\n{create_deck()}")
print(f"This is the shuffled deck:\n{shuffle()}")
deck = shuffle()
deck_lenght = len(deck)
print(f"Deck lenght: {deck_lenght}")

# def deal(hand, cards, deck):
deck = shuffle()  
hand_1 = []
hand_2 = []
hand_3 = []
hand_4 = []
updated_deck = []
while len(hand_1) < 4:
    
    shuffled_card = random.choice(deck)
    hand_1.append(shuffled_card)
    deck.remove(shuffled_card)
    shuffled_card2 = random.choice(deck)
    hand_2.append(shuffled_card2)
    deck.remove(shuffled_card2)
    shuffled_card3 = random.choice(deck)
    hand_3.append(shuffled_card3)
    deck.remove(shuffled_card3)
    shuffled_card4 = random.choice(deck)
    hand_4.append(shuffled_card4)
    deck.remove(shuffled_card4)


print(f"First hand: {hand_1}\nSecond hand: {hand_2}\nThird hand: {hand_3}\nForth hand: {hand_4}")
print(f"Remaining cards: {deck}")
deck_lenght = len(deck)
print(f"Deck lenght: {deck_lenght}")
