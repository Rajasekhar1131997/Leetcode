# Leetcode Problem 1464: Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initialize the max value to 0
        max_num = 0
        # loop through each value in nums
        for i in range(len(nums)):
            # inner loop starting from after i
            for j in range(i+1, len(nums)):
                # check the maximum product
                product = (nums[i] - 1) * (nums[j] - 1)
                max_num = max(max_num, product)
        # return the max num
        return max_num

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")