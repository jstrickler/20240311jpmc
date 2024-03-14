import random
from card import Card

class CardDeck:
    # class data
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self):
        self._make_cards()

    def _make_cards(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)  # shuffle cards in place

    def draw(self):
        return self._cards.pop()

    def __str__(self):
        return "CardDeck ???"

    def __repr__(self):
        return "CardDeck()"

if __name__ == "__main__":
    c = CardDeck()
    print(f"{c = }")  # uses repr() not str()
    print(c)  #  print(str(c))
    c.shuffle()
    print(f"{c.cards = }\n")
    for _ in range(5):
        card = c.draw() # draw one card
        print(f"{card = }")
