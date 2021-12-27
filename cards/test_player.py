from player import Player

def test_name():
    expected_name = "Michael"
    new_player = Player(expected_name)
    assert new_player.name == expected_name

def test_initialization():
    new_player = Player("Michael")
    assert new_player.score == 0
    assert len(new_player.hand) == 0
    assert len(new_player.melds) == 0