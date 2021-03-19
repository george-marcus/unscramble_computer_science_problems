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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
all_phone_numbers = set()

phone_numbers_in_texts = [(all_phone_numbers.add(
    record[0]), all_phone_numbers.add(record[1])) for record in texts]

phone_numbers_in_calls = [(all_phone_numbers.add(
    record[0]), all_phone_numbers.add(record[1])) for record in calls]

print("There are {} different telephone numbers in the records.".format(
    len(all_phone_numbers)))
