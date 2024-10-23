import numpy as np

# Input
N, M = map(int, input().split())  # Reading dimensions N and M
array = np.array(
    [list(map(int, input().split())) for _ in range(N)]
)  # Reading N lines of M integers each

# Calculating results
mean_result = np.mean(array, axis=1)  # Calculating mean along axis 1 (rows)
var_result = np.var(array, axis=0)  # Calculating variance along axis 0 (columns)
std_result = np.std(
    array, axis=None
)  # Calculating standard deviation for the entire array

# Output
print(mean_result)  # Printing mean
print(var_result)  # Printing variance
print(round(std_result, 11))  # Printing standard deviation 