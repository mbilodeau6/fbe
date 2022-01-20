from _pytest.python_api import raises
import pytest
from game import Game
from card import Card

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
    assert len(new_game.discards) == 0

    new_game.start_game()

    player_name = new_game.whose_turn_is_it()
    player_card_count = len(new_game.players[player_name].hand)
    card_to_discard = new_game.players[player_name].hand[0]
    new_game.discard_card(player_name, card_to_discard)
    assert new_game.discards[-1] == card_to_discard
    assert len(new_game.players[player_name].hand) == player_card_count - 1

def get_other_player_name(player_name):
    other_player = "Michael"
    if player_name == other_player:
        other_player = "Lisa"

    return other_player

def start_and_get_players(new_game):
    new_game.start_game()

    player_name = new_game.whose_turn_is_it()
    other_player = get_other_player_name(player_name)

    return (player_name, other_player)

def test_wrong_player_discards():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    card_to_discard = new_game.players[other_player].hand[0]
    with pytest.raises(ValueError):
        new_game.discard_card(other_player, card_to_discard)

def test_discard_wrong_card():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    card_to_discard = new_game.players[other_player].hand[0]
    with pytest.raises(ValueError):
        new_game.discard_card(player_name, card_to_discard)

def test_wrong_player_draw_card():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    with pytest.raises(ValueError):
        new_game.draw_card(other_player)

def test_wrong_player_draw_discard():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    with pytest.raises(ValueError):
        new_game.draw_discard(other_player)

def test_draw_card():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    selected_card = new_game.draw_card(player_name)
    assert isinstance(selected_card, Card), "Return value was not a Card."

    player_hand = new_game.get_player_hand(player_name)
    assert len(player_hand) == 14, "Card not added to player's hand"

    assert selected_card in player_hand, "Drawn card not found in player's hand"

def test_draw_discard():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    prev_discard = new_game.get_top_of_discard()
    selected_card = new_game.draw_discard(player_name)
    assert selected_card == prev_discard, "Unexpected card returned"
    assert new_game.get_top_of_discard() != prev_discard, "Discard didn't change"

    player_hand = new_game.get_player_hand(player_name)
    assert len(player_hand) == 14, "Card not added to player's hand"

    assert selected_card in player_hand, "Drawn card not found in player's hand"

def test_get_player_hand():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)
    assert len(new_game.get_player_hand(player_name)) == 13, f"Unexpected card count for {player_name}"
    assert len(new_game.get_player_hand(other_player)) == 13, f"Unexpected card count for {other_player}"
