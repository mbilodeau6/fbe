from game import Game

player_names = ["Michael", "Lisa"]
new_game = Game(player_names)

new_game.display_game()

print("Starting game: ")
new_game.start_game()

done = False

while(not done):
    new_game.display_game()
    print("Draw (N)ew; Draw from (D)iscard; (Q)uit")
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
    else:
        print("Invalid command. Please try again.")
        continue

    new_game.display_game()
    print("(D)iscard; (Q)uit")
    command = input().lower()

    if command == "d":
        print(f"Select card to discard (0-{len(new_game.get_player_hand(new_game.whose_turn_is_it()))-1})")
        card_index = int(input())
        new_game.discard_card(new_game.whose_turn_is_it(), new_game.get_player_hand(new_game.whose_turn_is_it())[card_index])
    elif command == "q":
        done = True
        continue
    else:
        print("Invalid command. Please try again.")
        continue

print()