# Leetcode Problem 442: Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # initialize an empty list to store result
        output = []
        # initialize an empty hashmap to store frequency of each num in nums list
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        # loop through the hash map and add the numbers whose frequency is >= 2
        for num, count in hash_map.items():
            if count >= 2:
                output.append(num)
        # return the output
        return output

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")