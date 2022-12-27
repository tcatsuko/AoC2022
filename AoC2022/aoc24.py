from math import lcm
from collections import deque
f = open('aoc24.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Determine start
start_pos = (raw_input[0].find('.'), 0)
end_pos = (raw_input[-1].find('.'), len(raw_input) - 1)
print()
# build the border
border = []
for y in range(len(raw_input)):
    border += [(0, y)]
    border += [(len(raw_input[0]) - 1, y)]
for x in range(1,len(raw_input[0]) - 1):
    if x != start_pos[0]:
        border += [(x, 0)]
border += [(start_pos[0], -1)]
border += [(end_pos[0], end_pos[1] + 1)]
for x in range(1,len(raw_input[0]) - 1):
    if x != end_pos[0]:
        border += [(x, len(raw_input)-1)]
# Find the playable board length and width
width = len(raw_input[0]) - 2
length = len(raw_input) - 2
blizz_cycle = lcm(length, width)
# build the cycles
blizzards = []
# build the initial state
current_blizzard = {}
blizzard_points = []
counter = 0
for y, line in enumerate(raw_input):
    for x , position in enumerate(line):
        if (position == '>') or (position == '<') or (position == '^') or (position == 'v'):
            # It's a blizzard
            blizzard_points += [{'pos': [x,y], 'direction': position}]
            current_blizzard[(x,y)] = 0
blizzards += [current_blizzard]
for time in range(1,blizz_cycle):
    current_blizzard = {}
    for storm in blizzard_points:
        if storm['direction'] == '>':
            new_pos = [storm['pos'][0] + 1, storm['pos'][1]]
            if new_pos[0] == len(raw_input[0]) - 1:
                new_pos[0] = 1
            
        elif storm['direction'] == '<':
            new_pos = [storm['pos'][0] - 1, storm['pos'][1]]
            if new_pos[0] == 0:
                new_pos[0] = len(raw_input[0]) - 2
            
        elif storm['direction'] == '^':
            new_pos = [storm['pos'][0], storm['pos'][1] - 1]
            if new_pos[1] == 0:
                new_pos[1] = len(raw_input) - 2
            
        elif storm['direction'] == 'v':
            new_pos = [storm['pos'][0], storm['pos'][1] + 1]
            if new_pos[1] == len(raw_input) - 1:
                new_pos[1] = 1
        storm['pos'] = new_pos
        current_blizzard[tuple(new_pos)] = 0
    blizzards += [current_blizzard]
visited_points = set()
points_to_visit = []
time = 0
current_point = (start_pos[0], start_pos[1], 0)
start_time = -1
possible_offsets = [[0,0], [1,0], [-1,0], [0,1], [0,-1]]
def maze_time(start_pos, end_pos, start_time):
    global border
    global blizzards
    visited_points = set()
    points_to_visit = []

    current_point = (start_pos[0], start_pos[1], 0)

    possible_offsets = [[0,0], [1,0], [-1,0], [0,1], [0,-1]]
    while True:
        while len(points_to_visit) == 0:
            start_time += 1
            if (current_point[0], current_point[1]) not in blizzards[start_time % blizz_cycle]:
                points_to_visit += [(current_point[0], current_point[1], start_time)]
        x, y, time = points_to_visit.pop(0)
        if (x, y, time) in visited_points:
            continue
        visited_points.add((x, y, time))
        if (x, y) == end_pos:
            end_time = time
            return end_time
        for offset_x, offset_y in possible_offsets:
            next_x = x + offset_x
            next_y = y + offset_y
            if ((next_x, next_y) not in border) and (next_x, next_y) not in blizzards[(time + 1) % blizz_cycle]:
                points_to_visit += [(next_x, next_y, time + 1)]
end_time_1 = maze_time(start_pos, end_pos, -1)
print('Part 1: it took ' + str(end_time_1) + ' minutes to traverse the maze.')
return_time = maze_time(end_pos, start_pos, end_time_1)
second_try = maze_time(start_pos, end_pos, return_time)
print('Part 2: it took ' + str(second_try) + ' minutes to go to the end, go back, and go back again')


