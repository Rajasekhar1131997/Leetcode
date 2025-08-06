# Leetcode Problem 48: Rotate Image
# https://leetcode.com/problems/rotate-image/

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Initialize the left and right pointers to start and end of the matrix
        left, right = 0, len(matrix) - 1
        # Loop until the left value is less than right
        while left < right:
            # Inner loop to shift the values
            for i in range(right - left):
                # intializing the top and bottom variables
                top, bottom = left, right

                # Save the top left most element into top_left
                top_left = matrix[top][left+i]

                # move the bottom left element to top left
                matrix[top][left+i] = matrix[bottom - i][left]

                # move the bottom right element to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move the top right element to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # move the top left element into top right
                matrix[top + i][right] = top_left
            # move the left pointer to right side
            left += 1
            # move the right pointer to the left side
            right -= 1