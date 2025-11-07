# Leetcode Problem 3120: Count the Number of Special Characters I
# https://leetcode.com/problems/count-the-number-of-special-characters-i/description/
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # convert the given string into set
        seen = set(word)
        # initialize the count to 0
        count = 0
        # initialize an empty set 
        counted = set()
        # loop through each character in seen set
        for char in seen:
            # if the character is lowercase, then we check if the uppercase of that character is present in seen set and if it's not present in counted set or not
            if char.islower():
                if char.upper() in seen and char not in counted:
                    # if yes, we count that and add that char to counted
                    count += 1
                    counted.add(char)
        # finally, return the special letter in the word
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")