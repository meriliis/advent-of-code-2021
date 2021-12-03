from typing import Tuple
import numpy as np


def read_diagnostic_report(data: str) -> np.array:
    diagnostic_report = np.array([[int(bit) for bit in line] for line in data.split('\n')])

    return diagnostic_report


def convert_to_decimal(binary_list: np.array) -> int:
    binary_str = ''.join([str(bit) for bit in binary_list])

    return int(binary_str, 2)


def get_gamma_rate(diagnostic_report: np.array) -> int:
    position_sums = diagnostic_report.sum(axis=0)
    is_one_most_common = position_sums > len(diagnostic_report) / 2
    most_common_bits = is_one_most_common.astype(int)
    gamma_rate = convert_to_decimal(most_common_bits)

    return gamma_rate


def get_epsilon_rate(diagnostic_report: np.array) -> int:
    position_sums = diagnostic_report.sum(axis=0)
    is_one_most_common = position_sums > len(diagnostic_report) / 2
    least_common_bits = (~is_one_most_common).astype(int)
    epsilon_rate = convert_to_decimal(least_common_bits)

    return epsilon_rate


def get_oxygen_generator_rating(diagnostic_report: np.array) -> int:
    current_bit_index = 0
    while len(diagnostic_report) > 1:
        most_common_bit = int(diagnostic_report[:, current_bit_index].sum() >= len(diagnostic_report) / 2)
        keep_number = diagnostic_report[:, current_bit_index] == most_common_bit
        diagnostic_report = diagnostic_report[keep_number]
        current_bit_index += 1

    oxygen_generator_rating = convert_to_decimal(diagnostic_report[0])

    return oxygen_generator_rating


def get_co2_scrubber_rating(diagnostic_report: np.array) -> int:
    current_bit_index = 0
    while len(diagnostic_report) > 1:
        least_common_bit = int(~(diagnostic_report[:, current_bit_index].sum() >= len(diagnostic_report) / 2))
        keep_number = diagnostic_report[:, current_bit_index] == least_common_bit
        diagnostic_report = diagnostic_report[keep_number]
        current_bit_index += 1

    co2_scrubber_rating = convert_to_decimal(diagnostic_report[0])

    return co2_scrubber_rating


def get_part_a_answer(data: str) -> int:
    diagnostic_report = read_diagnostic_report(data)
    gamma_rate = get_gamma_rate(diagnostic_report)
    epsilon_rate = get_epsilon_rate(diagnostic_report)
    power_consumption = gamma_rate * epsilon_rate

    return power_consumption


def get_part_b_answer(data: str) -> int:
    diagnostic_report = read_diagnostic_report(data)
    oxygen_generator_rating = get_oxygen_generator_rating(diagnostic_report)
    co2_scrubber_rating = get_co2_scrubber_rating(diagnostic_report)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    return life_support_rating
