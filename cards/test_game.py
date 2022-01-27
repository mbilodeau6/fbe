from unittest.mock import PropertyMock
from _pytest.python_api import raises
import pytest
from frustration_rules import CARD_DEAL_COUNT
from game import Game
from card import Card
from game_state import GameState

def create_2_person_game():
    player_names = ["Michael", "Jason"]
    return Game(player_names)

def test_initialize_2_players():
    new_game = create_2_person_game()
    assert len(new_game.players) == 2
    assert "Michael" in new_game.players
    assert "Jason" in new_game.players
    assert new_game.get_current_state() == GameState.initializing

def test_initialize_empty_players():
    player_names = []
    with pytest.raises(ValueError):
        new_game = Game(player_names)

def test_initialize_1_player():
    player_names = ["Michael"]
    with pytest.raises(ValueError):
        new_game = Game(player_names)

def test_start_game():
    new_game = create_2_person_game()
    new_game.start_game()
    assert new_game.players["Michael"].hand.get_card_count() == CARD_DEAL_COUNT
    assert new_game.players["Jason"].hand.get_card_count() == CARD_DEAL_COUNT

def test_discard_card():
    new_game = create_2_person_game()
    assert len(new_game.discards) == 0

    new_game.start_game()

    player_name = new_game.whose_turn_is_it()
    player_card_count = new_game.players[player_name].hand.get_card_count()
    card_to_discard = new_game.players[player_name].hand.get_card(0)
    new_game.discard_card(player_name, card_to_discard)
    assert new_game.get_top_of_discard() == card_to_discard, "Discarded card should be on top of discard pile"
    assert new_game.players[player_name].hand.get_card_count() == player_card_count - 1, "Card count should decrease after discard"
    assert player_name != new_game.whose_turn_is_it(), "Play turn should change after discard"

def test_all_players_get_turn():
    player_names = ["A", "B", "C"]
    new_game = Game(player_names)
    new_game.start_game()

    players_seen = []
    first_player = new_game.whose_turn_is_it()

    for i in range(3):
        current_player = new_game.whose_turn_is_it()
        players_seen.append(current_player)
        new_game.discard_card(current_player, new_game.players[current_player].hand.get_card(0))
    
    assert "A" in players_seen
    assert "B" in players_seen
    assert "C" in players_seen

    assert new_game.whose_turn_is_it() == first_player, "Should wrap to first player after all players have played."

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

    card_to_discard = new_game.players[other_player].hand.get_card(0)
    with pytest.raises(ValueError):
        new_game.discard_card(other_player, card_to_discard)

def test_discard_wrong_card():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    card_to_discard = new_game.players[other_player].hand.get_card(0)
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
    assert player_hand.get_card_count() == 14, "Card not added to player's hand"

    assert selected_card in player_hand, "Drawn card not found in player's hand"

def test_draw_discard():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    prev_discard = new_game.get_top_of_discard()
    selected_card = new_game.draw_discard(player_name)
    assert selected_card == prev_discard, "Unexpected card returned"
    assert new_game.get_top_of_discard() != prev_discard, "Discard didn't change"

    player_hand = new_game.get_player_hand(player_name)
    assert player_hand.get_card_count() == 14, "Card not added to player's hand"

    assert selected_card in player_hand, "Drawn card not found in player's hand"

def test_get_player_hand():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)
    assert new_game.get_player_hand(player_name).get_card_count() == CARD_DEAL_COUNT, f"Unexpected card count for {player_name}"
    assert new_game.get_player_hand(other_player).get_card_count() == CARD_DEAL_COUNT, f"Unexpected card count for {other_player}"

def test_has_player_used_all_cards_true(mocker):
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    def mock_get_card_count(self):
        return 0

    mocker.patch('hand.Hand.get_card_count', mock_get_card_count)

    def mock_get_current_state(self):
        return GameState.start_round

    mocker.patch('game.Game.get_current_state', mock_get_current_state)
    
    assert new_game.has_player_used_all_cards()

    # with mocker.patch('game.Game.get_current_state', new_callable=PropertyMock, return_value=True) as mock_get_current_state:

def test_has_player_used_all_cards_false():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)
    assert not new_game.has_player_used_all_cards()

def test_get_winner_before_game_won():
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)
    assert len(new_game.get_winner()) == 0

def test_get_winner_on_level(mocker):
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    def mock_get_level(self):
        if self.name == "Jason":
            return 13
        else:
            return 12

    mocker.patch('player.Player.get_level', mock_get_level)

    assert len(new_game.get_winner()) == 1
    assert "Jason" in new_game.get_winner()

def test_get_winner_on_score(mocker):
    new_game = create_2_person_game()
    player_name, other_player = start_and_get_players(new_game)

    def mock_get_level(self):
        return 13

    def mock_get_score(self):
        if self.name == "Jason":
            return 200
        else:
            return 100

    mocker.patch('player.Player.get_level', mock_get_level)
    mocker.patch('player.Player.get_score', mock_get_score)

    assert len(new_game.get_winner()) == 1
    assert "Michael" in new_game.get_winner()

def test_get_winner_multiple_winners(mocker):
    player_names = ["Michael", "Jason", "Jeff", "Mary"]
    new_game = Game(player_names)
    player_name, other_player = start_and_get_players(new_game)

    def mock_get_level(self):
        return 13

    def mock_get_score(self):
        if self.name == "Jason" or self.name == "Michael":
            return 200
        else:
            return 100

    mocker.patch('player.Player.get_level', mock_get_level)
    mocker.patch('player.Player.get_score', mock_get_score)

    assert len(new_game.get_winner()) == 2
    assert "Jeff" in new_game.get_winner()
    assert "Mary" in new_game.get_winner()
