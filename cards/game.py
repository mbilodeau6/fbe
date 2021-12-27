from deck import Deck
from player import Player
from frustration_rules import FrustrationRules

class Game:
    def initialize_players(self, player_names):
        self.players = {}

        for player_name in player_names:
            self.players[player_name] = Player(player_name)

    def __init__(self, player_names):
        if len(player_names) < 2:
            raise ValueError("Require a minimum of 2 players")

        self.initialize_players(player_names)

        self.deck = Deck(True)
        self.deck.shuffle()

    def start_game(self):
        for i in range(FrustrationRules.get_card_deal_count()):
            for player in self.players.values():
                player.hand.append(self.deck.get_next_card())

    def display_game(self):
        for player in self.players.values():
            print(f"Name: {player.name}; Score: {player.score}")

            print("\tHand: ", end="")
            for card in player.hand:
                print(f"{repr(card)}", end="; ")
            print()