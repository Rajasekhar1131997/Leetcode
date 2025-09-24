# Leetcode Problem 2089: Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # sort the given list in ascending order
        nums.sort()
        # initialize an empty result list
        result = []
        # loop through each number in nums list
        for i in range(len(nums)):
            # check if the given number is equal to target, then append that number to result list
            if nums[i] == target:
                result.append(i)
        # return the result list
        return result

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")