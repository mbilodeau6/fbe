from _pytest.python_api import raises
import pytest
from game import Game

def create_2_person_game():
    player_names = ["Michael", "Jason"]
    return Game(player_names)

def test_initialize_2_players():
    new_game = create_2_person_game()
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

def test_discard_card():
    new_game = create_2_person_game()
    assert new_game.top_of_discard is None

    new_game.start_game()

    player_name = new_game.whose_turn_is_it()
    player_card_count = len(new_game.players[player_name].hand)
    card_to_discard = new_game.players[player_name].hand[0]
    new_game.discard_card(player_name, card_to_discard)
    assert new_game.top_of_discard == card_to_discard
    assert len(new_game.players[player_name].hand) == player_card_count - 1

def get_other_player_name(player_name):
    other_player = "Michael"
    if player_name == other_player:
        other_player = "Lisa"

    return other_player

def test_wrong_player_discards():
    new_game = create_2_person_game()
    new_game.start_game()

    player_name = new_game.whose_turn_is_it()
    other_player = get_other_player_name(player_name)

    card_to_discard = new_game.players[other_player].hand[0]
    with pytest.raises(ValueError):
        new_game.discard_card(other_player, card_to_discard)

def test_discard_wrong_card():
    new_game = create_2_person_game()
    new_game.start_game()

    player_name = new_game.whose_turn_is_it()
    other_player = get_other_player_name(player_name)

    card_to_discard = new_game.players[other_player].hand[0]
    with pytest.raises(ValueError):
        new_game.discard_card(player_name, card_to_discard)
