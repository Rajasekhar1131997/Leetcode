# Leetcode Problem 33: Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# we can solve this problem using Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize the left pointer to start of the list
        left = 0
        # initialize the right pointer to end of the list
        right = len(nums) - 1
        # start the while loop
        while left < right:
            # find the mid point
            mid = (left + right) // 2
            # if the target is equal to the mid point, we simply return mid index
            if target == nums[mid]:
                return mid
            # checking if the list is sorted or not in the left side of mid point
            if nums[left] <= nums[mid]:
                # check if the target lies in between left and mid point, we make the right pointer to be mid - 1
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # else, we update the left pointer to mid + 1
                else:
                    left = mid + 1
            # if the array is not sorted and our target lies in b/w mid and right pointer
            else:
                if nums[mid] <= target <= nums[right]:
                    # we update the left pointer to start from mid+1
                    left = mid + 1
                else:
                    # we update the right pointer to be mid-1
                    right = mid - 1
        # if the target isn't present, we have to return -1 else we return right
        return -1 if nums[right] != target else right

print("Time Complexity: O(log N)")
print("Space Complexity: O(1)")