import re
from functools import reduce
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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A


def filter_calls(record):
    incoming_phone_number = record[0]

    first_five_chars_in_phone_number = incoming_phone_number[:5]

    return first_five_chars_in_phone_number == '(080)'


calls_from_bangalore = list(filter(filter_calls, calls))

codes_dict = {}

for call in calls_from_bangalore:

    answering_phone_number = call[1]

    first_three_digits_in_answering_phone_number = answering_phone_number[:3]

    first_four_digits_in_answering_phone_number = answering_phone_number[:4]

    matched_fixed_lines_codes = re.match(
        r"\(([0-9]+)\)", answering_phone_number)

    # Check for fixed lines phone numbers

    if matched_fixed_lines_codes:

        digits_within_parentheses = matched_fixed_lines_codes.group(0)[1:-1]

        if digits_within_parentheses in codes_dict:

            codes_dict[digits_within_parentheses] += 1

        else:
            codes_dict[digits_within_parentheses] = 1

        continue

    # Check for telemarketers phone numbers

    if first_three_digits_in_answering_phone_number == '140':

        if '140' in codes_dict:

            codes_dict['140'] += 1

        else:
            codes_dict['140'] = 1

        continue

    # Check for mobile phone numbers

    if first_four_digits_in_answering_phone_number in codes_dict:

        codes_dict[first_four_digits_in_answering_phone_number] += 1

    else:
        codes_dict[first_four_digits_in_answering_phone_number] = 1

print("The numbers called by people in Bangalore have codes:")

lexographically_sorted_codes = sorted([*codes_dict])

for code in lexographically_sorted_codes:
    print(code)

# Part B

fixed_lines_call_duration = codes_dict['080']

duration_of_all_lines_calls = reduce(
    lambda acc, value: acc + value, codes_dict.values(), 0)

percent_of_calls = round(fixed_lines_call_duration *
                         100 / duration_of_all_lines_calls, 2)

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent_of_calls))
