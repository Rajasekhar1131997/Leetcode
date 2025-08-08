# Leetcode Problem 345: Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
class Solution:
    def reverseVowels(self, s: str) -> str:
        # s is a string, we change the string to list
        s = list(s)
        # create a set with lower and uppercases of vowels
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        # initialize our left and right pointer to use two-pointers technique
        left = 0
        right = len(s) - 1
        # loop until we check each character in the list
        while left < right:
            # if the left character is not in vowels, we move right to the next character
            if s[left] not in vowels:
                left += 1
            # if the right character is not in vowels, we move left to the next character
            elif s[right] not in vowels:
                right -= 1
            # if we find that they are vowels, we interchange them and move our pointers to right and left
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        # since we need to return string, using join we convert list to string
        return ''.join(s)
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")