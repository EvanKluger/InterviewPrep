
def spiral_ordering(matrix):
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    result = []


    while top <= bottom and left <= right:
        # move RIGHT

        for i in range(left, right + 1):
            result.append(matrix[top][i])
        
        top += 1
        
        #move DOWN
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        
        right -= 1

        #move LEFT

        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
        bottom -= 1
        #move UP

        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
        
        left += 1

        return result
    

# Test Case 1:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiral_ordering(matrix1))  # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Test Case 2:
matrix2 = [
    [1]
]
print(spiral_ordering(matrix2))  # Expected: [1]

# Test Case 3:
matrix3 = [
    [1, 2],
    [4, 3]
]
print(spiral_ordering(matrix3))  # Expected: [1, 2, 3, 4]


# Test Case 4:
matrix4 = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]
print(spiral_ordering(matrix4))  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Test Case 5:
matrix5 = [
    [1, 2],
    [6, 3],
    [5, 4]
]
print(spiral_ordering(matrix5))  # Expected: [1, 2, 3, 4, 5, 6]

# Test Case 6:
matrix6 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
print(spiral_ordering(matrix6))  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

