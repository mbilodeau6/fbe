import enum

class GameState(enum.Enum):
    initializing = 1
    start_round = 3,
    cards_exhausted = 4,
    end_round = 5,
    end_game = 6

    @staticmethod
    def get_next_state(game):
        if game.get_current_state() == GameState.start_round:
            if game.has_player_used_all_cards():
                return GameState.end_round
            else:
                return GameState.start_round
        else:
            return GameState.initializing
