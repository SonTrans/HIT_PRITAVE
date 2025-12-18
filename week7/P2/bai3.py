import numpy as np

# Ma trận A kích thước 2×3
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Ma trận B kích thước 3×2
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])
print(f"A*B = {A@B}")
print(f"B^T * A^T = {B.T} * {A.T} = {B.T @ A.T}")
print(f"(B*A)^T = {(A@B).T}")
print(f"(B*A)^T == B^T*A^T --> {np.all((A@B).T == B.T @ A.T)}")