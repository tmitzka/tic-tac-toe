"""Classes for a game of Tic Tac Toe."""

from random import choice
from typing import Optional

PLAYER_MARKS = "X", "O"
EMPTY_MARK = "-"


class Game:
    """A class representing a game of Tic Tac Toe."""

    def __init__(self, players: list):
        """Initialize attributes."""

        self.players = players
        self.players[0].mark, self.players[1].mark = PLAYER_MARKS
        # Grid list contains mark characters and index numbers,
        # so that it's clear where marks should be placed.
        # self.grid = [[EMPTY_MARK, i] for i in range(9)]
        # --> Replace self.grid with list comprehension later.
        example_marks = [
            "-", "-", "-",
            "X", "-", "X",
            "O", "-", "O",
        ]
        self.grid = [[example_marks[i], i] for i in range(9)]

    def show_grid(self):
        """Show game grid to human player."""
        if self.players[0].is_human:
            print()
            print(" ".join(self.grid[0:3]))
            print(" ".join(self.grid[3:6]))
            print(" ".join(self.grid[6:9]))
            print()

    def three_in_a_row(self) -> bool:
        """Check whether there's a row of three marks."""
        # Check for horizontal row.
        for row in (self.grid[0:3], self.grid[3:6], self.grid[6:9]):
            if row[0] == row[1] == row[2] and row[0] in PLAYER_MARKS:
                return True
        # Check for vertical row.
        for col in (self.grid[0:7:3], self.grid[1:8:3], self.grid[2:9:3]):
            if col[0] == col[1] == col[2] and col[0] in PLAYER_MARKS:
                return True
        # Check for diagonal row.
        if (self.grid[0] == self.grid[4] == self.grid[8] and \
            self.grid[0] in PLAYER_MARKS):
            return True
        if (self.grid[2] == self.grid[4] == self.grid[6] and \
            self.grid[2] in PLAYER_MARKS):
            return True
        return False

    def win_or_block(self) -> Optional[int]:
        """Find an incomplete row and return the missing index.

        First, search for the current player's mark.
        Second, search for the opponent player's mark.
        """
        for player in self.players:
            current_mark = player.mark
            # Check horizontal rows.
            for row in (self.grid[0:3], self.grid[3:6], self.grid[6:9]):
                if (row.count(current_mark) == 2 \
                    and row.count(EMPTY_MARK) == 1):
                    return row.index(EMPTY_MARK)
            # Check columns.
            for col in (self.grid[0:7:3], self.grid[1:8:3], self.grid[2:9:3]):
                if (col.count(current_mark) == 2 \
                    and col.count(EMPTY_MARK) == 1):
                    return col.index(EMPTY_MARK)
            # Check diagonal rows.
            for d_row in (self.grid[0:9:4], self.grid[2:7:2]):
                if (d_row.count(current_mark) == 2 \
                    and d_row.count(EMPTY_MARK) == 1):
                    return d_row.index(EMPTY_MARK)
        return None

    def place_mark(self):
        """Place a player mark at the chosen field."""
        indices_empty = [i for i in range(9) if self.grid[i] == EMPTY_MARK]

        if self.players[0].is_human:
            index = self.players[0].choose_field_human(indices_empty)
        else:
            win_block_index = self.win_or_block()
            if win_block_index:
                index = win_block_index
            else:
                index = self.players[0].choose_field_computer(indices_empty)
        self.grid[index] = self.players[0].mark
        print(f"Field {index + 1} was marked with '{self.players[0].mark}'.")

    def switch_players(self):
        """Reverse order of player list."""
        self.players.reverse()
        print(f"\nNow it's your turn, {self.players[0].name}!")

    def play_again(self) -> bool:
        """Play again?"""
        answer = input("Play again? (y/n) ")
        if answer == "y":
            return True
        else:
            return False


class Player:
    """A class representing a player of Tic Tac Toe."""

    def __init__(self, name: str, is_human: bool):
        self.name = name
        self.is_human = is_human
        self.mark = ""
        self.points = 0

    def __repr__(self) -> str:
        return f"{self.name} ({self.mark}): {self.points} points"

    def choose_field_human(self, indices_empty: list[int]) -> int:
        """Let the human player choose an empty field.

        Show field numbers (starting from 1) instead of indices.
        """
        empty_field_numbers = [str(i + 1) for i in indices_empty]
        print("Where do you want to place your mark?")
        print(f"Empty fields: {empty_field_numbers}")
        field_number = ""
        while field_number not in empty_field_numbers:
            field_number = input("Enter a field number: ")
            if field_number not in empty_field_numbers:
                print("Please enter the number of an empty field.\n")
        index = int(field_number) - 1
        return index

    def choose_field_computer(self, indices_empty: list[int]) -> int:
        """Choose an empty field for a computer player.

        Choose either the center field or a random field.
        """
        index = 4 if 4 in indices_empty else choice(indices_empty)
        return index
