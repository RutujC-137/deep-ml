import numpy as np

def matrix_dot_vector(a: list, b:list)-> list:
	try:
		a = np.array(a)
		b = np.array(b)
		if a.shape[1] != b.shape[0]:
			return -1

		result = np.dot(a, b)
		return result.tolist()
	except Exception:
		return -1 
