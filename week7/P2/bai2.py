import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [1, 2, 3]])
print(f"A+B = {A+B}")
print(f"A^T + B^T = {A.T} + {B.T} = {A.T + B.T}")
print(f"(A+B)^T = {(A+B).T}")
print(f"(A+B)^T == A^T + B^T --> {np.all((A+B).T == A.T + B.T)}")