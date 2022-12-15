import re
import math

f = open('aoc15.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
sensors = set()
exclusion_points = {}
beacons = set()
def get_manhattan(source, destination):
    manhattan = abs(source[0] - destination[0]) + abs(source[1] - destination[1])
    return manhattan


for idx, line in enumerate(raw_input):
    print('Processing sensor pair ' + str(idx + 1) + ' of ' + str(len(raw_input)))
    [sensor, beacon] = line.split(':')
    sensor_pos = re.findall(r'-?\d+', sensor)
    sensor_pos = (int(sensor_pos[0]),int(sensor_pos[1]))
    beacon_pos = re.findall(r'-?\d+', beacon)
    beacon_pos = (int(beacon_pos[0]), int(beacon_pos[1]))
    
        
    beacons.add((beacon_pos[0],beacon_pos[1]))
    sensors.add((sensor_pos[0], sensor_pos[1]))
    manhattan = get_manhattan(sensor_pos, beacon_pos)
    exclusion_zone = manhattan 
    y_deviation = exclusion_zone
    x_deviation = 0
    for y in range(y_deviation, -1, -1):
        left_x = sensor_pos[0] - x_deviation
        right_x = sensor_pos[0] + x_deviation   # We are using ranges
        up_pos = sensor_pos[1] + y
        down_pos = sensor_pos[1] - y
       
        if up_pos not in exclusion_points:
            exclusion_points[up_pos] = []
        if down_pos not in exclusion_points:
            exclusion_points[down_pos] = []
        exclusion_points[up_pos] += [(left_x, right_x)]
        exclusion_points[down_pos] += [(left_x, right_x)]
        
       
        
        x_deviation += 1
# Now remove actual beacons from exclusion points
# Reduce each set of exclusion points
print('Finished marking off exclusion areas.  Now reducing the exclusion segments.')
#for idx,key in enumerate(exclusion_points):
    #print(' reducing line ' + str(idx + 1) + ' of ' + str(len(exclusion_points)))
    #replaced_line = True
    #while replaced_line == True:
        #replaced_line = False
        #exclusion_line = exclusion_points[key]
        #for idx, item in enumerate(exclusion_line[:-1]):
            #current_item = item
            #next_item = exclusion_line[idx + 1]
            ## Find overlap
            #if next_item[1] < current_item[0]:
                #continue
            #if current_item[1] < next_item[0]:
                #continue
            ## there's an intersection
            #replaced_line = True
            #new_line = (min(current_item[0], next_item[0]), max(current_item[1], next_item[1]))
            #exclusion_line[idx] = new_line
            #del(exclusion_line[idx + 1])
            #break
    #exclusion_points[key] = exclusion_line
interest_line = 2000000
replaced_line = True
while replaced_line == True:
    replaced_line = False
    exclusion_line = exclusion_points[interest_line]
    for idx, item in enumerate(exclusion_line[:-1]):
            current_item = item
            next_item = exclusion_line[idx + 1]
            # Find overlap
            if next_item[1] < current_item[0]:
                continue
            if current_item[1] < next_item[0]:
                continue
            # there's an intersection
            replaced_line = True
            new_line = (min(current_item[0], next_item[0]), max(current_item[1], next_item[1]))
            exclusion_line[idx] = new_line
            del(exclusion_line[idx + 1])
            break
    exclusion_points[interest_line] = exclusion_line
    
    


exclusion_line = exclusion_points[interest_line]
# Get raw number of occupied points
excluded_points = 1
for segment in exclusion_line:
    excluded_points += segment[1] - segment[0]
for beacon in beacons:
    for segment in exclusion_line:
        if beacon[0] >= segment[0] and beacon[0] <= segment[1] and beacon[1] == interest_line:
            excluded_points -= 1
if interest_line in exclusion_points:
    print('Part 1: there are ' + str(excluded_points) + ' points in line ' + str(interest_line) + ' that cannot be a beacon.')

# Part 2
min_y = 0
max_y = 4000000
candidate_position = None
found_distress_beacon = False
for y in range(2021700, max_y + 1):
    if found_distress_beacon == True:
        break
    #print('Checking line ' + str(y) + ' of ' + str(max_y))
    
    if y in exclusion_points:
        #print(' reducing line ' + str(idx + 1) + ' of ' + str(len(exclusion_points)))
        replaced_line = True
        while replaced_line == True:
            replaced_line = False
            exclusion_line = exclusion_points[y]
            for idx, item in enumerate(exclusion_line[:]):
                current_item = item
                # Find overlap
                if current_item[0] < 0 and current_item[1] < 0:
                    del(exclusion_line[idx])
                    replaced_line = True
                    break                    
                if current_item[0] > max_y and current_item[1] > max_y:
                    del(exclusion_line[idx])
                    replaced_line = True
                    break
                if current_item[0] < 0:
                    current_item = (0, current_item[1])
                    exclusion_line[idx] = current_item
                if current_item[1] > max_y:
                    current_item = (current_item[0], max_y)
                    exclusion_line[idx] = current_item
            exclusion_line.sort(key=lambda a:(a[0],a[1]))    
            exclusion_points[y] = exclusion_line
            
            replaced_line = True
            while replaced_line == True:
                replaced_line = False
                exclusion_line = exclusion_points[y]
                for idx, item in enumerate(exclusion_line[:-1]):
                    current_item = item
                    next_item = exclusion_line[idx + 1]
                    if next_item[1] < current_item[0]:
                        continue
                    if current_item[1] < next_item[0]:
                        continue
                    current_item = (min(current_item[0], next_item[0]), max(current_item[1], next_item[1]))
                    del(exclusion_line[idx + 1])
                    exclusion_line[idx] = current_item
                    replaced_line = True
                    break
                    
                    # Find overlap
                         

        
        unseen = len(exclusion_line)
            
        

        if unseen > 1:
            x_coord = (exclusion_line[1][0] + exclusion_line[0][1]) // 2
            #unseen_list = list(unseen)
            #print(unseen_list)
            print('Part 2: beacon found at (' + str(x_coord) + ',' + str(y) + '). Tuning frequency is ' + str(x_coord * 4000000 +  y))
            found_distress_beacon = True
                
        