from typing import List

board = []
for i in range(5):
    board.append(['O'] * 5)


def print_board(board_in: List[List[str]]) -> None:
    for row in board_in:
        print(row)


def print_board(board_in: List[List[str]]):
    for row in board_in:
        print(" ".join(row))
