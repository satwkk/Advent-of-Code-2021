import sys

with open(sys.argv[1], 'r') as input:
    numbers = input.readlines()
numbers = [int(i.strip('\r').strip('\n')) for i in numbers]

# Part 1
def part1():
    count = 0
    prev = numbers[0]
    for n in numbers[1:]:
        if n > prev:
            count += 1
        prev = n
    return count

# Part 2
def part2():
    count = 0
    for i in range(len(numbers)):
        if sum(numbers[i:i+3]) < sum(numbers[i+1:i+4]):
            count += 1
    return count

if __name__ == '__main__':
    # run the func here
    print(f'Part1: {part1()}')
    print(f'Part2: {part2()}')
