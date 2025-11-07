# Leetcode Problem 1816: Truncate Sentence
# https://leetcode.com/problems/truncate-sentence/description/
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # split the given sentence into list
        s = s.split()
        # initialize an empty result list
        result = []
        # loop through the range of k and add those words into list
        for i in range(k):
            result.append(s[i])
        # return the concatenated string using join separated by space
        return ' '.join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")