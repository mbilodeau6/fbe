class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def display(self):
        print(f"Card {self.suit}:{self.rank}")



