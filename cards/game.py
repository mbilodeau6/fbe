from deck import Deck
from player import Player
from frustration_rules import FrustrationRules
from random import randrange, seed

class Game:
    def initialize_players(self, player_names):
        self.players = {}

        for player_name in player_names:
            self.players[player_name] = Player(player_name)

    def __init__(self, player_names):
        if len(player_names) < 2:
            raise ValueError("Require a minimum of 2 players")

        self.players_in_order = player_names[:]
        self.initialize_players(player_names)
        self.top_of_discard = None

        self.deck = Deck(True)
        self.deck.shuffle()

    def start_game(self):
        for i in range(FrustrationRules.get_card_deal_count()):
            for player in self.players.values():
                player.hand.append(self.deck.get_next_card())

        self.top_of_discard = self.deck.get_next_card()

        self.player_turn = randrange(0, len(self.players))

    def display_game(self):
        for player in self.players.values():
            print(f"Name: {player.name}; Score: {player.score}")

            print("\tHand: ", end="")
            for card in player.hand:
                print(f"{repr(card)}", end="; ")
            print()

        print()

        # TODO: There should be a game_state to determine state
        if self.top_of_discard is not None:
            print(f"Top of Discard: {self.top_of_discard}")
            print(f"Player Turn: {self.players_in_order[self.player_turn]}")

    # TODO: Should use player_guid instead of name to identify player
    # TODO: Should verify the player has the card they are discarding
    def discard_card(self, player_name, card_to_discard):
        if player_name != self.whose_turn_is_it():
           raise ValueError(f"It is not {player_name}'s turn.")

        self.top_of_discard = card_to_discard
        self.players[player_name].hand.remove(card_to_discard)

    # TODO: Improve logic for calling the method at the wrong time
    def whose_turn_is_it(self):
        if self.player_turn is None:
            return None

        return self.players_in_order[self.player_turn]