def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        squared_row = [num ** 2 for num in row]
        new_matrix.append(squared_row)

    return new_matrix