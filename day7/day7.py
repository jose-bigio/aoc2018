with open('input.txt', 'r') as file:
    all_dependencies = set()
    dependencies = {}
    reverse_dependencies = {}
    for line in file:
        line = line.split()
        dependency, task = line[1], line[7]

        all_dependencies.add(dependency)
        if task in dependencies:
            dependencies[task].extend(dependency)
        else:
            dependencies[task] = [dependency]

        if dependency in reverse_dependencies:
            reverse_dependencies[dependency].extend(task)
        else:
            reverse_dependencies[dependency] = [task]

        
    print("Reverse dependencies {}".format(reverse_dependencies))
    print("Dependencies {}".format(dependencies))

    start_candidates = list(all_dependencies.difference(dependencies.keys()))
    start = "J"

    current = start
    print("Trying to remove {} from {}".format(start, start_candidates))
    #reachable =  set(start_candidates.remove(start))
    reachable =  {"X", "K"}
    order = start

    while len(order) != len(all_dependencies)+1:
        candidates = list(reverse_dependencies[current])
        completed = set(order)
        for candidate in candidates:
            if set(dependencies[candidate]).difference(completed) == set():
                reachable.add(candidate)
        set_list = list(reachable)
        set_list.sort()
        print("Current is {}".format(current))
        print("can now reach {}".format(set_list))
        current = set_list[0]
        order += current
        reachable.remove(current)


    print(order)



