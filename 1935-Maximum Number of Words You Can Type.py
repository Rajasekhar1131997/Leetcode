# Leetcode Problem 1935: Maximum Number of Words You Can Type
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # initialize the count to 0
        count = 0
        # convert the given brokenLetters to set
        broken = set(brokenLetters)
        # split the given text
        text = text.split()
        # loop through each word in text
        for i in range(len(text)):
            word = text[i]
            # check if any of the character in the word is present in broken, if yes, we count it
            if all(char not in broken for char in word):
                count += 1
        # return the count at the end
        return count

print("Time Complexity: O(N.M)")
print("Space Complexity: O(1)")