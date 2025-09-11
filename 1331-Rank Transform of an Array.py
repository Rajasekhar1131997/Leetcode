# Leetcode Problem 1331: Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array/description/
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # make a copy of the given arr list
        copy = arr.copy()
        # sort the given list
        arr.sort()
        # initialize the hashmap
        hash_map = {}
        i = 1
        # loop through each number in arr
        for num in arr:
            # if the number is already present in hashmap, skip it
            if num not in hash_map:
                # assigning the rank
                hash_map[num] = i
                # increase the rank
                i += 1
        # giving the rank of the number
        for index in range(len(copy)):
            copy[index] = hash_map[copy[index]]
        # return the updated rank array
        return copy

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")