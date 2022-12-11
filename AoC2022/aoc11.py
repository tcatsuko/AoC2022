import re
import math

rounds = 20

f = open('aoc11.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
monkeys = []
current_monkey = {}
current_monkey['items'] = []

# Build monkey list for part 1
for line in raw_input:
    if line == '':
        continue
    split_line = line.split(' ')
    if split_line[0] == 'Monkey':
        monkeys += [current_monkey]
        current_monkey = {}
        current_monkey['items'] = []
        current_monkey['inspections'] = 0
    elif split_line[2] == 'Starting':
        for x in split_line[4:]: 
            item_worry = re.findall(r'\d+', x)
            current_monkey['items'] += [int(item_worry[0])]
    elif split_line[2] == 'Operation:':
        current_monkey['operation'] = split_line[5] + ' ' + split_line[6] + ' ' + split_line[7]
    elif split_line[2] == 'Test:':
        current_monkey['test'] = int(split_line[5])
    elif split_line[4] == 'If':
        if split_line[5] == 'true:':
            current_monkey['true'] = int(split_line[9])
        else:
            current_monkey['false'] = int(split_line[9])
monkeys += [current_monkey]
monkeys.pop(0) # housekeeping, the first one is empty based on how I have things coded up

# Using least common multiple to make things managable, absolutely necessary for part 2
lcm = math.lcm(*[monkey['test'] for monkey in monkeys])

# Now, loop
for x in range(rounds):
    for monkey in monkeys:
        for item in monkey['items']:
            # parse the operation
            monkey['inspections'] += 1
            split_operation = monkey['operation'].split(' ')
            if split_operation[0] == 'old':
                op1 = int(item)
            else:
                op1 = int(split_operation[0])
            if split_operation[2] == 'old':
                op2 = int(item)
            else:
                op2 = int(split_operation[2])
            if split_operation[1] == '*':
                worry = ((op1 ) * (op2 ) ) % lcm
            elif split_operation[1] == '+':
                worry = ((op1 ) + (op2 )) % lcm
            # inspection done.  Monkey bored
            worry = int(worry / 3)
            # Now do the test
            if worry % monkey['test'] == 0:
                true_monkey = monkey['true']
                monkeys[true_monkey]['items'] += [worry]
            else:
                false_monkey = monkey['false']
                monkeys[false_monkey]['items'] += [worry]
        monkey['items'] = []
    print()
                
# Sort monkeys by inspections
sorted_monkey_list = sorted(monkeys, key = lambda d: d['inspections'], reverse=True)
monkey_business = sorted_monkey_list[0]['inspections'] * sorted_monkey_list[1]['inspections']
print('Part 1: after 20 rounds the monkey business is ' + str(monkey_business))

# Part 2
rounds = 10000
monkeys = []
current_monkey = {}
current_monkey['items'] = []

#rebuild initial monkey list
for line in raw_input:
    if line == '':
        continue
    split_line = line.split(' ')
    if split_line[0] == 'Monkey':
        monkeys += [current_monkey]
        current_monkey = {}
        current_monkey['items'] = []
        current_monkey['inspections'] = 0
    elif split_line[2] == 'Starting':
        for x in split_line[4:]: 
            item_worry = re.findall(r'\d+', x)
            current_monkey['items'] += [int(item_worry[0])]
    elif split_line[2] == 'Operation:':
        current_monkey['operation'] = split_line[5] + ' ' + split_line[6] + ' ' + split_line[7]
    elif split_line[2] == 'Test:':
        current_monkey['test'] = int(split_line[5])
    elif split_line[4] == 'If':
        if split_line[5] == 'true:':
            current_monkey['true'] = int(split_line[9])
        else:
            current_monkey['false'] = int(split_line[9])
monkeys += [current_monkey]
monkeys.pop(0) # housekeeping, the first one is empty based on how I have things coded up

# Now, loop
for x in range(rounds):
    for monkey in monkeys:
        for item in monkey['items']:
            # parse the operation
            monkey['inspections'] += 1
            split_operation = monkey['operation'].split(' ')
            if split_operation[0] == 'old':
                op1 = int(item)
            else:
                op1 = int(split_operation[0])
            if split_operation[2] == 'old':
                op2 = int(item)
            else:
                op2 = int(split_operation[2])
            if split_operation[1] == '*':
                worry = (op1 * op2) % lcm
            elif split_operation[1] == '+':
                worry = (op1 + op2) % lcm
            # Now do the test
            if worry % monkey['test'] == 0:
                true_monkey = monkey['true']
                monkeys[true_monkey]['items'] += [worry]
            else:
                false_monkey = monkey['false']
                monkeys[false_monkey]['items'] += [worry]
        monkey['items'] = []

# Sort monkeys by inspections
sorted_monkey_list = sorted(monkeys, key = lambda d: d['inspections'], reverse=True)
monkey_business = sorted_monkey_list[0]['inspections'] * sorted_monkey_list[1]['inspections']
print('Part 2: after 10000 rounds the monkey business is ' + str(monkey_business))
