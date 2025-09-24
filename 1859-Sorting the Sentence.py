# Leetcode Problem 1859: Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/description/
class Solution:
    def sortSentence(self, s: str) -> str:
        # intiliaze an empty result list to store the words
        result = []
        # split the given sentence
        s = s.split()
        # sort the words based on the last character of each word
        sorted_s = sorted(s, key=lambda word:word[-1])
        # we want to delete the last character from each word and append it to result list
        for word in sorted_s:
            word = word[:-1]
            result.append(word)
        # finally, return the list after concatenation
        return " ".join(result)

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")