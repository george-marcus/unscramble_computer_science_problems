"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

duration_per_phone_number_dict = {}

for call in calls:
    incoming_phone_number = call[0]
    answering_phone_number = call[1]
    duration = call[3]

    if incoming_phone_number in duration_per_phone_number_dict:
        duration_per_phone_number_dict[incoming_phone_number] += int(duration)
    else:
        duration_per_phone_number_dict[incoming_phone_number] = int(duration)

    if answering_phone_number in duration_per_phone_number_dict:
        duration_per_phone_number_dict[answering_phone_number] += int(duration)
    else:
        duration_per_phone_number_dict[answering_phone_number] = int(duration)

longest_phone_call_number = max(duration_per_phone_number_dict,
                                key=lambda x: duration_per_phone_number_dict[x])
print(
    f'{longest_phone_call_number} spent the longest time, {duration_per_phone_number_dict[longest_phone_call_number]} seconds, on the phone during September 2016')
