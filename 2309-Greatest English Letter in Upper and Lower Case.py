# Leetcode Problem 2309: Greatest English Letter in Upper and Lower Case
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/
class Solution:
    def greatestLetter(self, s: str) -> str:
        # convert the given string into set
        seen = set(s)
        # initialize an empty set to store capitalized letters
        letters = set()
        # loop through each character in seen
        for char in seen:
            # check if that character is present in both lower and upper cases in seen set
            if char.upper() in seen and char.lower() in seen:
                # if yes, add that letter to letters set
                letters.add(char.upper())
        # return the max letter from the letters, otherwise return empty string
        return max(letters) if letters else "" 

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")