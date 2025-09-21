# Leetcode Problem 2427: Number of Common Factors
# https://leetcode.com/problems/number-of-common-factors/description/
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # initialize the count to 0
        count = 0
        # loop through 1 to minimum number from a and b, because the number should be a common factor of both a and b
        for i in range(1, min(a,b)+1):
            # check if the number is divisible by both a and b or not
            if a % i == 0 and b % i == 0:
                # increase the count by 1
                count += 1
        # return the count at the end
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")