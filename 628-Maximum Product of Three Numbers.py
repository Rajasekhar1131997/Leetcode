# Leetcode Problem 628: Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # sort the given number list in ascending order
        nums.sort()
        # find the product of largest three numbers from the list
        largest_numbers_product = nums[-1] * nums[-2] * nums[-3]
        # find the product of smallest two numbers and one max number
        smallest_2_largest_1 = nums[0] * nums[1] * nums[-1]
        # return the maximum product of both
        return max(largest_numbers_product, smallest_2_largest_1)

print("Time Complexity: O(N logN)")
print("Space Complexity: O(1)")