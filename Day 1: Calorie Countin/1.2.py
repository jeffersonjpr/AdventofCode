list_of_results = [0,0,0]

def insert_into_list(candidate):
    if candidate > min(list_of_results):
        list_of_results.remove(min(list_of_results))
        list_of_results.append(candidate)

with open("input.txt") as f:
    aux = 0
    for line in f:
        if line == '\n':
            insert_into_list(aux)
            aux = 0
            
        else:    
            aux += int(line)
    
insert_into_list(aux)
print(f"Results: {list_of_results}")
print(f"Sum: {sum(list_of_results)}")