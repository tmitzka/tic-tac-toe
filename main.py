#!/usr/bin/python3
"""A text-based game of Tic Tac Toe."""

from game_player import Game, Player


def main():
    """Main function that uses methods from modules."""

    print("Welcome to Tic Tac Toe!")
    game = Game([
        Player("Human", True),
        Player("Computer", False),
    ])
    # print(game)
    while True:
        game.show_grid()
        game.place_mark()
        if game.check_for_row():
            print(f"\n{game.players[0].name} won!")
            game.show_grid()
            break
        game.switch_players()



if __name__ == "__main__":
    main()
