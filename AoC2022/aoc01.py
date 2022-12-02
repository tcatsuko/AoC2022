f = open('aoc01.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
elves = []
current_elf = []
for line in raw_input:
    if line == '':
        elves += [sum(current_elf)]
        current_elf = []
    else:
        current_elf += [int(line)]
max_calories = max(elves)
print('Part 1: max calories carried is ' + str(max_calories))
# Find the top 3
cal_sum = 0
max_index = elves.index(max(elves))
cal_sum += elves.pop(max_index)
max_index = elves.index(max(elves))
cal_sum += elves.pop(max_index)
max_index = elves.index(max(elves))
cal_sum += elves.pop(max_index)
print('Part 2: top 3 elves carry ' + str(cal_sum) + ' calories')
