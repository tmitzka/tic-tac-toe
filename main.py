#!/usr/bin/python3
"""A text-based game of Tic Tac Toe."""

from time import sleep
from ttt_classes import Game, Player


def main():
    """Main function that uses methods from modules."""

    print("Welcome to Tic Tac Toe!")
    players = [
        Player(name="Human", is_human=True),
        Player(name="Computer", is_human=False),
    ]
    game = Game(players)

    while True:
        player = game.players[0]
        indices_empty = game.get_indices_empty()
        final_turn = True if len(indices_empty) == 1 else False

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

        # If all fields are taken, declare a winner or a draw.
        if final_turn:
            if game.three_in_a_row():
                if player.is_human:
                    print(f"\n{player.name}, you won!")
                else:
                    print(f"\n{player.name} won!")
            else:
                print("\nIt's a draw!")
            game.show_grid()

            # Let the user decide whether to start a new game.
            if game.play_again():
                game.start_new_game(players)
            else:
                break

        game.switch_players()


if __name__ == "__main__":
    main()
