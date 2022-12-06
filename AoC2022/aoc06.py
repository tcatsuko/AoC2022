f = open('aoc06.txt','rt')
raw_input = ''
for line in f:
    raw_input += line[:-1]
f.close()
marker_pos = 0
for x in range(3,len(raw_input)):
    snippet = raw_input[x-3:x+1]
    unique_count = 0
    for letter in snippet:
        unique_count += snippet.count(letter)
    if unique_count == 4:
        marker_pos = x + 1
        break
print('Part 1: marker found after ' + str(marker_pos) + ' characters.')
for x in range(13,len(raw_input)):
    snippet = raw_input[x-13:x+1]
    unique_count = 0
    for letter in snippet:
        unique_count += snippet.count(letter)
    if unique_count == 14:
        marker_pos = x + 1
        break
print('Part 2: message found after ' + str(marker_pos) + ' characters.')