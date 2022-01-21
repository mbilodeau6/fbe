from hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = Hand()
        self.melds = []
