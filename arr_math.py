import numpy as np

# Input dimensions N and M
N, M = map(int, input().split())

# Input the elements of array A
A = np.array([list(map(int, input().split())) for _ in range(N)])

# Input the elements of array B
B = np.array([list(map(int, input().split())) for _ in range(N)])

# Perform element-wise operations of A and B
print(np.add(A, B))  # Add (A + B)
print(np.subtract(A, B))  # Subtract (A - B)
print(np.multiply(A, B))  # Multiply (A * B)
print(np.floor_divide(A, B))  # Integer division (A // B)
print(np.mod(A, B))  # Mod (A % B)
print(np.power(A, B))  # Power (A ** B)
