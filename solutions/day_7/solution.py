from typing import List, Tuple


def read_crab_positions(data: str) -> List[int]:
    crab_positions = [int(pos) for pos in data.split(',')]

    return crab_positions


def find_optimal_alignment_position_at_constant_fuel_consumption(crab_positions: List[int]) -> int:
    sorted_positions = sorted(crab_positions)
    n_crabs = len(crab_positions)

    if n_crabs % 2 == 1:
        median_position = sorted_positions[int(n_crabs / 2)]
    else:
        median_position = (sorted_positions[int(n_crabs / 2) - 1] + sorted_positions[int(n_crabs / 2)]) / 2

    return median_position


def calculate_total_fuel_consumption_at_constant_fuel_consumption(crab_positions: List[int], final_position: int) -> int:
    distances = [abs(final_position - pos) for pos in crab_positions]
    total_fuel_consumption = sum(distances)

    return total_fuel_consumption


def calculate_total_fuel_consumption_at_linear_fuel_consumption(crab_positions: List[int], final_position: int) -> int:
    total_fuel_consumption = 0

    for pos in crab_positions:
        distance = abs(final_position - pos)
        fuel_consumption = distance * (distance + 1) / 2  # sum of n consecutive numbers is n(n+1)/2
        total_fuel_consumption += fuel_consumption

    return total_fuel_consumption


def find_optimal_alignment_position_at_linear_fuel_consumption(crab_positions: List[int]) -> Tuple[int, int]:
    current_position = find_optimal_alignment_position_at_constant_fuel_consumption(crab_positions)
    current_fuel_consumption = calculate_total_fuel_consumption_at_linear_fuel_consumption(
        crab_positions,
        current_position
    )

    fuel_consumption_to_current_minus_one = calculate_total_fuel_consumption_at_linear_fuel_consumption(
        crab_positions,
        current_position - 1
    )

    fuel_consumption_to_current_plus_one = calculate_total_fuel_consumption_at_linear_fuel_consumption(
        crab_positions,
        current_position + 1
    )

    if (fuel_consumption_to_current_plus_one > current_fuel_consumption) & \
            (fuel_consumption_to_current_minus_one > current_fuel_consumption):
        # Fuel consumption at both neighboring positions bigger than starting position, already the best position
        optimal_alignment_position = current_position
        total_fuel_consumption = current_fuel_consumption
    else:
        # Go towards smaller values
        if fuel_consumption_to_current_plus_one < fuel_consumption_to_current_minus_one:
            step_size = 1
        else:
            step_size = -1

        next_position = current_position + step_size
        next_fuel_consumption = calculate_total_fuel_consumption_at_linear_fuel_consumption(
            crab_positions,
            next_position
        )

        while next_fuel_consumption < current_fuel_consumption:
            current_position = next_position
            current_fuel_consumption = next_fuel_consumption
            next_position = current_position + step_size
            next_fuel_consumption = calculate_total_fuel_consumption_at_linear_fuel_consumption(
                crab_positions,
                next_position
            )

        optimal_alignment_position = current_position
        total_fuel_consumption = current_fuel_consumption

    return optimal_alignment_position, total_fuel_consumption


def get_part_1_answer(data: str) -> int:
    crab_positions = read_crab_positions(data)
    optimal_alignment_position = find_optimal_alignment_position_at_constant_fuel_consumption(crab_positions)
    total_fuel_consumption = calculate_total_fuel_consumption_at_constant_fuel_consumption(
        crab_positions,
        optimal_alignment_position
    )

    return total_fuel_consumption


def get_part_2_answer(data: str) -> int:
    crab_positions = read_crab_positions(data)
    optimal_alignment_position, total_fuel_consumption = find_optimal_alignment_position_at_linear_fuel_consumption(
        crab_positions
    )

    return total_fuel_consumption
