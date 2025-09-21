# Leetcode Problem 2404: Most Frequent Even Element
# https://leetcode.com/problems/most-frequent-even-element/description/
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # initialize an empty hashmap
        hash_map = {}
        # loop through each number in nums list
        for num in nums:
            # we need to get the count of elements which are even
            if num % 2 == 0:
                hash_map[num] = hash_map.get(num, 0) + 1
        # if there are no even elements, we return -1
        if not hash_map:
            return -1
        # find the maximum frequency/count from the hashmap
        max_freq = max(hash_map.values())
        # we also need to return the min value of even number
        return min([k for k, v in hash_map.items() if v == max_freq])

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")