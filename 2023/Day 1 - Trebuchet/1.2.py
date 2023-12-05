import re

def find_first_last(input: str):
    found_list = re.findall(r"\d", input)
    return found_list[0] + found_list[-1]

def replace_numbers(input: str):
    replacements = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    for word, replacement in replacements.items():
        input = input.replace(word, replacement)
    return input

result = 0
with open('input.txt', "r") as f:
    for line in f:
        result += int(find_first_last(replace_numbers(line)))
print("The result is: ", result)
