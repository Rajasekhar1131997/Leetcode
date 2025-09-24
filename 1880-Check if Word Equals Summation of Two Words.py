# Leetcode Problem 1880: Check if Word Equals Summation of Two Words
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description/
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # helper function to convert the given word into integer value
        def word2num(word):
            # if the length of given word is 0, we return 0
            if len(word) == 0:
                return 0
            # define an empty string
            string = ""
            # define the alphabets
            letters = "abcdefghijklmnopqrstuvwxyz"
            # map the alphabets to numbers starting from index 0
            hash_map = {}
            i = 0
            for letter in letters:
                hash_map[letter] = i
                i += 1
            # loop through each character in word
            for char in word:
                # append each character to string
                string += str(hash_map[char])
            # finally, return the integer value of the generated string
            return int(string)
        # we need to check if the first & second word sum is equal to the target word
        return word2num(firstWord) + word2num(secondWord) == word2num(targetWord)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")