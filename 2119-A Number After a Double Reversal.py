# Leetcode Problem 2119: A Number After a Double Reversal
# https://leetcode.com/problems/a-number-after-a-double-reversal/description/
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # base case, check if the number is 0, we return True
        if num == 0: return True
        # Initially, reverse the given number
        reversed_num = int(str(num)[::-1])
        # secondly, reverse the reversed number
        rev_reversed_num = int(str(reversed_num)[::-1])
        # check if the second reversed number equal to given number
        return num == rev_reversed_num

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")