# Parsing
with open('input.txt', 'r') as f:
    cmds = f.readlines()

# Part 1
def part1():
    horizontal, depth = 0, 0
    for cmd in cmds:
        direction, quantity = cmd.strip().split(' ')
        quantity = int(quantity)
        # Part 1
        if direction.lower() == 'forward':
            horizontal += quantity
        elif direction.lower() == 'down':
            depth += quantity
        elif direction.lower() == 'up':
            depth -= quantity

    print(horizontal * depth)
    
# Part 2
def part2():
    horizontal, depth, aim = 0, 0, 0
    for cmd in cmds:
        direction, quantity = cmd.strip().split(' ')
        quantity = int(quantity)
        # Part 1
        if direction.lower() == 'forward':
            horizontal += quantity
            depth += (aim * quantity)
        elif direction.lower() == 'down':
            aim += quantity
        elif direction.lower() == 'up':
            aim -= quantity
    print(horizontal * depth)

part2()
