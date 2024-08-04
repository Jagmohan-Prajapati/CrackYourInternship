# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        fcol = False
        frow = False

        # Check if the first column should be set to zero
        for i in range(rows):
            if matrix[i][0] == 0:
                fcol = True
        
        # Check if the first row should be set to zero
        for i in range(cols):
            if matrix[0][i] == 0:
                frow = True

        # Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set matrix cells to zero based on markers in the first row
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        # Set matrix cells to zero based on markers in the first column
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Set the first row to zero if needed
        if frow:
            for j in range(cols):
                matrix[0][j] = 0
            
        # Set the first column to zero if needed
        if fcol:
            for i in range(rows):
                matrix[i][0] = 0