import re

def find_first_last(input: str):
    found_list = re.findall(r"\d", input)
    return found_list[0] + found_list[-1]

def replace_numbers(input: str):
    replacements = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for word, replacement in replacements.items():
        input = input.replace(word, replacement)
    return input

result = 0
with open('input.txt', "r") as f:
    for line in f:
        result += int(find_first_last(replace_numbers(line)))
print("The result is: ", result)
