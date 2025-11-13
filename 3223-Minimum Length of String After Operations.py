# Leetcode Problem 3223: Minimum Length of String After Operations
# https://leetcode.com/problems/minimum-length-of-string-after-operations/description/
class Solution:
    def minimumLength(self, s: str) -> int:
        # initialize an empty hash_map
        hash_map = {}
        # find the frequency of each character in the given string
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        # let the final count or minimum length of final string be 0
        final_count = 0
        # loop through the counter
        for char, count in hash_map.items():
            # if the count is > 2, we decrease the count by 2 and assign that count to that char
            while count > 2:
                count -= 2
            hash_map[char] = count
            # we also compute the final count
            final_count += count
        # In the end, we return the final count
        return final_count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")