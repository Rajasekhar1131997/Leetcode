# Leetcode Problem 263: Ugly Number
# https://leetcode.com/problems/ugly-number/description/
class Solution:
    def isUgly(self, n: int) -> bool:
        # base case, if the given number is less than or equal to 0, return False
        if n <= 0:
            return False
        # loop through the given prime factors 2, 3 and 5
        for i in [2, 3, 5]:
            # we keep dividing with 2, 3 and 5 while possible
            while n % i == 0:
                # divide n by i for each iteration
                n //= i
        # at the end, if n is equal to 1, return true else false
        return n == 1

print("Time Complexity: O(log N)")
print("Space Complexity: O(1)")