#!/usr/bin/python3
"""A text-based game of Tic Tac Toe."""

from time import sleep
from ttt_classes import Game, Player


def main():
    """Main function that uses methods from modules."""

    print("Welcome to Tic Tac Toe!")

    game = Game(
        [
            Player(name="Human", is_human=True),
            Player(name="Computer", is_human=False),
        ]
    )

    while True:
        player = game.players[0]
        indices_empty = game.get_indices_empty()
        new_game = False

        if player.is_human:
            # Let the human player choose a field.
            game.show_grid()
            sleep(2)
            chosen_index = player.choose_field_human(indices_empty)
        else:
            # Let the computer player choose a field.
            index_win_block = game.win_or_block()
            if index_win_block:
                chosen_index = index_win_block
            else:
                chosen_index = player.choose_field_computer(indices_empty)
        sleep(2)
        game.place_mark(chosen_index)
        sleep(2)

        # Declare a winner or a draw.
        if game.three_in_a_row() or len(indices_empty) == 1:
            if game.three_in_a_row():
                if player.is_human:
                    print(f"\n* {player.name}, you win! *")
                else:
                    print(f"\n* {player.name} wins! *")
            else:
                print("\n* It's a draw! *")
            game.show_grid()

            # Let the user decide whether to start a new game.
            if game.play_again():
                game.start_new_game()
                # Change flag variable so that player order won't
                # get reversed at the end of this iteration.
                new_game = True
            else:
                break

        if not new_game:
            # Reverse order of players for the next iteration.
            game.switch_players()


if __name__ == "__main__":
    main()
