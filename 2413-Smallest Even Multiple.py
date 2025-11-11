# Leetcode Problem 2413: Smallest Even Multiple
# https://leetcode.com/problems/smallest-even-multiple/description/
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # loop through the range given in the constraints
        for i in range(1, (2*n)+1):
            # checking if they are multiple of both 2 and n and returning the smallest + integer
            if i % 2 == 0 and i % n == 0:
                return i

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")