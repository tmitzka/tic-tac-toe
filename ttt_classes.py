"""Classes for a game of Tic Tac Toe."""

from random import choice
from typing import Optional


class Game:
    """A class representing a game of Tic Tac Toe."""

    def __init__(self, players: list):
        """Initialize attributes."""
        
        self.players = players
        self.PLAYER_MARKS = ("X", "O")
        self.players[0].mark, self.players[1].mark = self.PLAYER_MARKS
        self.EMPTY_MARK = "-"
        # self.grid = [self.EMPTY_MARK for _ in range(9)]
        self.grid = [
            "-", "-", "-",
            "X", "-", "X",
            "O", "-", "O",
        ]

    def __repr__(self) -> str:
        return f"Tic Tac Toe: {self.players[0].name} vs {self.players[1].name}"

    def show_grid(self):
        """Show the game grid in a user-friendly way."""
        print()
        print(" ".join(self.grid[0:3]))
        print(" ".join(self.grid[3:6]))
        print(" ".join(self.grid[6:9]))
        print()

    def check_for_row(self) -> bool:
        """Check whether there's a row of three marks."""
        # Check for horizontal row.
        for row in (self.grid[0:3], self.grid[3:6], self.grid[6:9]):
            if row[0] == row[1] == row[2] and row[0] in self.PLAYER_MARKS:
                return True
        # Check for vertical row.
        for col in (self.grid[0:7:3], self.grid[1:8:3], self.grid[2:9:3]):
            if col[0] == col[1] == col[2] and col[0] in self.PLAYER_MARKS:
                return True
        # Check for diagonal row.
        if (self.grid[0] == self.grid[4] == self.grid[8] and \
            self.grid[0] in self.PLAYER_MARKS):
            return True
        if (self.grid[2] == self.grid[4] == self.grid[6] and \
            self.grid[2] in self.PLAYER_MARKS):
            return True
        return False

    def win_or_block(self) -> Optional[int]:
        """Find an incomplete row and return the missing index."""
        for current_mark in (self.players[0].mark, self.players[1].mark):

            # Check for horizontal row.
            for row in (self.grid[0:3], self.grid[3:6], self.grid[6:9]):
                if row.count(current_mark) == 2 and row.count(self.EMPTY_MARK) == 1:
                    return row.index(self.EMPTY_MARK)
            # Check for vertical row.
            for col in (self.grid[0:7:3], self.grid[1:8:3], self.grid[2:9:3]):
                if col.count(current_mark) == 2 and col.count(self.EMPTY_MARK) == 1:
                    return col.index(self.EMPTY_MARK)
            # Check for diagonal row.
            if (self.grid[0] == self.grid[4] == self.grid[8] and \
                self.grid[0] in self.PLAYER_MARKS):
                # return index
                pass
            if self.grid[2] == self.grid[4] == self.grid[6] == current_mark:
                # return index
                pass

        return None

    def place_mark(self):
        """Place a player mark at the chosen field."""
        indices_empty = [i for i in range(9) if self.grid[i] == "-"]

        if self.players[0].is_human:
            index = self.players[0].choose_field_human(indices_empty)
        else:
            win_block_index = self.win_or_block()
            if win_block_index:
                index = win_block_index
            else:
                index = self.players[0].choose_field_computer(indices_empty)
        self.grid[index] = self.players[0].mark

    def switch_players(self):
        """Reverse order of player list."""
        self.players.reverse()
        print(f"\nNow it's your turn, {self.players[0].name}!")

    def play_again(self) -> bool:
        """Play again?"""
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

    def __repr__(self):
        return f"{self.name} ({self.mark}) has {self.points} points."

    def choose_field_human(self, indices_empty: list[int]) -> int:
        # Human player chooses an empty field.
        # Show field numbers instead of indices to human player.
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
        # Choose the center field if it's empty.
        # Otherwise, choose a random field.
        index = 4 if 4 in indices_empty else choice(indices_empty)
        return index
