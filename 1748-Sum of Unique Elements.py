# Leetcode Problem 1748: Sum of Unique Elements
# https://leetcode.com/problems/sum-of-unique-elements/description/
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # initialize an empty hash map
        hash_map = {}
        # initialize the total to 0
        total = 0
        # loop through each num in nums to get frequency
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        # get the total of unique elements, if their frequncy is 1, we add that value to total
        for value, count in hash_map.items():
            if count == 1:
                total += value
        # return the total
        return total

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")