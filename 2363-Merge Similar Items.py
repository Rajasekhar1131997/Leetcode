# Leetcode problem 2363: Merge Similar Items
# https://leetcode.com/problems/merge-similar-items/description/
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # first combine both the lists into a single list
        items = items1 + items2
        # initialize an empty hashmap
        hash_map = {}
        # loop through every value and weight in items list
        for value, weight in items:
            # add their weights for each value
            hash_map[value] = hash_map.get(value, 0) + weight
        # we need to return the sum of weights of all items with value in sorted manner
        result_list = [[value, weight] for value, weight in sorted(hash_map.items())]
        return result_list

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")