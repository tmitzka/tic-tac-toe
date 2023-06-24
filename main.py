#!/usr/bin/python3
"""A text-based game of Tic Tac Toe."""

from ttt_classes import Game, Player


def main():
    """Main function that uses methods from modules."""

    print("Welcome to Tic Tac Toe!")
    game = Game([
        Player(name="Human", is_human=True),
        Player(name="Computer", is_human=False),
    ])
    # print(game)
    while True:
        current_player = game.players[0]
        indices_empty = game.get_indices_empty()
        if current_player.is_human:
            game.show_grid()
            chosen_index = current_player.choose_field_human(indices_empty)
        else:
            index_win_block = game.win_or_block()
            if index_win_block:
                chosen_index = index_win_block
            else:
                chosen_index = current_player.choose_field_computer(indices_empty)
        game.place_mark(chosen_index)
        if game.three_in_a_row():
            print(f"\n{current_player.name} won!")
            game.show_grid()
            break
        game.switch_players()



if __name__ == "__main__":
    main()
