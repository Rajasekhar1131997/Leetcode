# Leetcode Problem 152: Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # let the minimum and maximum product be the first value of nums list
        min_product = max_product = nums[0]
        # initialize the maximum product to keep track of the max product
        maximum_product = max_product
        # looping through remaining values from the nums list
        for num in nums[1:]:
            # assign the min product to temp
            temp = min_product
            # find the minimum product for each value we are multiplying
            min_product = min(num, min_product*num, max_product*num)
            # we also need to find the maximum product for each value we are multiplying
            max_product = max(num, temp*num, max_product*num)
            # finally, find the maximum product
            maximum_product = max(maximum_product, max_product)
        # return the maximum_product
        return maximum_product

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")