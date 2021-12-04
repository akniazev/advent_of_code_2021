from __future__ import annotations


class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.called = [[False for _ in row] for row in numbers]

    def check_row(self, index: int) -> bool:
        return all(self.called[index])

    def check_column(self, index: int) -> bool:
        return all([row[index] for row in self.called])

    def find_index_for(self, searched: int) -> tuple[int, int] | None:
        for i, row in enumerate(self.numbers):
            for j, number in enumerate(row):
                if number == searched:
                    return i, j
        return None

    def call_number(self, num: int) -> bool:
        index = self.find_index_for(num)
        if index:
            row, col = index
            self.called[row][col] = True
            return self.check_row(row) or self.check_column(col)
        return False

    def sum_uncalled(self) -> int:
        count = 0
        for row_i, row in enumerate(self.called):
            for col_i, called in enumerate(row):
                if not called:
                    count += self.numbers[row_i][col_i]
        return count


def fill_boards(raw_input: list[str]) -> list[Board]:
    boards = []
    for i in range(0, len(raw_input), 6):
        board_input = raw_input[i + 1:i + 6]
        board_numbers = [[int(num) for num in row.split() if num] for row in board_input]
        boards.append(Board(board_numbers))
    return boards
