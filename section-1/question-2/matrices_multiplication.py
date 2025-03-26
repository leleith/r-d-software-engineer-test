import numpy as np


def basic_multiply(
        matrix1: list[list[int]], 
        matrix2: list[list[int]]
) -> list[list[int]]:
    """
    Perform matrix multiplication using nested loops.
    
    :param matrix1: First input matrix
    :param matrix2: Second input matrix
    :return: Resulting matrix after multiplication
    :raises ValueError: If matrices cannot be multiplied
    """

    # Check if multiplication is possible
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrix dimensions are incompatible for multiplication")
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result


def numpy_multiply(
        matrix1: list[list[int]], 
        matrix2: list[list[int]]
) -> list[list[int]]:
    """
    Perform matrix multiplication using NumPy for optimization.
    
    :param matrix1: First input matrix (list of lists)
    :param matrix2: Second input matrix (list of lists)
    :return: Resulting matrix after multiplication
    """

    # Convert lists to NumPy arrays
    np_matrix1 = np.array(matrix1)
    np_matrix2 = np.array(matrix2)
    
    try:
        # Perform matrix multiplication
        result = np.dot(np_matrix1, np_matrix2)
    except ValueError:
        print('\n************** Impossible to multiply **************')
        return None
    
    # Convert back to list of lists
    return result.tolist()


if __name__ == "__main__":
    # Example matrices for demonstration
    list_a = [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 3, 4],
            [2, 1, 7]
        ],
        [
            [1, 2, 8],
            [8, 7, 0], 
            [4, 6, 9]
        ],
        [
            [3, 0],
            [9, 11],
            [2, 1]
        ]
    ]
    
    list_b = [
        [
            [9, 1, 0],
            [5, 6, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ]
    
    for matrix_a in list_a:
        for matrix_b in list_b:
            print("Matrix A:")
            for row in matrix_a:
                print(row)
            
            print("\nMatrix B:")
            for row in matrix_b:
                print(row)
            
            # NumPy multiplication
            numpy_result = numpy_multiply(matrix_a, matrix_b)
            
            if numpy_result:
                print("\nNumPy Method Result:")

                for row in numpy_result:
                    print(row)

            print("\n-----------------\n")
