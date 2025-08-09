# Leetcode Problem 350: Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # initialize an empty dictionary
        dict1 = {}
        # loop through nums1 and get frequency of each number
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
        # initialize an empty result list
        result = []
        # loop through each num in nums2 list
        for num in nums2:
            # check if that number is present in our dictionary or not
            if dict1.get(num, 0) > 0:
                # if yes, append that value to the result list
                result.append(num)
                # decrement the count of that number from list by 1
                dict1[num] -= 1
        # return the result
        return result

print("Time Complexity: O(N + M)")
print("Space Complexity: O(K), where k is the number of distinct elements we count")