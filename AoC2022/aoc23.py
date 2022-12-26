from collections import deque
import math

f = open('aoc23.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
elf_pos = {}
for y, line in enumerate(raw_input):
    for x, elf in enumerate(line):
        if elf == '#':
            elf_pos[(x, y)] = []
search_dir = deque(['n', 's', 'w', 'e'])
original_elf_pos = elf_pos

for round in range(10):
    proposed_moves = {}
    destinations = {}
    for elf in elf_pos:
        current_x = elf[0]
        current_y = elf[1]
        n = (current_x, current_y - 1)
        ne = (current_x + 1, current_y - 1)
        e = (current_x + 1,current_y)
        se = (current_x + 1, current_y + 1)
        s = (current_x, current_y + 1)
        sw = (current_x - 1, current_y + 1)
        w = (current_x - 1, current_y)
        nw = (current_x - 1, current_y - 1)
        if (n in elf_pos) or (ne in elf_pos) or (e in elf_pos) or (se in elf_pos) or (s in elf_pos) or (sw in elf_pos) or (w in elf_pos) or (nw in elf_pos):
            # need to move
            for direction in range(len(search_dir)):
                if search_dir[direction] == 'n':
                    if (n not in elf_pos) and (ne not in elf_pos) and (nw not in elf_pos):
                        destinations[elf] = n
                        if n not in proposed_moves:
                            proposed_moves[n] = [elf]
                        else:
                            proposed_moves[n] += [elf]
                        break
                elif search_dir[direction] == 's':
                    if (s not in elf_pos) and (se not in elf_pos) and (sw not in elf_pos):
                        destinations[elf] = s
                        if s not in proposed_moves:
                            proposed_moves[s] = [elf]
                        else:
                            proposed_moves[s] += [elf]
                        break
                elif search_dir[direction] == 'e':
                    if (e not in elf_pos) and (ne not in elf_pos) and (se not in elf_pos):
                        destinations[elf] = e
                        if e not in proposed_moves:
                            proposed_moves[e] = [elf]
                        else:
                            proposed_moves[e] += [elf]
                        break
                elif search_dir[direction] == 'w':
                    if (w not in elf_pos) and (nw not in elf_pos) and (sw not in elf_pos):
                        destinations[elf] = w
                        if w not in proposed_moves:
                            proposed_moves[w] = [elf]
                        else:
                            proposed_moves[w] += [elf]
                        break
        if elf not in destinations:
            destinations[elf] = elf
            if elf not in proposed_moves:
                proposed_moves[elf] = elf
            else:
                proposed_moves[elf] += [elf]
    # Done proposing moves, now make the moves
    new_destinations = {}
    for elf in destinations:
        move_to = destinations[elf]
        if move_to == elf:
            new_destinations[move_to] = []
        else:
            if len(proposed_moves[move_to]) > 1:
                new_destinations[elf] = []
            else:
                new_destinations[move_to] = []
    elf_pos = new_destinations
    search_dir.rotate(-1)
# Now need to find the area
min_x = math.inf
max_x = -1 * math.inf
min_y = math.inf
max_y = -1 * math.inf
for elf in elf_pos:
    if elf[0] < min_x:
        min_x = elf[0]
    if elf[0] > max_x:
        max_x = elf[0]
    if elf[1] < min_y:
        min_y = elf[1]
    if elf[1] > max_y:
        max_y = elf[1]
length = (max_y - min_y) + 1
width = (max_x - min_x) + 1
area = length * width
empty = area - len(elf_pos)
print('Part 1: empty space is ' + str(empty))

round = 0
elf_pos = original_elf_pos
search_dir = deque(['n', 's', 'w', 'e'])
while True:
    round += 1
    need_to_move = False
    proposed_moves = {}
    destinations = {}
    for elf in elf_pos:
        current_x = elf[0]
        current_y = elf[1]
        n = (current_x, current_y - 1)
        ne = (current_x + 1, current_y - 1)
        e = (current_x + 1,current_y)
        se = (current_x + 1, current_y + 1)
        s = (current_x, current_y + 1)
        sw = (current_x - 1, current_y + 1)
        w = (current_x - 1, current_y)
        nw = (current_x - 1, current_y - 1)
        if (n in elf_pos) or (ne in elf_pos) or (e in elf_pos) or (se in elf_pos) or (s in elf_pos) or (sw in elf_pos) or (w in elf_pos) or (nw in elf_pos):
            # need to move
            need_to_move = True
            for direction in range(len(search_dir)):
                if search_dir[direction] == 'n':
                    if (n not in elf_pos) and (ne not in elf_pos) and (nw not in elf_pos):
                        destinations[elf] = n
                        if n not in proposed_moves:
                            proposed_moves[n] = [elf]
                        else:
                            proposed_moves[n] += [elf]
                        break
                elif search_dir[direction] == 's':
                    if (s not in elf_pos) and (se not in elf_pos) and (sw not in elf_pos):
                        destinations[elf] = s
                        if s not in proposed_moves:
                            proposed_moves[s] = [elf]
                        else:
                            proposed_moves[s] += [elf]
                        break
                elif search_dir[direction] == 'e':
                    if (e not in elf_pos) and (ne not in elf_pos) and (se not in elf_pos):
                        destinations[elf] = e
                        if e not in proposed_moves:
                            proposed_moves[e] = [elf]
                        else:
                            proposed_moves[e] += [elf]
                        break
                elif search_dir[direction] == 'w':
                    if (w not in elf_pos) and (nw not in elf_pos) and (sw not in elf_pos):
                        destinations[elf] = w
                        if w not in proposed_moves:
                            proposed_moves[w] = [elf]
                        else:
                            proposed_moves[w] += [elf]
                        break
        if elf not in destinations:
            destinations[elf] = elf
            if elf not in proposed_moves:
                proposed_moves[elf] = elf
            else:
                proposed_moves[elf] += [elf]
    # Done proposing moves, now make the moves
    new_destinations = {}
    for elf in destinations:
        move_to = destinations[elf]
        if move_to == elf:
            new_destinations[move_to] = []
        else:
            if len(proposed_moves[move_to]) > 1:
                new_destinations[elf] = []
            else:
                new_destinations[move_to] = []
    elf_pos = new_destinations
    search_dir.rotate(-1)
    if need_to_move == False:
        break
print('Part 2: it took ' + str(round) + ' rounds to reach steady state.')
# 989 too high
#988 wrong

