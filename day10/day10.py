import re
import time
# regex: position=<([\s|-][0-9]*),\s([\s|-][0-9]*)> velocity=<([\s|-][0-9]*,\s)([\s|-][0-9]*)>

pattern = "position=<([\s|-][0-9]*),\s([\s|-][0-9]*)> velocity=<([\s|-][0-9]*),\s([\s|-][0-9]*)>"
def update_velocities(positions):
    for entry in positions:
        x, y = entry['position'][0], entry['position'][1]
        velocity_x, velocity_y = entry['velocity'][0], entry['velocity'][1]
        entry['position'] = [x+velocity_x, y+velocity_y]
    
    return positions

def bounding_box(positions):
    print("creating visualization")
    min_x, min_y, max_x, max_y = None, None, None, None
    for entry in positions:
        x, y = entry['position'][0], entry['position'][1]
        if max_x is None:
            max_x = x
        if min_x is None:
            min_x = x

        if min_y is None:
            min_y = y
        if max_y is None:
            max_y = y

        if max_x < x:
            max_x = x
        if min_x > x:
            min_x = x

        if min_y > y:
            min_y = y
        if max_y < y:
            max_y = y

    # Height of the array -> max_x - min_x
    # Width of the array -> max_y - min_y

    return max_x, max_y, min_x, min_y

# want to know what the array size should be need min and max x and y
def visualize(positions, max_x, max_y, min_x, min_y):
    height = max_x - min_x
    width = max_y - min_y
    print("Creating an array of size {} by {}".format(height, width))
    array = [ ['.' for _ in range(height+1)] for _ in range(width+1) ]
    
    print("Array has {} rows and rows of length {}".format(len(array), len(array[0])))
    print("Populating the array for each position")
    # Let min_x, min_y be 0, 0
    for entry in positions:
        x, y = entry['position'][0]-min_x, entry['position'][1]-min_y
        array[y][x] = 'x' 


    print("Converting array to string\n\n")
    for row in array:
        string = ""
        for element in row:
            string += element
        print("{}\n".format(string))


with open("input.txt", "r") as file:
    positions = []
    for line in file:
        m = re.match(pattern, line)
        positions.append({"position": [int(m.group(1)), int(m.group(2))], "velocity": [int(m.group(3)), int(m.group(4))]})

    for _ in range(1000000):
        positions = update_velocities(positions)
        max_x, max_y, min_x, min_y = bounding_box(positions)
        height = max_x - min_x
        width = max_y - min_y
        print("Bounding box is {} by {}".format(height, width))
        if width + height < 200:
            visualize(positions, max_x, max_y, min_x, min_y)
            time.sleep(5)
        #print("Input is {} position is {}, {} and velocity is {}, {}".format(line, m.group(1), m.group(2), m.group(3), m.group(4)))
