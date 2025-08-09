# Leetcode Problem 2000: Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # Index of the first occurrence of ch (default -1 for now)
        first_occurrence = -1

        # Scan to find the first index i where word[i] == ch
        for i in range(len(word)):
            if word[i] == ch:
                first_occurrence = i
                break  # stop at the first match
        # if first occurrence of ch not found, we simply return the word without any changes
        if first_occurrence == -1:
            return word
        # Convert the string to a list so we can swap characters in place
        word = list(word)
        # Set two pointers to the start of the word and the found index
        left, right = 0, first_occurrence

        # Reverse the prefix [0 .. first_occurrence] in place
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1

        # Join the list back into a string and return
        return ''.join(word)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")