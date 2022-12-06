import re
filename = 'aoc05.txt'

f = open(filename,'rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Get number of stacks
num_of_stacks = int((len(raw_input[0]) + 1) / 4)
row_counter = 0
stacks = {}
for x in range(num_of_stacks):
    stacks[str(x + 1)] = []
for line in raw_input:
    if '[' in line:
        for x in range(num_of_stacks):
            current_char = line[(x * 4) + 1]
            if current_char != ' ':
                stacks[str(x + 1)].insert(0, current_char)
        row_counter += 1
    else:
        break
print()
top_crates = ''
begin_instructions = row_counter + 2
for line in raw_input[begin_instructions:]:
    moves = re.findall(r'\d+', line)
    from_stack = stacks[moves[1]]
    to_stack = stacks[moves[2]]
    number = int(moves[0])
    for item in range(number):
        to_stack += from_stack.pop(-1)
top_crates = ''
for x in range(len(stacks)):
    index = str(x + 1)
    top_crates += stacks[index][-1]
print('Part 1: the top crates are ' + top_crates)


# Part 2
f = open(filename,'rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Get number of stacks
num_of_stacks = int((len(raw_input[0]) + 1) / 4)
row_counter = 0
stacks = {}
for x in range(num_of_stacks):
    stacks[str(x + 1)] = []
for line in raw_input:
    if '[' in line:
        for x in range(num_of_stacks):
            current_char = line[(x * 4) + 1]
            if current_char != ' ':
                stacks[str(x + 1)].insert(0, current_char)
        row_counter += 1
    else:
        break
print()
top_crates = ''
begin_instructions = row_counter + 2
for line in raw_input[begin_instructions:]:
    moves = re.findall(r'\d+',line)
    from_stack= stacks[moves[1]]
    to_stack = stacks[moves[2]]
    number = int(moves[0])
    temp_stack = []
    for item in range(number):
        temp_stack += from_stack.pop(-1)
    temp_stack.reverse()
    to_stack += temp_stack
top_crates = ''
for x in range(len(stacks)):
    index = str(x + 1)
    top_crates += stacks[index][-1]
print('Part 2: the top crates are ' + top_crates)
