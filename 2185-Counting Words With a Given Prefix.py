# Leetcode Problem 2185: Counting Words With a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # initialize the count to 0
        count = 0
        # loop through each word in words list
        for word in words:
            # check if the word starts with the prefix given using startswith
            if word.startswith(pref):
                # increment the count
                count += 1
        # return the count at the end
        return count

print("Time Complexity: O(N * M), where M is the length of the prefix for each word it checks")
print("Space Complexity: O(1)")