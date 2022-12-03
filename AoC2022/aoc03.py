f = open('aoc03.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
priority_sum = 0
for line in raw_input:
    # divide line in half
    line_length = len(line)
    first = line[:int(line_length / 2)]
    second = line[int(line_length / 2):]
    for letter in first:
        if letter in second:
            # Find the priority
            if letter == letter.upper():
                # uppercase
                priority = ord(letter) - ord('A') + 27
            else:
                priority = ord(letter) - ord('a') + 1
            priority_sum += priority
            break
print('Part 1: priority sum is ' + str(priority_sum))
# Part 2
priority_sum = 0
for i in range(0, len(raw_input) - 2, 3):
    first = raw_input[i]
    second = raw_input[i + 1]
    third = raw_input[i + 2]
    for letter in first:
        if (letter in second) and (letter in third):
            if letter == letter.upper():
                # uppercase
                priority = ord(letter) - ord('A') + 27
            else:
                priority = ord(letter) - ord('a') + 1
            priority_sum += priority
            break            
print('Part 2: priority sum is ' + str(priority_sum))
