# Leetcode Problem 1832: Check if the Sentence Is Pangram
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # initialize all the alphabets
        letters = "abcdefghijklmnopqrstuvwxyz"
        # initialize an empty hashmap to store each letter in alphabets
        hash_map = {}
        # for each letter in alphabets, mark the hashmap with false value
        for letter in letters:
            hash_map[letter] = False
        # now we want to check and see if each character in given string occures atleast one or not and make it to True
        for char in sentence:
            hash_map[char] = True
        # once all the letters are processed, we then check if there are any False values in hashmap and return False if yes, otherwise true
        for key in hash_map:
            if not hash_map[key]:
                return False
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")