from game import Game

player_names = ["Michael", "Lisa"]
new_game = Game(player_names)

new_game.display_game()

print("Starting game: ")
new_game.start_game()

done = False

while(not done):
    new_game.display_game()
    print("D(r)aw; (D)iscard; (Q)uit")
    command = input().lower()

    if command == "r":
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

print()