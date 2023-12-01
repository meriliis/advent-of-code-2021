from typing import Tuple, List
import numpy as np


def read_numbers_and_boards(data: str) -> Tuple[List[int], List[List[List[int]]]]:
    items = data.split('\n\n')
    numbers = [int(number) for number in items[0].split(',')]
    boards = np.asarray([
        [[int(number) for number in row.strip().split()] for row in board.split('\n')]
        for board in items[1:]
    ])

    return numbers, boards


def mark_number(number: int, board: np.array, marked_numbers: np.array) -> np.array:
    number_on_board = board == number
    updated_marked_numbers = marked_numbers | number_on_board

    return updated_marked_numbers


def is_winning_board(marked_numbers: np.array) -> bool:
    board_width, board_length = marked_numbers.shape
    has_full_row = (marked_numbers.sum(axis=1) == board_width).any()
    has_full_column = (marked_numbers.sum(axis=0) == board_length).any()

    if has_full_row or has_full_column:
        return True

    return False


def draw_numbers(numbers: List[int], boards: np.array) -> Tuple[int, np.array, np.array]:
    marked_boards = np.zeros_like(boards).astype(bool)

    for number in numbers:
        for board_idx, board in enumerate(boards):
            marked_numbers = mark_number(number, board, marked_boards[board_idx])
            marked_boards[board_idx] = marked_numbers
            if is_winning_board(marked_numbers):
                return number, board, marked_numbers


def find_last_winning_board(numbers: List[int], boards: np.array) -> Tuple[int, np.array, np.array]:
    marked_boards = np.zeros_like(boards).astype(bool)

    for number in numbers:
        is_winning = np.zeros(shape=len(boards)).astype(bool)

        for board_idx, board in enumerate(boards):
            marked_numbers = mark_number(number, board, marked_boards[board_idx])
            marked_boards[board_idx] = marked_numbers
            is_winning[board_idx] = is_winning_board(marked_numbers)

        if len(boards) == 1 and is_winning_board(marked_boards[0]):
            return number, boards[0], marked_boards[0]

        boards = boards[~is_winning]
        marked_boards = marked_boards[~is_winning]


def calculate_score(winning_board: np.array, marked_numbers: np.array) -> int:
    return (winning_board * ~marked_numbers).sum()


def get_part_1_answer(data: str) -> int:
    numbers, boards = read_numbers_and_boards(data)
    winning_number, winning_board, marked_numbers = draw_numbers(numbers, boards)
    score = calculate_score(winning_board, marked_numbers)
    final_score = score * winning_number

    return final_score


def get_part_2_answer(data: str) -> int:
    numbers, boards = read_numbers_and_boards(data)
    last_winning_number, last_winning_board, marked_numbers = find_last_winning_board(numbers, boards)
    score = calculate_score(last_winning_board, marked_numbers)
    final_score = score * last_winning_number

    return final_score
