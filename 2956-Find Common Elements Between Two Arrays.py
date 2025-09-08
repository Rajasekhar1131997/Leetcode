# Leetcode Problem 2956: Find Common Elements Between Two Arrays
# https://leetcode.com/problems/find-common-elements-between-two-arrays/description/
from typing import List
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map1 = {}
        hash_map2 = {}
        count1 = count2 = 0
        for num in nums1:
            hash_map1[num] = hash_map1.get(num, 0) + 1
        for num in nums2:
            hash_map2[num] = hash_map2.get(num, 0) + 1
        for num in nums1:
            if num in hash_map2:
                count1 += 1
        for num in nums2:
            if num in hash_map1:
                count2 += 1
        return [count1, count2]

print("Time Complexity: O(N + M)")
print("Space Complexity: O(N + M)")

# we can also solve this problem using Sets
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # eliminate the duplicate values from nums1
        set1 = set(nums1)
        # eliminate the duplicate values from nums2
        set2 = set(nums2)
        # get the count of numbers from nums1 present in set2
        count1 = sum(num in set2 for num in nums1)
        # get the count of numbers from nums2 present in set1
        count2 = sum(num in set1 for num in nums2)
        # return the count1 and count2 in list
        return [count1, count2]

print("Time Complexity: O(N + M)")
print("Space Complexity: O(N + M)")