# Leetcode Problem 1351: Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # find the length of the grid
        m = len(grid)
        n = len(grid[0])
        # initialize the count to 0
        count = 0
        # loop through each row from the grid
        for i in range(m):
            # loop through each col from the row
            for j in range(n):
                # check if the number is less than 0 (negative number), then count it
                if grid[i][j] < 0:
                    count += 1
        # return the count
        return count

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")