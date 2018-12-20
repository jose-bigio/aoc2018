# returns sorted list of entries
def parse_input(input_file):
    entries = []
    with open(input_file, 'r') as file:
        for line in file:
            current_list = line.split()
            time = current_list[0] + ' ' +  current_list[1]
            time = time.replace('[', '').replace(']', '')

            entries.append([time, current_list[2:]]) 
    

    entries = sorted(entries, key=lambda x: x[0])
    return entries


def time_asleep(entries):
    time_asleep_dict = {}
    sleep_minute_dict = {}
    past_time, guard_number, current_time = None, None, None
    for entry in entries:
        state = entry[1][0]
        if state == "Guard":
            guard_number = entry[1][1][1:]
        elif state == "falls":
            past_time = entry[0].split(" ")[1][3:]
        elif state == "wakes":
            current_time = entry[0].split(" ")[1][3:]
            time_slept = int(current_time) - int(past_time)
            if guard_number in time_asleep_dict:
                time_asleep_dict[guard_number] += time_slept
            else:
                time_asleep_dict[guard_number] = time_slept
            
            for x in range(int(past_time), int(current_time)):
                if guard_number in sleep_minute_dict:
                    sleep_minute_dict[guard_number][x] += 1
                else:
                    sleep_minute_dict[guard_number] = [0] * 61

    return time_asleep_dict, sleep_minute_dict

entries = (parse_input('input.txt'))
sleep_times, sleep_overlap = time_asleep(entries)

best_guard = None
max_time = 0
for guard, time in sleep_times.items():
    if time > max_time:
        best_guard = guard
        max_time = time

print("Sleepiest guard is {}".format(best_guard))
values = sleep_overlap[best_guard]
max_sleep_minute = values.index(max(values))
print("They sleep the most at time {}".format(max_sleep_minute))

print(max_sleep_minute*int(best_guard))

def most_frequently_asleep(sleep_overlap):
    guard_number = None 
    minute = None
    max_frequency = 0
    for guard, frequencies in sleep_overlap.items():
       current_frequency = max(frequencies)
       if current_frequency > max_frequency:
           max_frequency = current_frequency
           minute = frequencies.index(max_frequency)
           guard_number = guard

    return int(guard_number) * int(minute)

print(most_frequently_asleep(sleep_overlap))
