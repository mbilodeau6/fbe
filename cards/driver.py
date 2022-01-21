from frustration_rules import FrustrationRules
from game import Game

player_names = ["Michael", "Lisa"]
new_game = Game(player_names)

new_game.display_game()

print("Starting game: ")
new_game.start_game()

done = False

while(not done):
    new_game.display_game()
    print("Draw (N)ew; Draw from (D)iscard; Sort by (R)ank; Sort by (S); (Q)uit")
    command = input().lower()

    if command == "n":
        selected_card = new_game.draw_card(new_game.whose_turn_is_it())
        print(f"{new_game.whose_turn_is_it()} drew a {selected_card}")
    elif command == "d":
        selected_card = new_game.draw_discard(new_game.whose_turn_is_it())
        print(f"{new_game.whose_turn_is_it()} picked up discarded {selected_card}")
    elif command == "q":
        done = True
        continue
    elif command == "r":
        new_game.players[new_game.whose_turn_is_it()].hand.sort_by_rank()
        continue
    elif command == "s":
        new_game.players[new_game.whose_turn_is_it()].hand.sort_by_suit()
        continue
    else:
        print("Invalid command. Please try again.")
        continue

    new_game.display_game()
    print("(D)iscard; (Q)uit")
    command = input().lower()

    if command == "d":
        print(f"Select card to discard (0-{new_game.get_player_hand(new_game.whose_turn_is_it()).get_card_count()-1})")
        card_index = int(input())
        new_game.discard_card(new_game.whose_turn_is_it(), new_game.get_player_hand(new_game.whose_turn_is_it()).get_card(card_index))
    elif command == "q":
        done = True
        continue
    else:
        print("Invalid command. Please try again.")
        continue

print()

for key, value in new_game.players.items():
    print(f"{key}'s score: {FrustrationRules.get_hand_value(value.hand)}")

print()