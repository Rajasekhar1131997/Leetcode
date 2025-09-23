# Leetcode Problem 1417: Reformat The String
# https://leetcode.com/problems/reformat-the-string/description/
class Solution:
    def reformat(self, s: str) -> str:
        # initialize an empty letters and numbers list to store respective characters from string
        letters = []
        numbers = []
        # loop through each character in string s
        for char in s:
            # if the character is digit, we append that to numbers list
            if char.isdigit():
                numbers.append(char)
            # else, we append that character to letters list
            else:
                letters.append(char)
        # we need to check if it is impossible to reformat the string and return empty string
        if abs(len(letters) - len(numbers)) > 1:
            return ""
        
        # initialize an empty result list to store new permutation
        result = []
        # check which has the more characters, either letters or numbers
        if len(letters) > len(numbers):
            longlist, shortlist = letters, numbers
        else:
            longlist, shortlist = numbers, letters
        
        # loop through the long list and append that character to result
        for i in range(len(longlist)):
            result.append(longlist[i])
            # at the same time append a character from the shortlist to result
            if i < len(shortlist):
                result.append(shortlist[i])
        # finally, return the concatenated string
        return "".join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")