# Leetcode Problem 507: Perfect Number
# https://leetcode.com/problems/perfect-number/description/
# this problem exceeds the time limit for bigger number, so 58 testcases passed.
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # initialize an empty variable sum to keep track of the sum
        sum = 0
        # we need to find the divisiors of the given number including the num, because a number can be divisor of itself
        for i in range(1, num+1):
            # if num is divisible by integer i, then it's a divisor
            if num % i == 0:
                # adding each divisor
                sum += i
        # since, the sum includes the number itself, we subtract the given number from sum
        return sum-num == num

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")