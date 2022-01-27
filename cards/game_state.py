import enum

class GameState(enum.Enum):
    initializing = 1
    start_round = 3
    cards_exhausted = 4
    end_round = 5
    end_game = 6


