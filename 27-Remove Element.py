# Leetcode Problem 27: Remove Element
# https://leetcode.com/problems/remove-element/description/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # if the nums list is empty, return 0
        if not nums:
            return 0
        # initialize the k to 0
        k = 0
        # loop through each num in nums
        for i in range(len(nums)):
            # check if the current val is not equal to val or not
            if nums[i] != val:
                # if it's not equal, we move that value/assign that value
                nums[k] = nums[i]
                # increment the k value
                k += 1
        # finally, return the k value, which consists of number of elemens in nums != val
        return k

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")