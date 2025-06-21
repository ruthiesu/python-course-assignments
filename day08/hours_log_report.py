import sys
import re

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILENAME")

input_filename = sys.argv[1]
output_filename = sys.argv[2]

try:
    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()
except Exception as err:
    print('Could not read file:', input_filename, err)
    exit(1)

log_list = []
for i in range(len(lines)):
    m= re.search(r'^([0-2][0-9]:[0-9]{2})(.+)$', lines[i])
    if m:
        log_list.append((m.group(1), m.group(2).strip()))
        print("Found:", m.group(1), m.group(2).strip())



activity_duration = {}
total_duration = 0
log_string = ""
for i in range(len(log_list)-1):
    # print("looking at ", log_list[i], "and", log_list[i+1])
    if (log_list[i][1] == "End"): #skipping end activity
        log_string += f"\n"
        continue
    else:
        # print("Processing activity:", log_list[i][1])
        start_time = log_list[i][0]
        end_time = log_list[i+1][0]
        activity = log_list[i][1]

        log_string += f"{start_time}-{end_time} {activity}\n"
        # print(f"added: {start_time}-{end_time} {activity}\n")
        if activity not in activity_duration:
            activity_duration[activity] = 0

        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))

        duration = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
        activity_duration[activity] += duration
        total_duration += duration

try:
    with open(output_filename, 'w') as output_file:
        output_file.write(log_string + "\n")
        for activity, duration in activity_duration.items():
            percent = (int)((duration / total_duration) * 100)
            output_file.write(f"{activity:<30} {duration:>3} minutes {percent:>6}%\n")

except Exception as err:
    print('Could not write file:', output_filename, err)
    exit(1)

# 09:20-11:00 Introduction
# 11:00-11:15 Exercises
# 11:15-11:35 Break
# 11:35-12:30 Numbers and strings
# 12:30-13:30 Lunch Break
# 13:30-14:10 Exercises
# 14:10-14:30 Solutions
# 14:30-14:40 Break
# 14:40-15:40 Lists
# 15:40-17:00 Exercises
# 17:00-17:30 Solutions
#
# 09:30-10:30 Lists and Tuples
# 10:30-10:50 Break
# 10:50-12:00 Exercises
# 12:00-12:30 Solutions
# 12:30-12:45 Dictionaries
# 12:45-14:15 Lunch Break
# 14:15-16:00 Exercises
# 16:00-16:15 Solutions
# 16:15-16:30 Break
# 16:30-17:00 Functions
# 17:00-17:30 Exercises
#
# Break                      65 minutes    6%
# Dictionaries               15 minutes    1%
# Exercises                 340 minutes   35%
# Functions                  30 minutes    3%
# Introduction              100 minutes   10%
# Lists                      60 minutes    6%
# Lists and Tuples           60 minutes    6%
# Lunch Break               150 minutes   15%
# Numbers and strings        55 minutes    5%
# Solutions                  95 minutes    9%