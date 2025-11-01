# Leetcode Problem 3674: Minimum Operations to Equalize Array
# https://leetcode.com/problems/minimum-operations-to-equalize-array/description/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # convert the given nums list to set and check the length
        # if all the elements in nums are equal, we don't need to perform any operations and return 0
        if len(set(nums)) == 1:
            return 0
        # if the elements differ, we perform the bitwise AND operation of all elements in one go, so we return 1
        else:
            return 1

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")