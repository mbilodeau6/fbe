import enum

class Rank(enum.Enum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    joker = 14

    def __repr__(self):
        if self == Rank.ace:
            return "A"
        if self == Rank.ten:
            return "T"
        if self == Rank.jack:
            return "J"
        if self == Rank.queen:
            return "Q"
        if self == Rank.king:
            return "K"
        if self == Rank.joker:
            return "W"

        return str(self.value)