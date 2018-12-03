
#with open('input.txt', 'r') as file:
#	numbers = []
#	for line in file:
#
#		sign = 1
#		if line[0] == "-":
#			sign = -1
#		numbers.append((sign*int(line[1:])))
#	

with open('input.txt', 'r') as file:
	frequencies = {0:1}	
	input = []
	frequency = 0
	found_value = None
	for line in file:
	
		sign = 1
		if line[0] == "-":
			sign = -1
		input.append(sign*int(line[1:]))

	i = 0
	print(input)
	while found_value is None:
		frequency += input[i % len(input)]
		i += 1
		if frequency in frequencies:
			found_value = frequency
		else:
			frequencies[frequency] = 1
		#print(frequencies)
	
	print(found_value)

