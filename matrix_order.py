import sys 

NOMBRE_MATRICES = 3 + 1 
# + 1 pour la taille de la liste matrixes_dimension

# dimensions : liste tel que A_i est 
# de taille dimensions[i-1]*dimensions[i]
def cout_opti_produit(dimensions): 

	for i in range(1, NOMBRE_MATRICES): 
		m[i][i] = 0

	for L in range(2, NOMBRE_MATRICES): 
		for i in range(1, NOMBRE_MATRICES - L + 1): 
			j = i + L - 1
			m[i][j] = sys.maxsize
			for k in range(i, j): 
				# m[i][k] le nombre d'opérations minimal de A_i * ... * A_k
				# m[k+1][j] le nombre d'opérations minimla de A_k+1 * ... * A_j
				# p[i-1]*p[k]*p[j] le nombre d'opérations pour multiplier
				# (A_i * ... * A_k) et (A_k+1 * ... * A_j)
				cout = m[i][k] + m[k + 1][j] + dimensions[i-1]*dimensions[k]*dimensions[j] 
				if cout < m[i][j]: 
					m[i][j] = cout
	return m[1][NOMBRE_MATRICES-1] 

# table de memoization des résultats 
m = [[0 for x in range(NOMBRE_MATRICES)] for x in range(NOMBRE_MATRICES)] 

matrixes_dimension = [100, 20, 100, 20]

print("Le nombre de multiplication minimum est de " +
	str(cout_opti_produit(matrixes_dimension)))