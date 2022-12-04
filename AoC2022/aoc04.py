f = open('aoc04.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
overlaps = 0
for line in raw_input:
    [elf1, elf2] = line.split(',')
    [elf1_low, elf1_high] = elf1.split('-')
    [elf2_low, elf2_high] = elf2.split('-')
    # check if 1 is in 2
    if int(elf1_low) >= int(elf2_low) and int(elf1_high) <= int(elf2_high):
        overlaps += 1
    #check if 2 is in 1
    elif int(elf2_low) >= int(elf1_low) and int(elf2_high) <= int(elf1_high):
        overlaps += 1
print('part 1: there are ' + str(overlaps) + ' overlaps')
# part 2
overlaps = 0
for line in raw_input:
    [elf1, elf2] = line.split(',')
    [elf1_low, elf1_high] = elf1.split('-')
    [elf2_low, elf2_high] = elf2.split('-')
    # check if 1 is in 2
    if (int(elf1_low) >= int(elf2_low)) and (int(elf1_low) <= int(elf2_high)):
        overlaps += 1
    elif (int(elf2_low) >= int(elf1_low)) and (int(elf2_low) <= int(elf1_high)):
        overlaps += 1
print('part 2: there are ' + str(overlaps) + ' overlaps')