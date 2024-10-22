# Matrix Operations with NumPy

**This project performs basic element-wise operations on two matrices (2D arrays) using the NumPy library in Python. The operations include addition, subtraction, multiplication, integer division (floor division), modulus, and power.**

## Table of Contents

- Problem Description
- Installation
- Usage
- Input Format
- Output Format
- Sample Input/Output
- Operations Performed
- Requirements


### Problem Description

You are given two integer matrices A and B of dimensions `N × M`. The task is to perform the following element-wise operations:

1. Addition: A+B
2. Subtraction: A−B
3. Multiplication: A×B
4. Integer Division: A//B (floor division)
5. Modulus: A%B
6. Power: A**B
 
The input consists of two matrices, and the program outputs the result of each operation in sequence.

### Installation

Before running the program, ensure that Python is installed and the necessary dependencies are installed. You can install the required dependencies using pip:

`pip install numpy`

### Usage

1. Clone the repository or download the Python script.

2. Run the script using Python:

`python matrix_operations.py`

3. Provide the input for the matrices when prompted.

#### Example:

````
    1 4
    1 2 3 4
    5 6 7 8
````    
The output will be:

````
    [[ 6  8 10 12]]
    [[-4 -4 -4 -4]]
    [[ 5 12 21 32]]
    [[0 0 0 0]]
    [[1 2 3 4]]
    [[    1    64  2187 65536]]
````

#### Input Format

1. The first line contains two space-separated integers, N and M, representing the dimensions of matrices A and B.

2. The next N lines contain M space-separated integers representing the matrix A.

3. The following N lines contain M space-separated integers representing the matrix B.

#### Output Format

The output consists of six printed matrices, each corresponding to the result of an element-wise operation between the matrices A and B.
The operations are printed in the following order:

1. Addition
2. Subtraction
3. Multiplication
4. Integer Division
5. Modulus
6. Power


### Sample Input/Output

#### Sample Input

`1 4`
`1 2 3 4`
`5 6 7 8`

#### Sample Output

`[[ 6  8 10 12]]`
`[[-4 -4 -4 -4]]`
`[[ 5 12 21 32]]`
`[[0 0 0 0]]`
`[[1 2 3 4]]`
`[[    1    64  2187 65536]]`

### Operations Performed

1. Addition `(np.add(A, B))`: Adds corresponding elements of the two matrices.

2. Subtraction `(np.subtract(A, B))`: Subtracts elements of B from A.

3. Multiplication `(np.multiply(A, B))`: Multiplies corresponding elements of A and B.

4. Integer Division `(np.floor_divide(A, B))`: Divides elements of A by corresponding elements in B, performing floor division.

5. Modulus `(np.mod(A, B))`: Returns the remainder when A is divided by B.

6. Power `(np.power(A, B))`: Raises each element of 
A to the power of the corresponding element in B.

### Requirements

Python 3.x
NumPy library (`pip install numpy`)