"""Classes for a game of Tic Tac Toe."""

from random import choice

PLAYER_MARKS = "X", "O"
EMPTY_MARK = "-"


class Game:
    """A class representing a game of Tic Tac Toe."""

    def __init__(self, players: list):
        """Initialize attributes."""

        self.players = players
        self.players[0].mark, self.players[1].mark = PLAYER_MARKS
        self.grid = [EMPTY_MARK for _ in range(9)]

    def show_grid(self):
        """Show the current game grid."""
        print()
        print(" ".join(self.grid[0:3]))
        print(" ".join(self.grid[3:6]))
        print(" ".join(self.grid[6:9]))
        print()

    def get_indices_empty(self) -> list[int]:
        """Get indices of all empty fields for players to choose from."""
        return [i for i in range(9) if self.grid[i] == EMPTY_MARK]

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
        if (
            self.grid[0] == self.grid[4] == self.grid[8]
            and self.grid[0] in PLAYER_MARKS
        ):
            return True
        if (
            self.grid[2] == self.grid[4] == self.grid[6]
            and self.grid[2] in PLAYER_MARKS
        ):
            return True
        return False

    def win_or_block(self) -> int | None:
        """Find an incomplete row and return the missing index.

        First, search for the current player's mark.
        Second, search for the opponent player's mark.
        Use an indexed list to keep track of the original row indices.
        """
        indexed_grid = list(enumerate(self.grid))
        for player in self.players:
            current_mark = player.mark
            # Check horizontal rows.
            for indexed_row in (
                indexed_grid[0:3],
                indexed_grid[3:6],
                indexed_grid[6:9],
            ):
                row_marks = [element[1] for element in indexed_row]
                if (
                    row_marks.count(current_mark) == 2
                    and row_marks.count(EMPTY_MARK) == 1
                ):
                    empty_index = row_marks.index(EMPTY_MARK)
                    return indexed_row[empty_index][0]
            # Check columns.
            for indexed_column in (
                indexed_grid[0:7:3],
                indexed_grid[1:8:3],
                indexed_grid[2:9:3],
            ):
                column_marks = [element[1] for element in indexed_column]
                if (
                    column_marks.count(current_mark) == 2
                    and column_marks.count(EMPTY_MARK) == 1
                ):
                    empty_index = column_marks.index(EMPTY_MARK)
                    return indexed_column[empty_index][0]
            # Check diagonal rows.
            for indexed_diagonal in (indexed_grid[0:9:4], indexed_grid[2:7:2]):
                diagonal_marks = [element[1] for element in indexed_diagonal]
                if (
                    diagonal_marks.count(current_mark) == 2
                    and diagonal_marks.count(EMPTY_MARK) == 1
                ):
                    empty_index = diagonal_marks.index(EMPTY_MARK)
                    return indexed_diagonal[empty_index][0]
        return None

    def place_mark(self, grid_index):
        """Place the current player's mark at the chosen field."""
        if self.grid[grid_index] == EMPTY_MARK:
            self.grid[grid_index] = self.players[0].mark
            print(f"Field {grid_index + 1} was marked with {self.players[0].mark}.")
        else:
            raise ValueError("The chosen field is not empty")

    def switch_players(self):
        """Reverse order of player list."""
        self.players.reverse()
        print(f"\nNow it's your turn, {self.players[0].name}!")

    @staticmethod
    def play_again() -> bool:
        """Play again?"""
        answer = input("Play again? (y/n) ")
        return answer.lower() == "y"

    def start_new_game(self):
        """Reset attributes for a new game."""
        self.grid = [EMPTY_MARK for _ in range(9)]
        if not self.players[0].is_human:
            self.players.reverse()
        print("A new game is about to start.")


class Player:
    """A class representing a player of Tic Tac Toe."""

    def __init__(self, name: str, is_human: bool):
        self.name = name
        self.is_human = is_human
        self.mark = ""

    def __repr__(self) -> str:
        return f"{self.name} ({self.mark})"

    @staticmethod
    def choose_field_human(indices_empty: list[int]) -> int:
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

    @staticmethod
    def choose_field_computer(indices_empty: list[int]) -> int:
        """Choose an empty field for a computer player.

        Choose either the center field or a random field.
        """
        index = 4 if 4 in indices_empty else choice(indices_empty)
        return index
