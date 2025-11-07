# Leetcode Problem 1822: Sign of the Product of an Array
# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # let the product be 1
        product = 1
        # loop through each number in nums list and compute the product
        for num in nums:
            product *= num
        # if the product value is 0, we return 0
        if product == 0:
            return 0
        # if the product value is greater than 0, we return 1
        elif product > 0:
            return 1
        # else, we return -1
        else:
            return -1
    
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")