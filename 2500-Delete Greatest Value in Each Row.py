# Leetcode Problem 2500: Delete Greatest Value in Each Row
# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
from typing import List
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # sort each row in grid
        for row in grid:
            row.sort()
        # initialize the total to 0
        total = 0
        # find the length of each row
        n = len(grid[0])
        # for every col in n, we find the max number
        for col in range(n):
            col_max = 0
            for row in grid:
                col_max = max(col_max, row[col])
            # add that col max to total
            total += col_max
        # return the total at the end
        return total

print("Time Complexity: O(M * N log N)")
print("Space Complexity: O(1)")