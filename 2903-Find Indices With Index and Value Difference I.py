# Leetcode Problem 2903: Find Indices With Index and Value Difference I
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        if len(nums) == 1 and indexDifference == 0 and valueDifference == 0:
            return [0, 0]
        # loop through nums list starting from index 0
        for i in range(len(nums)):
            # loop through nums list starting from index 1 to end of list
            for j in range(len(nums)):
                # check the given condition
                if abs(i-j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    # if there are such combinations, we return any of the resulting pair (i, j)
                    return [i, j]
        # otherwise, we need to return [-1, -1]
        return [-1, -1]

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")