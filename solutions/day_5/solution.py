from typing import List, Tuple, Dict
from collections import Counter

Coordinate = Tuple[int, int]
Vent = Tuple[Coordinate, Coordinate]


def read_hydrothermal_vents(data: str) -> List[Vent]:
    hydrothermal_vents = []

    for vent in data.split('\n'):
        coordinates = vent.split(' -> ')
        vent_start = tuple(int(c) for c in coordinates[0].split(','))
        vent_end = tuple(int(c) for c in coordinates[1].split(','))
        hydrothermal_vents.append((vent_start, vent_end))

    return hydrothermal_vents


def is_horizontal(hydrothermal_vent: Vent) -> bool:
    (_, y1), (_, y2) = hydrothermal_vent
    if y1 == y2:
        return True

    return False


def is_vertical(hydrothermal_vent: Vent) -> bool:
    (x1, _), (x2, _) = hydrothermal_vent
    if x1 == x2:
        return True

    return False


def get_horizontal_and_vertical_vents(hydrothermal_vents: List[Vent]) -> List[Vent]:
    horizontal_and_vertical_vents = [vent for vent in hydrothermal_vents if is_horizontal(vent) or is_vertical(vent)]

    return horizontal_and_vertical_vents


def get_step_direction(x1: int, x2: int) -> int:
    if x1 < x2:
        dx = 1
    elif x1 > x2:
        dx = -1
    else:
        dx = 0

    return dx


def get_coordinates(hydrothermal_vent: Vent) -> List[Coordinate]:
    (x1, y1), (x2, y2) = hydrothermal_vent
    dx = get_step_direction(x1, x2)
    dy = get_step_direction(y1, y2)
    n_steps = max(abs(x2 - x1), abs(y2 - y1))
    coordinates = [(x1 + i * dx, y1 + i * dy) for i in range(n_steps + 1)]

    return coordinates


def count_vents_per_coordinate(hydrothermal_vents: List[Vent]) -> Dict[Coordinate, int]:
    vent_counts = Counter()

    for vent in hydrothermal_vents:
        vent_coordinates = get_coordinates(vent)
        vent_counts.update(vent_coordinates)

    return vent_counts


def get_coordinates_with_multiple_vents(vents_per_coordinate: Dict[Coordinate, int]):
    coordinates_with_multiple_vents = [coordinates for coordinates, vent_count in vents_per_coordinate.items()
                                       if vent_count > 1]

    return coordinates_with_multiple_vents


def get_part_1_answer(data: str) -> int:
    hydrothermal_vents = read_hydrothermal_vents(data)
    horizontal_and_vertical_vents = get_horizontal_and_vertical_vents(hydrothermal_vents)
    vents_per_coordinate = count_vents_per_coordinate(horizontal_and_vertical_vents)
    coordinates_with_multiple_vents = get_coordinates_with_multiple_vents(vents_per_coordinate)

    return len(coordinates_with_multiple_vents)


def get_part_2_answer(data: str) -> int:
    hydrothermal_vents = read_hydrothermal_vents(data)
    vents_per_coordinate = count_vents_per_coordinate(hydrothermal_vents)
    coordinates_with_multiple_vents = get_coordinates_with_multiple_vents(vents_per_coordinate)

    return len(coordinates_with_multiple_vents)
