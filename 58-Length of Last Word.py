# Leetcode Problem 58: Length of Last Word
#https://leetcode.com/problems/length-of-last-word/description/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # with the help of split function, split the given word into words
        s = s.split()
        # get the last word using negative indexing
        last_word = s[-1]
        # finally, we return the length of the last word
        return len(last_word)

print("Time Complexity: O(N), as the splitting takes O(N) time")
print("Space Complexity: O(N), since the splitting is creating a list of words")