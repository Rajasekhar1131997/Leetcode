# Leetcode Problem 2490: Circular Sentence
# https://leetcode.com/problems/circular-sentence/description/
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Assume the chain is valid initially
        is_chain = True

        # Split the sentence into individual words
        sentence = sentence.split()

        # First word first character
        fwfc = sentence[0][0]

        # Last word last character
        lwlc = sentence[-1][-1]

        # Assume the circular condition is valid initially
        is_circular = True

        # Check if first word first char == last word last char
        if fwfc == lwlc:
            is_circular = True
        else:
            is_circular = False

        # Loop through consecutive words to check the chain condition
        for i in range(len(sentence) - 1):
            last_char = sentence[i][-1]      # last char of current word
            first_char = sentence[i+1][0]    # first char of next word
            if last_char != first_char:      # if they don't match
                is_chain = False             # chain is broken
                break                        # stop checking further

        # Return True only if both circular and chain conditions hold
        return is_circular and is_chain
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")