# Leetcode Problem 238: Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize the result list with all 1's
        result = [1] * len(nums)
        # initialize the prefix to 1
        prefix = 1
        # loop through each number in nums list and find the prefix of each number
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        # initialize the postfix value to 1
        postfix = 1
        # loop to find the postfix of each number from the end of the list
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        # return the result list at the end
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")