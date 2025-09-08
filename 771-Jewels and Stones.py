# Leetcode Problem 771: Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # initialize an empty hash map to store the jewels
        hash_map = {}
        # initialize the count to 0
        count = 0
        # for every jewel in jewels, marking it as true
        for jewel in jewels:
            hash_map[jewel] = True
        # check every stone in stones
        for stone in stones:
            # checking if that stone is present in the hashmap or not
            if stone in hash_map:
                # if it's present, increase the count by 1
                count += 1
        # return the count at the end
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")