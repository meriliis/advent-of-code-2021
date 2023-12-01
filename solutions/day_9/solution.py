from typing import List, Set, Tuple
from functools import reduce
import numpy as np


def read_heightmap(data: str) -> np.array:
    heightmap = np.asarray([[int(height) for height in row] for row in data.split('\n')])

    return heightmap


def get_low_points_mask(heightmap: np.array) -> np.array:
    heightmap_padded = np.pad(heightmap, pad_width=1, mode='maximum')
    low_points_mask = (
        (heightmap < heightmap_padded[1:-1, :-2]) &  # left
        (heightmap < heightmap_padded[1:-1, 2:]) &  # right
        (heightmap < heightmap_padded[:-2, 1:-1]) &  # up
        (heightmap < heightmap_padded[2:, 1:-1])  # down
    )

    return low_points_mask


def get_basin_size(starting_point: Tuple[int, int], unexplored_basin_points: np.array) -> Tuple[int, np.array]:
    x, y = starting_point

    if not unexplored_basin_points[x, y]:
        # Already explored or not a basin point
        return 0, unexplored_basin_points

    # Not explored basin point, mark as explored
    unexplored_basin_points[x, y] = False

    # Scan left, right, up, down neighbors
    left_size, unexplored_basin_points = get_basin_size((x, y - 1), unexplored_basin_points)
    right_size, unexplored_basin_points = get_basin_size((x, y + 1), unexplored_basin_points)
    up_size, unexplored_basin_points = get_basin_size((x - 1, y), unexplored_basin_points)
    down_size, unexplored_basin_points = get_basin_size((x + 1, y), unexplored_basin_points)

    return 1 + left_size + right_size + up_size + down_size, unexplored_basin_points


def get_basin_sizes(heightmap: np.array) -> List[int]:
    heightmap_padded = np.pad(heightmap, pad_width=1, mode='maximum')
    unexplored_basin_points = heightmap_padded != heightmap.max()
    basin_sizes = []

    while unexplored_basin_points.any():
        first_unexplored_basin_point = list(zip(*np.where(unexplored_basin_points)))[0]
        basin_size, unexplored_basin_points = get_basin_size(first_unexplored_basin_point, unexplored_basin_points)
        basin_sizes.append(basin_size)

    return basin_sizes


def get_part_1_answer(data: str) -> int:
    heightmap = read_heightmap(data)
    low_points_mask = get_low_points_mask(heightmap)
    low_points = heightmap[low_points_mask]
    low_points_risk_levels = low_points + 1
    total_risk_level = sum(low_points_risk_levels)

    return total_risk_level


def get_part_2_answer(data: str) -> int:
    heightmap = read_heightmap(data)
    basin_sizes = get_basin_sizes(heightmap)
    top_3_basin_sizes = sorted(basin_sizes)[-3:]

    return reduce(lambda x, y: x * y, top_3_basin_sizes)
