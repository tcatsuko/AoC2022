from collections import deque
filename = 'aoc20.txt'
f = open(filename,'rt')
elf_list = deque()
counter = 0
for line in f:
    num_string = line[:-1]
    elf_list.append((counter, int(num_string)))
    counter += 1
f.close()
original_order = list(elf_list.copy())
list_length = len(original_order)

for item in original_order:
    if item[1] == 0:
        zero_index = item[0]
        continue
    item_index = elf_list.index(item)
    elf_list.rotate(-1 * item_index)
    original_list = list(elf_list.copy())
    number_to_move = elf_list.popleft()
    if number_to_move != item:
        print()
    #determine direction 
    direction = -1 if number_to_move[1] > 0 else 1
    original_sign = -1 if number_to_move[1] < 0 else 1
    spaces_to_move = abs(number_to_move[1]) % len(elf_list)

    elf_list.rotate(-1 * original_sign * spaces_to_move)

    elf_list.appendleft(number_to_move)
# All moves made
#Now find the interested numbers
target_numbers = []

elf_zero_index = elf_list.index((zero_index, 0))
elf_list.rotate(-1 * elf_zero_index)


for x in range(1,4):
    target_location = (1000 * x) 
    elf_list.rotate(-1000)
    target_numbers += [elf_list[0][1]]
grove_sum = sum(target_numbers)

print('Part 1: grove sum is ' + str(grove_sum))

key = 811589153
keyed_list = []
f = open(filename,'rt')
elf_list = deque()
counter = 0
for line in f:
    num_string = line[:-1]
    elf_list.append((counter, int(num_string) * key))
    counter += 1
f.close()
keyed_list = list(elf_list.copy())

for round in range(10):
    for item in keyed_list:
        if item[1] == 0:
            zero_index = item[0]
            continue
        item_index = elf_list.index(item)
        elf_list.rotate(-1 * item_index)
        
        number_to_move = elf_list.popleft()
        #determine direction 
        direction = -1 if number_to_move[1] > 0 else 1
        original_sign = -1 if number_to_move[1] < 0 else 1
        spaces_to_move = abs(number_to_move[1]) % len(elf_list)

        elf_list.rotate(-1 * original_sign * spaces_to_move)

        elf_list.appendleft(number_to_move)
target_numbers = []

elf_zero_index = elf_list.index((zero_index, 0))
elf_list.rotate(-1 * elf_zero_index)


for x in range(1,4):
    target_location = (1000 * x) 
    elf_list.rotate(-1000)
    target_numbers += [elf_list[0][1]]
grove_sum = sum(target_numbers)

print('Part 2: grove sum is ' + str(grove_sum))