# Leetcode Problem 1913: Maximum Product Difference Between Two Pairs
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # sort the given numbers list in descending order
        nums.sort(reverse=True)
        # after sorting, the product of 1 & 2nd elements provide the maximum product and subtracting from the product of last 2 elements gives us the maximum product difference
        return (nums[0] * nums[1]) - (nums[-1] * nums[-2])

print("Time Complexity: O(N logN)")
print("Space Complexity: O(logN)")