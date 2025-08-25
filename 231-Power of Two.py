# Leetcode Problem 231: Power of Two
# https://leetcode.com/problems/power-of-two/description/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # we check if n value is greater than 0 or not and we perform bitwise and operator
        return n > 0 and (n & (n-1)) == 0

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")