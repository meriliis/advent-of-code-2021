import os
import argparse
from datetime import datetime

from solutions.utils.print_answers import print_answers

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('day', type=int)
    parser.add_argument('-p', '--part', default=None, type=str)
    args = parser.parse_args()

    aoc_year = int(os.environ.get("YEAR"))

    if args.day:
        print_answers(day=args.day, year=aoc_year, part=args.part)
    else:
        current_time = datetime.now()
        for date in range(1, 32):
            time = datetime(aoc_year, 12, date, 7)  # Puzzles open at 7AM
            if current_time >= time:
                print_answers(day=time.day, year=2020)
