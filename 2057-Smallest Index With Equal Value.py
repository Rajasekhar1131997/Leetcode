# Leetcode Problem 2057: Smallest Index With Equal Value
# https://leetcode.com/problems/smallest-index-with-equal-value/description/
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        # loop through each number in given nums list
        for i in range(len(nums)):
            # check the given condition and return the smallest index
            if i % 10 == nums[i]:
                return i
        # if there is no such index, we return -1
        return -1

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")