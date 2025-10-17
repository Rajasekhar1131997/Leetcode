# Leetcode Problem 153: Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Class definition for the solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # initialize the left pointer to the start of the list
        left = 0
        # initialize the right pointer to the end of the list
        right = len(nums) - 1
        # loop continues until left pointer meets right pointer
        while left < right:
            # find the middle index between left and right
            mid = (left + right) // 2
            # if middle element is greater than the rightmost element,
            # that means the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # otherwise, the minimum is in the left half (including mid)
            else:
                right = mid
        # when the loop ends, both pointers point to the minimum element
        return nums[right]

print("Time Complexity: O(log N)")
print("Space Complexity: O(1)")

# we can also solve this problem using recrusive approach
# Class definition for the solution
class Solution:
    # helper function to recursively call
    def find(self, left, right, nums):
        # base case, if the right pointer is less than or equal to left, we return nums[right]
        if right <= left:
            return nums[right]
        # find the mid value
        mid = (left+right) // 2
        # if the mid value is greater than the right most value in nums list, min value will be in right side, so we recursively call the function starting from mid+1 point
        if nums[mid] > nums[right]:
            return self.find(mid+1, right, nums)
        # else, the min value will be in the left side
        else:
            return self.find(left, mid, nums)
    # main function
    def findMin(self, nums: List[int]) -> int:
        # calling the recursive function with initial values
       return self.find(0, len(nums)-1, nums)
    

print("Time Complexity: O(log N)")
print("Space Complexity: O(1)")