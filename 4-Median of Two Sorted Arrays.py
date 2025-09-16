# Leetcode Problem 4: Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # append all the values from nums2 list to nums1 list
        for num in nums2:
            nums1.append(num)
        # sort the values of nums1 list
        nums1.sort()
        # trying to calculate the median, initialize left and right to find the mid value
        left = 0
        right = len(nums1) - 1
        # find the mid value
        mid = left +(right-left) // 2
        # check whether the list is even or odd length
        if len(nums1) % 2 == 0:
            sum = nums1[mid] + nums1[mid+1]
            median = sum / 2
            return median
        # if the list length is odd, we simply return the mid value
        else:
            return nums1[mid]
    
print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")
