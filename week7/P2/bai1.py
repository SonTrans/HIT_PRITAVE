import numpy as np
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 0],
              [1, 2]])
AB = A @ B
BA = B @ A
print(f"A = {A}")
print(f"B = {B}")
print(f"AB = {AB}")
print(f"BA = {BA}")
print(f"AB == BA --> {np.all(AB == BA)}")