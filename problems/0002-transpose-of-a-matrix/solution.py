def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    if not a :
        return []

    row = len(a)
    cols = len(a[0])
    result = []

    
    

    for j in range(cols):
        new_row = []
        for i in range(row):
            new_row.append(a[i][j])
        result.append(new_row)
    
    return result
