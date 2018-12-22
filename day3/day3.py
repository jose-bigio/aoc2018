def get_entries(input_file):
    with open(input_file, 'r') as file:
        entries = [ ]
        for line in file:
            line = line.split()
            claimID = line[0][1:]
            x, y = line[2].split(",")
            x = int(x)
            y = y[:-1]
            width, height = line[3].split("x")
            entries.append([claimID, int(x), int(y), int(width),int(height)])

    return entries

# don't know the size of cloth
# so best way is to use dictionaires to
# not allocate entire memory
# dictionary of rows. claim_grid[x][y] -> number of entries at this point
def populate_entries(entries):
    claim_grid = {}
    overlap = 0
    for entry in entries:
        _, x, y, width, height = entry
        for i in range(x, x+width):
            if i not in claim_grid:
                claim_grid[i] = {}
            for j in range(y, y+height):
                if j not in claim_grid[i]:
                    claim_grid[i].update({j:1})
                else:
                    if claim_grid[i][j] == 1:
                        overlap += 1
                    claim_grid[i][j] += 1
                    
    return overlap, claim_grid

# how many square inches of fabric are within two or more claims?
entries = get_entries('input.txt')
overlap, claim_grid = populate_entries(get_entries('input.txt'))


def find_non_overlapping(claim_grid, entries):
    for entry in entries:
        claimID, x, y, width, height = entry
        claimValid = True
        for i in range(x, x+width):
            if not claimValid:
                break
            for j in range(y, y+height):
                if claim_grid[i][j] != 1:
                   claimValid = False
                   break
        if claimValid:
            return claimID


print(find_non_overlapping(claim_grid, entries))
# example problem
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2


# x, y width x height
# top left -> x, y 
# top right -> x, y + width

# bottom left -> x+height, y
# bottom right -> x+height, y + width

# determing overlap and how much overlap
# There is overlap if the corrner of one image is 
