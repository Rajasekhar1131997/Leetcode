# Leetcode Problem 1455: Check If a Word Occurs As a Prefix of Any Word in a Sentence
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # splitting the given single spaced sentence into list using split method
        sentence = sentence.split(" ")
        # loop until each word is checked
        for i in range(len(sentence)):
            # using startswith function, we check if the word is prefix of searchWord
            if sentence[i].startswith(searchWord):
                # if yes, we return i+1, since it's a 1-indexed list
                return i+1
        # if the above case didn't exist, we return -1
        return -1

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")