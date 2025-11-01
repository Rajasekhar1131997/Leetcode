# Leetcode Problem 2788: Split Strings by Separator
# https://leetcode.com/problems/split-strings-by-separator/description/
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # initialize an empty list to store the result
        words_list = []
        # loop through each word in words list
        for word in words:
            # seperate each combined word with help of separator
            split_words = word.split(separator)
            # append that seperated words as a list to words_list
            words_list.append(split_words)
        # now process each sublist and combine them into a single list
        combined = [word for sublist in words_list for word in sublist if word!= '']
        # return the combined list at the end
        return combined

print("Time Complexity: O(M.N)")
print("Space Complexity: O(M.N)")