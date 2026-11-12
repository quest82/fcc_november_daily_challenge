def build_matrix(rows, cols):
    array = []
    i = 0
    while i < rows:
        array.append([])
        i += 1

    for row in array:
        for num in range(cols):
            row.append(0)
    
    
    return array

print(build_matrix(9, 1))