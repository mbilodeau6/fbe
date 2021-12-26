import enum

class Suit(enum.Enum):
    heart = 1
    diamond = 2
    club = 3
    spade = 4

    def __repr__(self):
        if self == Suit.heart:
            return "H"
        if self == Suit.diamond:
            return "D"
        if self == Suit.club:
            return "C"
        
        return "S"