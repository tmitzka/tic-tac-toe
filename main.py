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
        game.show_grid()
        game.place_mark()
        if game.three_in_a_row():
            print(f"\n{game.players[0].name} won!")
            game.show_grid()
            break
        game.switch_players()



if __name__ == "__main__":
    main()
