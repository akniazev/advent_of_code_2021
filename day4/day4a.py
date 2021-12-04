from day4.utils import Board, fill_boards

with open("input.txt") as file:
    lines: list[str] = list(map(lambda line: line.strip(), file.readlines()))


def find_winning_board(numbers_to_call: list[int], boards: list[Board]) -> tuple[Board, int]:
    for calling in numbers_to_call:
        for board in boards:
            if board.call_number(calling):
                return board, calling
    raise ValueError("no winning board")


numbers_to_call = list(map(int, lines[0].split(",")))
boards = fill_boards(lines[1:])

winning_board, winning_number = find_winning_board(numbers_to_call, boards)
print(winning_number)
print(winning_board.sum_uncalled() * winning_number)
