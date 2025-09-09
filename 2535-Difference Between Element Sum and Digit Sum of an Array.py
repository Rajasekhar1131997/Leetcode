# Leetcode Problem 2535: Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
from typing import List
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # initialize digit sum to 0
        digit_sum = 0
        # find the sum of all values of given list
        element_sum = sum(nums)
        # loop through each number in given list
        for num in nums:
            # if the number is < 10, we add it directly to digit sum
            if num < 10:
                digit_sum += num
            # else, we add each digit to digit sum
            else:
                while num != 0:
                    remainder = num % 10
                    digit_sum += remainder
                    num = num // 10
        # return the abs difference of element sum and digit sum as requested
        return abs(element_sum - digit_sum)

print("Time Complexity: O(N.D), where D is the digit in each num")
print("Space Complexity: O(1)")