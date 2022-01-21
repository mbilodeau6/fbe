class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_card(self, index):
        return self.cards[index]

    def remove_card_at_index(self, index):
        del self.cards[index]

    def get_card_count(self):
        return len(self.cards)

    def remove_card(self, card):
        self.cards.remove(card)

    def __iter__(self):
        return HandIterator(self)

class HandIterator:
    def __init__(self, hand):
        self._hand = hand
        self._index = 0

    def __next__(self):
        if self._index < self._hand.get_card_count():
            result = self._hand.get_card(self._index)
            self._index += 1
            return result

        raise StopIteration