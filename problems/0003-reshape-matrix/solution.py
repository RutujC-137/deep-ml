import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	row, col = new_shape
	elements = [x for row in a for x in row  ]

	if len(elements)!= row*col:
		return  []
	


	
	return [elements[i*col:col*(i+1)] for i in range(row)]