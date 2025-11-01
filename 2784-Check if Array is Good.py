# Leetcode Problem 2784: Check if Array is Good
# https://leetcode.com/problems/check-if-array-is-good/description/
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # find the max number from the nums list
        n = max(nums)
        # now create a new array based on the max number
        arr = list(range(1, n)) + [n, n]
        # return true if the new array is same as sorted array of original array, else false
        if sorted(nums) == arr:
            return True
        else:
            return False

print("Time Complexity: O(N logN)")
print("Space Complexity: O(1)")