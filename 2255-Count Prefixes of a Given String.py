# Leetcode Problem 2255: Count Prefixes of a Given String
# https://leetcode.com/problems/count-prefixes-of-a-given-string/description/
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # initialize the count to 0
        count = 0
        # loop through each word in words
        for word in words:
            # check if the string startswith each word listed, if yes, increment the count, else 0
            if s.startswith(word):
                count += 1
        # return the count
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")