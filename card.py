class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def get_rank(self):  # getter method
        return self._rank

    @property  # public variable (attribute) of an instance
    def rank(self):  # getter property
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def __str__(self):
        return f"{self.rank}-{self.suit}"   #  5-Diamonds
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"  # Card('5', 'Diamond')

if __name__ == "__main__":
    c1 = Card('10', 'Clubs')
    c2 = Card('5', 'Diamonds')
    print(f"{c1 = }")
    print(f"{c2 = }")
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
        