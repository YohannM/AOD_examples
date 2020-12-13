import random as rd
import time
import sys
import timeit

TAILLE_MATRICE = 2000
TAILLE_SOUS_MATRICES = 200
MAX = 1


def get_sous_matrice(placement):
    nombre_bloc_par_ligne = TAILLE_MATRICE // TAILLE_SOUS_MATRICES
    ligne_debut = (placement // nombre_bloc_par_ligne) * TAILLE_SOUS_MATRICES
    colonne_debut = (placement * TAILLE_SOUS_MATRICES) % TAILLE_MATRICE
    result = [[0 for j in range(TAILLE_SOUS_MATRICES)] for i in range(TAILLE_SOUS_MATRICES)]

    for i, x in zip(range(ligne_debut, ligne_debut + TAILLE_SOUS_MATRICES), range(TAILLE_SOUS_MATRICES)):
        for j, y in zip(range(colonne_debut, colonne_debut+TAILLE_SOUS_MATRICES), range(TAILLE_SOUS_MATRICES)):
            result[x][y] = matrix[i][j]

    return result

def mat_mul(X, Y):
    result = [[0 for j in range(TAILLE_SOUS_MATRICES)] for i in range(TAILLE_SOUS_MATRICES)]
    for I in range(0, TAILLE_SOUS_MATRICES, K):
        i_end = I + K if I + K < TAILLE_SOUS_MATRICES else TAILLE_SOUS_MATRICES
        for J in range(0, TAILLE_SOUS_MATRICES, K):
            j_end = J + K if J + K < TAILLE_SOUS_MATRICES else TAILLE_SOUS_MATRICES
            for P in range(0, TAILLE_SOUS_MATRICES, K):
                p_end = P + K if P + K < TAILLE_SOUS_MATRICES else TAILLE_SOUS_MATRICES
                for i in range(I, i_end, 1):
                    for j in range(J, j_end, 1):
                        for p in range(P, p_end, 1):
                            result[i][j] += X[i][p] * Y[p][j]
    return result

def mat_mul_raw(X, Y):
    result = [[0 for j in range(TAILLE_SOUS_MATRICES)] for i in range(TAILLE_SOUS_MATRICES)]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def get_nth_fibo_mult_blocking(n):
    placement = ordre[n-1]
    if (n == 1):
        return get_sous_matrice(placement)
    
    return mat_mul(get_sous_matrice(placement), get_nth_fibo_mult_blocking(n-1))

def get_nth_fibo_mult_blocking_memo(n):
    placement = ordre[n-1]
    if (n == 1):
        return get_sous_matrice(placement)

    if table_memo_blocking[n-1] == None:
        table_memo_blocking[n - 1] = mat_mul(get_sous_matrice(placement), get_nth_fibo_mult_blocking_memo(n-1))
    
    return table_memo_blocking[n - 1]
    
def get_nth_fibo_mult_memo(n):
    placement = ordre[n-1]
    if (n == 1):
        return get_sous_matrice(placement)
    if table_memo[n-1] == None:
        table_memo[n - 1] = mat_mul_raw(get_sous_matrice(placement), get_nth_fibo_mult_memo(n-1))
    return table_memo[n - 1]

def get_nth_fibo_mult_raw(n):
    placement = ordre[n-1]
    if (n == 1):
        return get_sous_matrice(placement)
    return mat_mul_raw(get_sous_matrice(placement), get_nth_fibo_mult_raw(n-1))


matrix = [[rd.randint(1, MAX) for j in range(TAILLE_MATRICE)] for i in range(TAILLE_MATRICE)]

nombre_sous_matrice = int(TAILLE_MATRICE * TAILLE_MATRICE / (TAILLE_SOUS_MATRICES * TAILLE_SOUS_MATRICES))
table_memo = [None for k in range(nombre_sous_matrice)]
table_memo_blocking = [None for k in range(nombre_sous_matrice)]

ordre = [i for i in range(nombre_sous_matrice)]
rd.shuffle(ordre)

K = 128

print("TEST : TAILLE_MATRICE = ", TAILLE_MATRICE, ", TAILLE_SOUS_MATRICE = ", TAILLE_SOUS_MATRICES," :")

print("simple:")
for i in range(10, 31):
    start = time.time()
    get_nth_fibo_mult_raw(i)
    end = time.time()
    print("{:.3f}".format(end - start))

print("blocking")
for i in range(10, 31):
    start = time.time()
    get_nth_fibo_mult_blocking(i)
    end = time.time()
    print("{:.3f}".format(end - start))

print("memo")
for i in range(10, 31):
    start = time.time()
    get_nth_fibo_mult_memo(i)
    end = time.time()
    print("{:.3f}".format(end - start))

print("blocking + mémo")
for i in range(10, 31):
    start = time.time()
    get_nth_fibo_mult_blocking_memo(i)
    end = time.time()
    print("{:.3f}".format(end - start))

print("\nEND")