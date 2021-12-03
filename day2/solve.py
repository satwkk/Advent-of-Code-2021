#!/usr/bin/env python3
import sys
import argparse

class Day2:
    def __init__(self, input_file):
        self.input_file = input_file

    def parse_input(self) -> list:
        with open(self.input_file, 'r') as f:
            return f.readlines()

    def part1(self) -> int:
        horizontal, depth = 0, 0
        for cmd in self.parse_input():
            direction, quantity = cmd.strip().split(' ')
            quantity = int(quantity)
            if direction.lower() == 'forward':
                horizontal += quantity
            elif direction.lower() == 'down':
                depth += quantity
            elif direction.lower() == 'up':
                depth -= quantity
        return horizontal * depth

    def part2(self) -> int:
        horizontal, depth, aim = 0, 0, 0
        for cmd in self.parse_input():
            direction, quantity = cmd.strip().split(' ')
            quantity = int(quantity)
            if direction.lower() == 'forward':
                horizontal += quantity
                depth += (aim * quantity)
            elif direction.lower() == 'down':
                aim += quantity
            elif direction.lower() == 'up':
                aim -= quantity
        return horizontal * depth


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of code solver')
    parser.add_argument('filename', help='Input filenmae')
    args = parser.parse_args()
    if args.filename is None:
        parser.print_help(sys.stderr)

    day2 = Day2(args.filename)
    print(f'Part1 Solution: {day2.part1()}')
    print(f'Part2 Solution: {day2.part2()}')

