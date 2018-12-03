# part 1
def create_dict(input_string):
	frequency = {}
	for letter in input_string:
		if letter in frequency:
			frequency[letter] += 1
		else:
			frequency[letter] = 1
	return frequency

def check_x(occurrences, check):
	for x in occurrences:
		if x == check:
			return True
	return False



#with open('input.txt', 'r') as file:
#	two_count = 0
#	three_count = 0
#	for line in file:
#		frequency = create_dict(line)		
#		occurrences = frequency.values()
#		if check_x(occurrences, 2):
#			two_count += 1
#		if check_x(occurrences, 3):
#			three_count += 1
#	print(two_count)
#	print(three_count)
#	print(two_count * three_count)


# part 2
# ASsume strings have same length

def diff(string_1, string_2):
	count = 0
	index = None
	i =  0
	found = False
	for a, b in zip(string_1, string_2):
		if a != b:
			#print("{} != {}".format(a, b))
			found = True
			index =  i
			count += 1
		
		if count > 1:
			index = None
			found = False
			#print("Diff count of {} and {} was greater than 1".format(string_1, string_2))
			return found, index
		i += 1

	#print("Diff count of {} and {} is: ".format(string_1, string_2, count))
	return found, index


def find_box(boxes):
	for i in range(0, len(boxes)-1):
		for j in range(i+1, len(boxes)):
			print("Searching {} {}".format(i, j))
			found, index =  diff(boxes[i], boxes[j])
			if found:
				return boxes[i], index

	return "Not Found", "bleh"			


with open('input.txt', 'r') as file:
	boxes = []
	for line in file:
		boxes.append(line)

	box_id, index = find_box(boxes)
	print(box_id, index)

	print(box_id[:index] + box_id[index+1:])
