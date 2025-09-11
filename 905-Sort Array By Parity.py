# Leetcode Problem 905: Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/description/
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
        return nums

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")