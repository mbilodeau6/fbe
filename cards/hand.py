class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_card(self, index):
        return self.cards[index]

    def remove_card(self, index):
        del self.cards[index]

    def get_card_count(self):
        return len(self.cards)