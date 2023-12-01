from typing import Tuple, List

SignalPatterns = List[str]
Output = List[str]
NoteEntry = Tuple[SignalPatterns, Output]


def read_notes(data: str) -> List[NoteEntry]:
    notes = []

    for note_entry in data.split('\n'):
        signal_patterns, output = note_entry.split(' | ')
        signal_patterns_split = signal_patterns.split()
        output_split = output.split()
        notes.append((signal_patterns_split, output_split))

    return notes


def count_digits_with_unique_number_of_segments(outputs: List[Output]) -> int:
    digits_with_unique_number_of_segments = {
        1: 2,
        4: 4,
        7: 3,
        8: 7
    }

    digits_with_unique_number_of_segments_count = 0

    for output in outputs:
        for digit in output:
            if len(digit) in digits_with_unique_number_of_segments.values():
                digits_with_unique_number_of_segments_count += 1

    return digits_with_unique_number_of_segments_count


def get_part_1_answer(data: str) -> int:
    notes = read_notes(data)
    outputs = [note[1] for note in notes]
    digits_with_unique_number_of_segments_count = count_digits_with_unique_number_of_segments(outputs)

    return digits_with_unique_number_of_segments_count


def get_part_2_answer(data: str) -> int:
    data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    notes = read_notes(data)
    outputs = [note[1] for note in notes]
    digits_with_unique_number_of_segments_count = count_digits_with_unique_number_of_segments(outputs)

    return digits_with_unique_number_of_segments_count