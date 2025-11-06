# Leetcode Problem 3232: Find if Digit Game Can Be Won
# https://leetcode.com/problems/find-if-digit-game-can-be-won/description/
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        # compute the single digit sum
        single_digit_sum = sum(digit for digit in nums if digit < 10)
        # compute the double digit sum
        double_digit_sum = sum(digit for digit in nums if digit >= 10)
        # if their sums are not equal, that means no matter what digits alice choose, he will win and can return true, otherwise false
        if single_digit_sum != double_digit_sum:
            return True
        else:
            return False

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")