def parse_file(input_file):
    data = []
    with open(input_file, 'r') as file:
        for line in file:
            entry = []
            for char in line.split()[0]:
                entry.append(char)
            data.append(entry)
            
    return data


