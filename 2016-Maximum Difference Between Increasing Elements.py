# Leetcode Problem 2016: Maximum Difference Between Increasing Elements
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # initialize the max difference to -1
        max_difference = -1
        # let n be the length of nums
        n = len(nums)
        # start the for loop
        for i in range(n):
            for j in range(n):
                # check the conditions as listed
                if 0 <= i < j < n and nums[i] < nums[j]:
                    # compute the difference
                    diff = nums[j] - nums[i]
                    # compute the max difference
                    max_difference = max(diff, max_difference)
        # finally, return the max difference
        return max_difference

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")