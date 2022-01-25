from player import Player

def test_name():
    expected_name = "Michael"
    new_player = Player(expected_name)
    assert new_player.name == expected_name

def test_initialization():
    new_player = Player("Michael")
    assert new_player.get_score() == 0
    assert new_player.hand.get_card_count() == 0
    assert len(new_player.melds) == 0

def test_increment_level():
    new_player = Player("Michael")
    assert new_player.get_level() == 1
    new_player.increment_level()
    assert new_player.get_level() == 2
    for i in range(13):
        new_player.increment_level()

    assert new_player.get_level() == 13