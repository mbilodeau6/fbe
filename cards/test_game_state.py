from _pytest.python_api import raises
import pytest
from game_state import GameState
from game import Game

def test_get_next_state_stay_in_initializing():
    player_names = ["A", "B"]
    new_game = Game(player_names)

    assert GameState.get_next_state(new_game) == GameState.initializing

def test_get_next_state_initializing_to_start_round():
    player_names = ["A", "B"]
    new_game = Game(player_names)
    new_game.start_game()

    assert GameState.get_next_state(new_game) == GameState.start_round

def test_get_next_state_start_round_to_end_round(mocker):
    player_names = ["A", "B"]
    new_game = Game(player_names)
    new_game.start_game()

    def mock_has_player_used_all_cards(self):
        return True

    mocker.patch('game.Game.has_player_used_all_cards', mock_has_player_used_all_cards)

    assert GameState.get_next_state(new_game) == GameState.end_round
