f = open('aoc10.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
x = 1
pc = 0
signal_check = 20
signal_strength_sum = 0
sprite_pos = [0, 1, 2]
cursor_pos = 0
display = []
current_row = 0
text_line = ''
for line in raw_input:
    split_line = line.split(' ')
    if split_line[0] == 'noop':
        pc += 1
        if int(cursor_pos / 40) > current_row:
            display += [text_line]
            text_line = ''
            current_row += 1
        if (cursor_pos % 40) in sprite_pos:
            text_line += '#'
        else:
            text_line += '.'
        cursor_pos += 1
        if pc == signal_check:
            signal_strength = x * signal_check
            signal_strength_sum += (x * signal_check)
            signal_check += 40        
    else:
        pc += 1
        if int(cursor_pos / 40) > current_row:
            display += [text_line]
            text_line = ''
            current_row += 1        
        if (cursor_pos % 40) in sprite_pos:
            text_line += '#'
        else:
            text_line += '.'
        cursor_pos += 1
        if pc == signal_check:
            signal_strength = x * signal_check
            signal_strength_sum += (x * signal_check)
            signal_check += 40
        pc += 1
        if int(cursor_pos / 40) > current_row:
            display += [text_line]
            text_line = ''
            current_row += 1        
        if (cursor_pos % 40) in sprite_pos:
            text_line += '#'
        else:
            text_line += '.'
        cursor_pos += 1
        if pc == signal_check:
            signal_strength = x * signal_check
            signal_strength_sum += (x * signal_check)
            signal_check += 40
        x += int(split_line[1])
        sprite_pos = [(x - 1) % 40, x % 40, (x + 1) % 40]
    if signal_check > 220:
        signal_check = 0
display += [text_line]
print('Part 1: sum of signal strength is ' + str(signal_strength_sum))
print('Part 2:')
for line in display:
    print(line)
    
