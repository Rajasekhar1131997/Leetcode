# Leetcode Problem 2114: Maximum Number of Words Found in Sentences
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # initialize the max sentence to -1
        max_sentence = -1
        # loop through each sentence in given list of sentences
        for sentence in sentences:
            # split the sentence
            sentence = sentence.split()
            # find the length of the each sentence
            sentence_len = len(sentence)
            # find the max length sentence
            max_sentence = max(max_sentence, sentence_len)
        # return the max_sentence
        return max_sentence

print("Time Complexity: O(N.M)")
print("Space Complexity: O(M)")