from typing import List, Optional
import numpy as np


CHUNK_CHARACTERS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

SYNTAX_ERROR_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

LINE_COMPLETION_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def is_opening_character(character: str) -> bool:
    return character in CHUNK_CHARACTERS.keys()


def is_closing_character(character: str) -> bool:
    return character in CHUNK_CHARACTERS.values()


def read_navigation_subsystem(data: str) -> List[str]:
    navigation_subsystem = data.split('\n')

    return navigation_subsystem


def find_first_illegal_character(line: str, open_chunks: str) -> Optional[str]:
    if len(line) == 0:
        return None

    next_char = line[0]
    line = line[1:]

    if is_opening_character(next_char):
        open_chunks += next_char

    elif is_closing_character(next_char):
        if len(open_chunks) == 0:
            # Can't start a chunk with closing character
            return next_char

        last_char = open_chunks[-1]

        if next_char != CHUNK_CHARACTERS[last_char]:
            # Closing character NOT corresponding to the previous (opening) character
            return next_char
        else:
            # Closing character IS corresponding to the previous (opening) character, so the chunk is closed
            open_chunks = open_chunks[:-1]

    else:
        raise ValueError(f'{next_char} is neither an opening nor a closing character.')

    return find_first_illegal_character(line, open_chunks)


def calculate_line_syntax_error_score(line: str) -> int:
    first_illegal_character = find_first_illegal_character(line, '')
    if first_illegal_character in SYNTAX_ERROR_SCORES:
        line_syntax_error_score = SYNTAX_ERROR_SCORES[first_illegal_character]
    else:
        line_syntax_error_score = 0

    return line_syntax_error_score


def calculate_total_syntax_error_score(navigation_subsystem: List[str]) -> int:
    total_syntax_error_score = 0

    for line in navigation_subsystem:
        total_syntax_error_score += calculate_line_syntax_error_score(line)

    return total_syntax_error_score


def discard_corrupted_lines(navigation_subsystem: List[str]) -> List[str]:
    uncorrupted_lines = [line for line in navigation_subsystem if find_first_illegal_character(line, '') is None]

    return uncorrupted_lines


def get_completing_characters(line: List[str], open_chunks: str) -> str:
    if len(line) == 0:
        completing_characters = ''.join([CHUNK_CHARACTERS[character] for character in open_chunks[::-1]])
        return completing_characters

    next_char = line[0]
    line = line[1:]

    if is_opening_character(next_char):
        open_chunks += next_char

    else:
        open_chunks = open_chunks[:-1]

    return get_completing_characters(line, open_chunks)


def calculate_line_completion_score(line: str) -> int:
    line_completion_score = 0
    completing_characters = get_completing_characters(line, '')

    for character in completing_characters:
        line_completion_score *= 5
        line_completion_score += LINE_COMPLETION_SCORES[character]

    return line_completion_score


def get_part_1_answer(data: str) -> int:
    navigation_subsystem = read_navigation_subsystem(data)
    total_syntax_error_score = calculate_total_syntax_error_score(navigation_subsystem)

    return total_syntax_error_score


def get_part_2_answer(data: str) -> int:
    navigation_subsystem = read_navigation_subsystem(data)
    incomplete_lines = discard_corrupted_lines(navigation_subsystem)
    line_completion_scores = [calculate_line_completion_score(line) for line in incomplete_lines]
    middle_score = int(np.median(line_completion_scores))

    return middle_score
