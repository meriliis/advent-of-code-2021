from typing import List, Dict
from collections import Counter


def read_lanternfish(data: str) -> List[int]:
    lanternfish = [int(timer) for timer in data.split(',')]

    return lanternfish


def get_lanternfish_counts(lanternfish: List[int]) -> Dict[int, int]:
    lanternfish_counts = Counter(lanternfish)

    return lanternfish_counts


def simulate_one_day(lanternfish_counts: Dict[int, int]) -> Dict[int, int]:
    lanternfish_counts_new = Counter()

    for timer_value in range(1, 9):
        lanternfish_counts_new[timer_value - 1] = lanternfish_counts[timer_value]

    # timer 0 creates a new lanternfish and resets the timer
    lanternfish_counts_new[8] = lanternfish_counts[0]
    lanternfish_counts_new[6] += lanternfish_counts[0]

    return lanternfish_counts_new


def simulate_lanternfish(lanternfish_counts: Dict[int, int], n_days: int) -> Dict[int, int]:
    for _ in range(n_days):
        lanternfish_counts = simulate_one_day(lanternfish_counts)

    return lanternfish_counts


def count_lanternfish(lanternfish_counts: Dict[int, int]) -> int:
    lanternfish_count = sum(lanternfish_counts.values())

    return lanternfish_count


def get_part_1_answer(data: str) -> int:
    n_days = 80
    lanternfish = read_lanternfish(data)
    initial_lanternfish_counts = get_lanternfish_counts(lanternfish)
    final_lanternfish_counts = simulate_lanternfish(initial_lanternfish_counts, n_days=n_days)
    final_lanternfish_total_count = count_lanternfish(final_lanternfish_counts)

    return final_lanternfish_total_count


def get_part_2_answer(data: str) -> int:
    n_days = 256
    lanternfish = read_lanternfish(data)
    initial_lanternfish_counts = get_lanternfish_counts(lanternfish)
    final_lanternfish_counts = simulate_lanternfish(initial_lanternfish_counts, n_days=n_days)
    final_lanternfish_total_count = count_lanternfish(final_lanternfish_counts)

    return final_lanternfish_total_count
