def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == "row":
		result = []
		for row in matrix:
			result.append(sum(row)/len(row))
		return result
	elif mode == "column":
		result = []
		for j in range(len(matrix[0])):
			total = 0 
			for i in range(len(matrix)):
				total += matrix[i][j]
			result.append(total/len(matrix))
		
		return result 




	return means