import math
f = open('aoc17.txt','rt')
instructions = ''
for line in f:
    instructions = line.strip()
f.close()
inst_length = len(instructions)
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
found_one_cycle = False
pieces =100000
found_cycle_counter = 0
#pieces = 
elapsed_pieces = 0
found_cycle = False
inst_length = len(instructions)
cycle_height_list = []
cycle_start_list = []
for piece_counter in range(pieces):
    cycle_key = (shape_offset, wind_offset)
    # Housekeeping
    if len(chamber) > 2000:
        chamber_offset += len(chamber) - 2000
        for x in range(len(chamber)-2000):
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


                        cycle_history = cycle_dictionary[cycle_key]
                        cycle_history_pre_height = heights[cycle_history['pieces'] - 1]
                        cycle_start_height = heights[cycle_history['pieces']]
                        cycle_end_height = heights[piece_counter - 1]

                        cycle_start_height = cycle_dictionary[cycle_key]['height']
                        cycle_height = cycle_end_height - cycle_start_height
                        cycle_start_pieces = cycle_dictionary[cycle_key]['pieces']
                        cycle_length = piece_counter - cycle_start_pieces - 1
                        cycle_prev_chamber = cycle_dictionary[cycle_key]['prev_chamber']
                        alt_cycle_height = heights[piece_counter - 1] - heights[cycle_start_pieces] 
                        cycle_end = piece_counter - 1
                        found_cycle = True
                        
                        if cycle_key == (1,10086): # In my input this is the first detected cycle
                            #cycle_start_list += [cycle_history['pieces']  + len(cycle_height_list) * cycle_length]
                            if len(cycle_height_list) < 1:
                                cycle_height_list += [cycle_height]
                                cycle_start_list += [cycle_history['pieces']]
                            else:
                                cycle_height_list += [cycle_height - sum(cycle_height_list)]
                                
                            cycle_start_list += [piece_counter]

                        
        else:
            shape_start -= 1
    # if found_cycle == True:
    #     break

total_cycles_needed = 2022

pre_cycle = cycle_start_list[1] - 1
remaining_cycles = total_cycles_needed - pre_cycle
cycle_length = cycle_start_list[-1]- cycle_start_list[-2]

full_cycles = remaining_cycles // cycle_length
extra_iterations = remaining_cycles % cycle_length 

pieces = extra_iterations
cycle_detect_current_height = chamber_max_height + chamber_offset

initial_height = heights[pre_cycle]
added_cycle_height = full_cycles * cycle_height_list[-1]
post_cycle_height = heights[pre_cycle + extra_iterations] - heights[pre_cycle] 

total_height = initial_height + added_cycle_height + post_cycle_height
print('Part 1: chamber max height after 2022 pieces is ' + str(total_height))
total_cycles_needed = 1000000000000

pre_cycle = cycle_start_list[1] - 1
remaining_cycles = total_cycles_needed - pre_cycle
cycle_length = cycle_start_list[-1]- cycle_start_list[-2]

full_cycles = remaining_cycles // cycle_length
extra_iterations = remaining_cycles % cycle_length 

pieces = extra_iterations
cycle_detect_current_height = chamber_max_height + chamber_offset

initial_height = heights[pre_cycle]
added_cycle_height = full_cycles * cycle_height_list[-1]
post_cycle_height = heights[pre_cycle + extra_iterations] - heights[pre_cycle] 

total_height = initial_height + added_cycle_height + post_cycle_height
print('Part 2: chamber max height after 1000000000000 pieces is ' + str(total_height))
