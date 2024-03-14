from carddeck import CardDeck
from card import Card

class Game:
    pass

class JokerDeck(CardDeck):
    def _make_cards(self):  # overwrite base class method
        super()._make_cards()  # call base class method
        for joker in "Joker1", "Joker2":
            card = Card(joker, joker)
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()

    for _ in range(10):
        card = j.draw()
        print(f"{card = }")
    print('-' * 60)
    print(j.cards)