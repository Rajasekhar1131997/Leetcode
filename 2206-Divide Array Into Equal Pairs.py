# Leetcode Problem 2206: Divide Array Into Equal Pairs
# https://leetcode.com/problems/divide-array-into-equal-pairs/description/
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # initialize an empty hash map
        hash_map = {}
        # get the frequency of each number
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        # we can divide the nums into equal pairs only if their count is even, otherwise return False
        for count in hash_map.values():
            if count % 2 != 0:
                return False
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")