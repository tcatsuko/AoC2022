import ast
f = open('aoc13.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
packets = []
for line in raw_input:
    if line == '':
        continue
    packets += [ast.literal_eval(line)]
    
correct_order_sum = 0
def compare_packets(packet, int_list = False):
    left = packet[0]
    right = packet[1]

    left_list = isinstance(left, list)
    right_list = isinstance(right, list)
    
    if (left_list == False) and (right_list == False):
        if int(left) > int(right):
            return 1 # Denoting False  (i.e. right is smaller than left -- right of 0)
        elif int(left) < int(right):
            return -1 # Denoting True  (i.e left is smaller than right -- left of 0)
        else:
            return 0 # Denoting Equal
    else:
        if not(left_list):
            left = [left]
        elif not(right_list):
            right = [right]
        if len(left) == 0 and len(right) > 0:
            return -1 # Denoting True 

        for index in range(len(left)):
            new_left = left[index]
            if index > len(right) -1:
                return 1 # Denoting False
            new_right = right[index]            
            order = compare_packets([new_left, new_right])
            if order != 0:
                return order
            else:
                if (index == len(left) - 1) and (len(left) < len(right)):
                    return -1 # denoting True
    return 0 # Default to think the two packets are equal

for x in range(0, len(packets), 2):
    left_packet = packets[x]
    right_packet = packets[x + 1]
    packet = [left_packet, right_packet]
    test_compare = compare_packets(packet)
    if test_compare == -1:
        correct_order_sum += (x // 2 + 1)
print('Part 1: correct order index sum is ' + str(correct_order_sum))
# Now just figure out how many packets are "correctly left" of the divider

div1 = [[2]]
div2 = [[6]]
div1_index = 0
div2_index = 0
for packet in packets:
    if compare_packets([packet, div1]) < 0:
        div1_index += 1
    if compare_packets([packet, div2]) < 0:
        div2_index += 1
div1_index += 1 # Elf indexing starts at 1
div2_index += 2 # Elf indexing starts at 1, also need to shift up by one more to account for first dividing packet
print('Part 2: decoder key is ' + str(div1_index * div2_index))