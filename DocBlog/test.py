from math import *

matrix = [[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]

lignes = len(matrix)
columns = len(matrix[0])


taille_matrix = int(lignes * columns)

for i in range(taille_matrix):
    print(max(matrix[i]))




# 119 + 114 + 56 + 125 = 414


