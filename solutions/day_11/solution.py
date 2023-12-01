from typing import Tuple
import numpy as np


def read_octopus_energy_levels(data: str) -> np.array:
    octopus_energy_levels = np.asarray([[int(level) for level in line] for line in data.split('\n')])

    return octopus_energy_levels


def simulate_step(octopus_energy_levels: np.array) -> Tuple[np.array, int, bool]:
    def count_flashing_neighbors(flashing_octopuses: np.array) -> np.array:
        n_rows, n_columns = flashing_octopuses.shape
        flashing_octopuses_padded = np.pad(flashing_octopuses, pad_width=1, constant_values=False)
        flashing_neighbors_count = np.zeros_like(flashing_octopuses_padded, dtype=np.int)

        for i in range(1, n_rows + 1):
            for j in range(1, n_columns + 1):
                flashing_neighbors_count[i, j] = flashing_octopuses_padded[i-1 : i+2, j-1 : j+2].sum()
                if flashing_octopuses_padded[i, j]:
                    flashing_neighbors_count[i, j] -= 1

        return flashing_neighbors_count[1:-1, 1:-1]

    octopus_energy_levels += 1
    current_flashing_octopuses = octopus_energy_levels > 9
    current_flashing_neighbors_count = count_flashing_neighbors(current_flashing_octopuses)
    has_flashed_in_this_step = np.zeros_like(current_flashing_neighbors_count).astype(bool)

    while current_flashing_octopuses.any():
        octopus_energy_levels[current_flashing_octopuses] = 0
        has_flashed_in_this_step = has_flashed_in_this_step | current_flashing_octopuses
        octopus_energy_levels += current_flashing_neighbors_count * ~has_flashed_in_this_step
        current_flashing_octopuses = octopus_energy_levels > 9
        current_flashing_neighbors_count = count_flashing_neighbors(current_flashing_octopuses)

    octopus_energy_levels[has_flashed_in_this_step] = 0
    total_flashes = has_flashed_in_this_step.sum()
    everyone_flashed = has_flashed_in_this_step.all()

    return octopus_energy_levels, total_flashes, everyone_flashed


def get_part_1_answer(data: str) -> int:
    octopus_energy_levels = read_octopus_energy_levels(data)
    n_steps = 100
    total_flashes = 0
    for _ in range(n_steps):
        octopus_energy_levels, flashes_in_step, _ = simulate_step(octopus_energy_levels)
        total_flashes += flashes_in_step

    return total_flashes


def get_part_2_answer(data: str) -> int:
    octopus_energy_levels = read_octopus_energy_levels(data)

    step_idx = 1
    while True:
        octopus_energy_levels, _, everyone_flashed = simulate_step(octopus_energy_levels)
        if everyone_flashed:
            return step_idx

        step_idx += 1
