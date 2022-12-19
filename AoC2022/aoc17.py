import math
f = open('aoc17.txt','rt')
instructions = ''
for line in f:
    instructions = line.strip()
f.close()
shapes = []
heights = []
heights += [0]
cycle_dictionary = {}
chamber = ['#########']
chamber_offset = 0
shapes = ['hline','cross','l','vline','box']
shape_offset = 0
wind_offset = 0
wind_repeated = False
height = 0
chamber_max_height = 0
pieces = 1000000000000
elapsed_pieces = 0
found_cycle = False
inst_length = len(instructions)
for piece_counter in range(pieces):

    # Housekeeping
    if len(chamber) > 100:
        chamber_offset += len(chamber) - 100
        for x in range(len(chamber)-100):
            chamber.pop(0)
    
    
    # spawn a new piece
    for y in range(3):
        chamber += ['#.......#']
    shape_start = len(chamber)
    for counter in range(4):
        chamber += ['#.......#']

        
    current_piece = shapes[shape_offset]
    if current_piece == 'hline':
        shape = ['...####..']
    elif current_piece == 'cross':
        shape = [
            '....#....',
            '...###...',
            '....#....']
    elif current_piece == 'l':
        shape = [
            '...###...',
            '.....#...',
            '.....#...']
    elif current_piece == 'vline':
        shape = [
            '...#.....',
            '...#.....',
            '...#.....',
            '...#.....']
    elif current_piece == 'box':
        shape = [
            '...##....',
            '...##....']
    for r in range(len(shape)):
        chamber += ['#.......#']
    can_drop = True
    while can_drop == True:
    # try to move lateral
        wind = instructions[wind_offset]
        wind_offset += 1
        if wind_offset == len(instructions):
            wind_offset = 0
            wind_repeated = True
        if wind == '>':
            # move right
            old_shape = shape[:]
            for idx, row in enumerate(shape):
                row = row[:-1]
                row = '.' + row
                shape[idx] = row
            # check boundary
            can_move = True
            for idx, row in enumerate(shape):
                occupied_shape = row.rfind('#')
                occupied_chamber = chamber[shape_start + idx][occupied_shape]
                if occupied_chamber == '#':
                    can_move = False
            if can_move == False:
                shape = old_shape
        elif wind == '<':
            # move left
            old_shape = shape[:]
            for idx, row in enumerate(shape):
                row = row[1:]
                row += '.'
                shape[idx] = row
            # check boundary
            can_move = True
            for idx, row in enumerate(shape):
                occupied_shape = row.find('#')
                if chamber[shape_start + idx][occupied_shape] == '#':
                    can_move = False
            if can_move == False:
                shape = old_shape
        # Now try to move down
        
        for idx, row in enumerate(shape):
            for c_idx, character in enumerate(row):
                if chamber[shape_start - 1 + idx][c_idx] == '#' and row[c_idx] == '#':
                    can_drop = False
        if can_drop == False:
            # Shape is at rest
            prev_chamber = chamber[:]
            for idx, row in enumerate(shape):
                current_chamber_row = ''
                for char in range(9):
                    char_to_add = '#' if (chamber[shape_start + idx][char] == '#' or row[char] == '#') else '.'
                    current_chamber_row += char_to_add
                chamber[idx + shape_start] = current_chamber_row
            # prune the empty rows
            prev_height = chamber_max_height + chamber_offset
            
            chamber_max_height = 0
            prune_height = 0
            for i,e in reversed(list(enumerate(chamber))):
                if '#' in e[1:8]:
                    chamber_max_height = i
                    prune_height = chamber_max_height + 1
                    break
            for counter in range(prune_height, len(chamber)):
                chamber.pop(-1)
            shape_offset += 1
            if shape_offset == len(shapes):
                shape_offset = 0
            cycle_key = (shape_offset, wind_offset)
            heights += [chamber_max_height + chamber_offset]
            
            if wind_repeated == True:
                if cycle_key not in cycle_dictionary:
                    cycle_dictionary[cycle_key] = {}
                    cycle_dictionary[cycle_key]['chamber'] = chamber[:]
                    cycle_dictionary[cycle_key]['pieces'] = piece_counter
                    cycle_dictionary[cycle_key]['height'] = chamber_max_height + chamber_offset
                    cycle_dictionary[cycle_key]['prev_height'] = prev_height
                    cycle_dictionary[cycle_key]['prev_chamber'] = prev_chamber
                else:
                    if cycle_dictionary[cycle_key]['chamber'] == chamber:
                        # we have a cycle
                        cycle_start_height = cycle_dictionary[cycle_key]['height']
                        cycle_height = prev_height - cycle_start_height 
                        cycle_start_pieces = cycle_dictionary[cycle_key]['pieces']
                        cycle_length = piece_counter - cycle_start_pieces - 1
                        cycle_prev_chamber = cycle_dictionary[cycle_key]['prev_chamber']
                        found_cycle = True
                        
        else:
            shape_start -= 1
    #if found_cycle == True:
        #break
# Determine full cycles + whatever else is needed to get to 
total_cycles_needed = 1000000000000
pre_cycle = cycle_start_pieces - 1
remaining_cycles = total_cycles_needed - pre_cycle

#remaining_cycles = total_cycles_needed - cycle_start_pieces - 1
full_cycles = remaining_cycles // cycle_length
extra_iterations = remaining_cycles % cycle_length 

pieces = extra_iterations
cycle_detect_current_height = chamber_max_height + chamber_offset

initial_height = heights[cycle_start_pieces - 1]
added_cycle_height = full_cycles * cycle_height
post_cycle_height = heights[cycle_start_pieces - 1 + extra_iterations] - heights[cycle_start_pieces - 1] 



total_height = initial_height + added_cycle_height + post_cycle_height
print('Part 1: chamber max height after 2022 pieces is ' + str(total_height))
# 1596903669743 too high
# 1597477064237 too high