# Leetcode Problem 3099: Harshad Number
# https://leetcode.com/problems/harshad-number/description/
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # initialize total to 0
        total = 0
        # make a copy of number x to num
        num = x
        # get the total of given number
        while x != 0:
            remainder = x % 10
            total += remainder
            x = x // 10
        # checking if the given number is said to be a harshad number or not
        if num % total == 0:
            return total
        # if not, we return -1
        else:
            return -1

print("Time Complexity: O(N)")
print("Space Complexity : O(1)")