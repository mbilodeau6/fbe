from frustration_rules import FrustrationRules
from hand import Hand
from frustration_rules import MAXIMUM_LEVEL, FrustrationRules

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = Hand()
        self.melds = []
        self.level = 1

    def get_level(self):
        return self.level

    def increment_level(self):
        if self.level < MAXIMUM_LEVEL:
            self.level += 1

    def get_score(self):
        return self.score