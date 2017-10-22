#Operation with numpy libraries
import numpy as np

print(np.cos(1))

print("Matrix 1:")
matrix1=np.arange(9).reshape(3,3)
print(matrix1)


print('\nMatrix 2:')
matrix2=np.arange(11,20,1).reshape(3,3)
print(matrix2)

print("\nMultiplication of M1 and M2 is :-")
print(matrix1*matrix2)