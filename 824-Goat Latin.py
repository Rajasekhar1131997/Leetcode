# Leetcode Problem 824: Goat Latin
# https://leetcode.com/problems/goat-latin/description/
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # Split the given sentence in words using split command
        words = sentence.split()
        # define the vowels
        vowels = ['a','e','i','o','u']
        # loop through each word in words list
        for i in range(len(words)):
            # assing the each word to a variable
            word = words[i]
            # check if the first letter in word starts with vowels, if yes append ma to the end of word
            if word[0].lower() in vowels:
                word += "ma"
            # check if the first letter in word starts with consonants, if yes remove the first letter and append that to the end of string and append ma to the end of string
            else:
                word = word[1:] + word[0]
                word += "ma"
            # as per 3rd condition, we need to 'a's for each word based on its index position
            word += ('a' * (i+1))
            # assign the modified word to words list
            words[i] = word
        # finally, return the sentence after appending
        return " ".join(words)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")