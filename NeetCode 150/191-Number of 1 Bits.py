# Leetcode Problem 191: Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        # if n value is 0, we return 0
        if n == 0:
            return 0
        # initialize the result to 0, this will hold the number of 1's
        result = 0
        # loop until the n is greater than 0
        while n > 0:
            # get the remainder using % 2
            digit = n % 2
            # add that remainder to the result
            result += digit
            # decrease the value of n
            n = n // 2
        # return the result
        return result

print("Time Complexity: O(log N)")
print("Space Complexity: O(1)")