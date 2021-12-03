from typing import List, Tuple


def read_moving_commands(data: str) -> List[Tuple[str, int]]:
    moving_commands = []

    for command in data.split('\n'):
        direction, amount = command.split(' ')
        moving_commands.append((direction, int(amount)))

    return moving_commands


def execute_command_a(horizontal_position: int, depth: int, command: Tuple[str, int]) -> Tuple[int, int]:
    direction, amount = command

    if direction == 'forward':
        horizontal_position += amount
    elif direction == 'up':
        depth -= amount
    elif direction == 'down':
        depth += amount

    return horizontal_position, depth


def move_ship_a(horizontal_position: int, depth: int, commands: List[Tuple[str, int]]) -> Tuple[int, int]:
    for command in commands:
        horizontal_position, depth = execute_command_a(horizontal_position, depth, command)

    return horizontal_position, depth


def execute_command_b(horizontal_position: int, depth: int, aim: int, command: Tuple[str, int]) -> Tuple[int, int, int]:
    direction, amount = command

    if direction == 'forward':
        horizontal_position += amount
        depth += aim * amount
    elif direction == 'up':
        aim -= amount
    elif direction == 'down':
        aim += amount

    return horizontal_position, depth, aim


def move_ship_b(horizontal_position: int, depth: int, aim: int, commands: List[Tuple[str, int]]) -> Tuple[int, int, int]:
    for command in commands:
        horizontal_position, depth, aim = execute_command_b(horizontal_position, depth, aim, command)

    return horizontal_position, depth, aim


def get_part_a_answer(data: str) -> int:
    moving_commands = read_moving_commands(data)
    horizontal_position, depth = move_ship_a(horizontal_position=0, depth=0, commands=moving_commands)

    return horizontal_position * depth


def get_part_b_answer(data: str) -> int:
    moving_commands = read_moving_commands(data)
    horizontal_position, depth, _ = move_ship_b(horizontal_position=0, depth=0, aim=0, commands=moving_commands)

    return horizontal_position * depth
