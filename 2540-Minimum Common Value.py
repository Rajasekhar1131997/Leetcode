# Leetcode Problem 2540: Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/
from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # convert the nums1 array into set to eliminate the duplicate values
        set1 = set(nums1)
        # convert the nums2 array into set to eliminate the duplicate values
        set2 = set(nums2)
        # find the common values from both sets using intersection
        common = set1 & set2
        # return the min value from common set, if there isn't one, return -1
        return min(common) if common else -1

print("Time Complexity: O(N + M)")
print("Space Complexity: O(N + M)")

# we can also solve this problem using Two pointer approach
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # initialize the i pointer to keep track of nums1
        i = 0
        # initialize the j pointer to keep track of nums2
        j = 0
        while i < len(nums1) and j < len(nums2):
            # if both the numbers are equal, we return that number
            if nums1[i] == nums2[j]:
                return nums1[i]
            # else if the value from nums1 is less than nums2, we move i pointer by 1 to right
            elif nums1[i] < nums2[j]:
                i += 1
            # else, we move the j pointer in nums2 by 1 to right
            else:
                j += 1
        # return -1 if the above case didn't exist
        return -1

print("Time Complexity: O(N+M)")
print("Space Complexity: O(1)")