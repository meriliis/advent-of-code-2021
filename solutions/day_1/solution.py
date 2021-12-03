from typing import List


def get_increase_count(sonar_sweep_report: List[int]) -> int:
    increase_count = 0

    for i in range(len(sonar_sweep_report) - 1):
        diff = sonar_sweep_report[i + 1] - sonar_sweep_report[i]
        if diff > 0:
            increase_count += 1

    return increase_count


def get_rolling_sum(arr: List[int], window_size: int) -> List[int]:
    rolling_sum = [sum(arr[i:i + window_size]) for i in range(len(arr) - window_size + 1)]

    return rolling_sum


def get_part_1_answer(data: str) -> int:
    sonar_sweep_report = [int(x) for x in data.split('\n')]
    increase_count = get_increase_count(sonar_sweep_report)

    return increase_count


def get_part_2_answer(data: str) -> int:
    sonar_sweep_report = [int(x) for x in data.split('\n')]
    sonar_sweep_report_rolling_sum = get_rolling_sum(sonar_sweep_report, window_size=3)
    increase_count = get_increase_count(sonar_sweep_report_rolling_sum)

    return increase_count
