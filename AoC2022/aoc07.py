f = open('aoc07.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Start to build the structure

folders = {}
# create a root folder
folders['/'] = {}
folders['/']['children'] = []
folders['/']['files'] = []
folders['/']['parent'] = []
folders['/']['name'] = '/'
folders['/']['size'] = 0
parent_folder = {}
current_folder = folders['/']
current_path = ['/']
for line in raw_input[1:]:

    split_line = line.split(' ')
    if split_line[0] == '$':
        # command
        if split_line[1] == 'cd':
            if split_line[2] != '..':

                
                next_folder_name = split_line[2]
                current_path += [next_folder_name]
                next_folder = '/'.join(current_path)
                
                
                if next_folder not in folders:
                    folders[next_folder] = {}
                    folders[next_folder]['name'] = next_folder
                    folders[next_folder]['files'] = []
                    folders[next_folder]['children'] = []
                    folders[next_folder]['parent'] = current_folder
                    folders[next_folder]['size'] = 0
                current_folder['children'] += [folders[next_folder]]
                current_folder = folders[next_folder]
            else:
                
                if current_folder['parent'] != []:
                    current_path.pop()
                   
                    current_folder = current_folder['parent']
    else:
        split_line = line.split(' ')
        if split_line[0] != 'dir':
            current_folder['size'] += int(split_line[0])



# try to print out the file tree

def calc_size(folder):
    if folder['children'] != []:
        for child in folder['children']:
            folder['size'] += calc_size(child)
    return folder['size']
calc_size(folders['/'])
total_size = 0
for item in folders:
    if folders[item]['size'] <= 100000:
        total_size += folders[item]['size']
print('Part 1: total size of relevant directories is ' + str(total_size))
total_available = 70000000
free_needed = 30000000
free_available = total_available - folders['/']['size']
total_needed = free_needed - free_available
target_number = free_needed
for item in folders:
    if folders[item]['size'] >= total_needed and folders[item]['size'] <= target_number:
        target_number = folders[item]['size']
print('Part 2: total size of directory to delete is ' + str(target_number))
