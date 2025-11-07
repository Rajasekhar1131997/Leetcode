# Leetcode Problem 1380: Lucky Numbers in a Matrix
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # find the m and n values
        m = len(matrix)
        n = len(matrix[0])
        # initialize two list to keep track of min elements in each row and max elements of each col
        row_min_elements = []
        col_max_elements = []
        # loop through each row and add elements to row_min_elements list
        for row in matrix:
            row_min_elements.append(min(row))
        # loop through each col
        for j in range(n):
            # assign a prefix value i.e., first value of 1st row and 1st column
            max_value = matrix[0][j]
            # loop through each row and find the max value of each column and add it to col max list
            for i in range(1, m):
                if matrix[i][j] > max_value:
                    max_value = matrix[i][j]
            col_max_elements.append(max_value)
        # find the lucky number which is present in both list and return that number
        result = [num for num in row_min_elements if num in col_max_elements]
        return result

print("Time Complexity: O(M * N)")
print("Space Complexity: O(M + N)")