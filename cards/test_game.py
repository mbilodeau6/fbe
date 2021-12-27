from _pytest.python_api import raises
import pytest
from game import Game

def test_initialize_2_players():
    player_names = ["Michael", "Jason"]
    new_game = Game(player_names)
    assert len(new_game.players) == 2
    assert "Michael" in new_game.players
    assert "Jason" in new_game.players

def test_initialize_empty_players():
    player_names = []
    with pytest.raises(ValueError):
        new_game = Game(player_names)

def test_initialize_1_player():
    player_names = ["Michael"]
    with pytest.raises(ValueError):
        new_game = Game(player_names)
