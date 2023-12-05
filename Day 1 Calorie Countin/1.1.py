with open("input.txt") as f:
    result, aux = 0, 0
    for line in f:
        if line == '\n':
            result = aux if aux > result else result
            aux = 0
            
        else:    
            aux += int(line)
    
result = aux if aux > result else result
print(f"Result: {result}")
