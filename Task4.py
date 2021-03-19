"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_telemarketer_phone_numbers = set()

other_phone_numbers = set()

for call in calls:
    incoming_phone_number = call[0]
    possible_telemarketer_phone_numbers.add(incoming_phone_number)

    answering_phone_number = call[1]
    other_phone_numbers.add(answering_phone_number)

for text in texts:
    incoming_phone_number = text[0]
    answering_phone_number = text[1]

    other_phone_numbers.add(incoming_phone_number)
    other_phone_numbers.add(answering_phone_number)

lexographically_sorted_telemarketers_numbers = sorted(
    possible_telemarketer_phone_numbers.difference(other_phone_numbers))


print('These numbers could be telemarketers: ')

for phone_number in lexographically_sorted_telemarketers_numbers:
    print(phone_number)
