# Leetcode Problem 2643: Row With Maximum Ones
# https://leetcode.com/problems/row-with-maximum-ones/description/
from typing import List
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        # initialize the variables max ones and row index to -1
        max_ones = -1
        row_index = -1
        # loop through each index and list in mat
        for index, list in enumerate(mat):
            # find the sum of each list i.e. count of each row
            list_sum = sum(list)
            # if the list sum is greater than max ones
            if list_sum > max_ones:
                # assign the list sum to max ones and index to row index
                max_ones = list_sum
                row_index = index
        # return the row index and max ones at the end
        return [row_index, max_ones]

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")