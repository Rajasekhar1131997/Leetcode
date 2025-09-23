# Leetcode Problem 1636: Sort Array by Increasing Frequency
# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # initialize an empty hashmap
        hash_map = {}
        # get the frequency of each number
        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1
        # sort the hashmap using lambda function where x[1] sorts the values based on high frequency and -x[0] sorts the values with higher number if they have same frequency
        sorted_hash_map = sorted(hash_map.items(), key=lambda x:(x[1],-x[0]))
        # we have to return only the numbers, so we use below
        return [num for num,count in sorted_hash_map for _ in range(count)]

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")