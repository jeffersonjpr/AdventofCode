import re
result = 0
with open("input.txt", "r") as f:
    for line in f:
        found_list = re.findall(r"\d", line)
        print(found_list)
        result += int(found_list[0] + found_list[-1])
print("The result is: ", result)