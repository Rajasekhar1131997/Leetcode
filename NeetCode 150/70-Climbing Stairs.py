# Leetcode Problem 70: Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        # Initializing two variables one and two to 1
        one, two = 1, 1
        # we start from the end
        for i in range(n-1):
            # we store the one value to temp
            temp = one
            # we update the one with sum of one and two
            one = one + two
            # now, we assign the value of temp to two
            two = temp
        # return one as the result
        return one

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")