from deck import Deck
from player import Player
from frustration_rules import MAXIMUM_LEVEL, FrustrationRules
from random import randrange, seed
from game_state import GameState

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
        self.discards = []

        self.game_state = GameState.initializing
        self.deck = Deck(True)
        self.deck.shuffle()

    def start_game(self):
        for i in range(FrustrationRules.get_card_deal_count()):
            for player in self.players.values():
                player.hand.add_card(self.deck.get_next_card())

        self.discards.append(self.deck.get_next_card())

        self.player_turn = randrange(0, len(self.players))

    def get_current_state(self):
        return self.game_state

    def get_top_of_discard(self):
        if (len(self.discards) == 0):
            return None

        return self.discards[-1]

    def display_game(self):
        for player in self.players.values():
            print(f"Name: {player.name}; Score: {player.score}")

            print("\tHand: ", end="")
            for card in player.hand:
                print(f"{repr(card)}", end="; ")
            print()

        print()

        # TODO: There should be a game_state to determine state
        if self.game_state != GameState.initializing and self.game_state != GameState.end_game:
            print(f"Top of Discard: {self.get_top_of_discard()}")
            print(f"Player Turn: {self.players_in_order[self.player_turn]}")

    # TODO: Should use player_guid instead of name to identify player
    def discard_card(self, player_name, card_to_discard):
        if player_name != self.whose_turn_is_it():
           raise ValueError(f"It is not {player_name}'s turn.")

        self.discards.append(card_to_discard)
        self.players[player_name].hand.remove_card(card_to_discard)
        self.move_to_next_player()

    # TODO: Improve logic for calling the method at the wrong time
    def whose_turn_is_it(self):
        if self.player_turn is None:
            return None

        return self.players_in_order[self.player_turn]

    def move_to_next_player(self):
        self.player_turn = (self.player_turn + 1) % len(self.players)

    def draw_card(self, player_name):
        if player_name != self.whose_turn_is_it():
            raise ValueError(f"It is not {player_name}'s turn.")

        drawn_card = self.deck.get_next_card()
        self.players[player_name].hand.add_card(drawn_card)
        return drawn_card

    def draw_discard(self, player_name):
        if player_name != self.whose_turn_is_it():
           raise ValueError(f"It is not {player_name}'s turn.")

        drawn_card = self.discards.pop()
        self.players[player_name].hand.add_card(drawn_card)
        return drawn_card

    def get_player_hand(self, player_name):
        return self.players[player_name].hand

    def has_player_used_all_cards(self):
        if self.get_current_state() == GameState.start_round:
            for player in self.players.values():
                if player.hand.get_card_count() == 0:
                    return True

        return False

    def get_winner(self):
        winners = []
        lowest_score = 9000

        for player in self.players.values():
            if player.get_level() == MAXIMUM_LEVEL:
                if player.get_score() < lowest_score:
                    winners.clear()
                    lowest_score = player.get_score()

                if player.get_score() <= lowest_score:
                    winners.append(player.name)

        return winners

    def game_loop(self):
        if self.get_current_state() == GameState.initializing:
            self.start_game()
            self.game_state = GameState.start_round
        elif self.get_current_state() == GameState.start_round:
            # TODO: We need to accept user input here
            if self.has_player_used_all_cards():
                self.game_state = GameState.end_round
        elif self.get_current_state() == GameState.end_round:
            if len(self.get_winner()) != 0:
                # TODO: Announce winner here or in the end_game step?
                self.game_state = GameState.end_game
            else:
                # TODO: Need to shuffle and deal
                self.game_state = GameState.start_round
        elif self.get_current_state() == GameState.end_game:
            pass
        else:
            raise(NotImplemented, 'Unsupported game state hit')
