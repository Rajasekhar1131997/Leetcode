# Leetcode Problem 389: Find the Difference
# https://leetcode.com/problems/find-the-difference/description/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize two empty dictionary or hash maps for both strings
        hash_s, hash_t = {},  {}
        # get the frequency of each character in string s
        for char in s:
            hash_s[char] = hash_s.get(char, 0) + 1
        # get the frequency of each character in string t
        for char in t:
            hash_t[char] = hash_t.get(char, 0) + 1
        # loop through each character in string t hash map
        for char in hash_t:
            # if that added character is not in string s hash map, return that character
            if char not in hash_s:
                return char
            # if the frequency of that charater from both hash maps and return that character
            if hash_s[char] < hash_t[char]:
                return char

print("Time Complexity: O(N)")
print("Space Complexity: O(1), if the strings of lower case characters, O(N) for all cases")

# Solving this problem using ASCII approach
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize two variables sum_s and sum_t
        sum_s, sum_t = 0, 0
        # ord function get the ascii value of each character, we find the total sum of string s
        for char in s:
            sum_s += ord(char)
        # ord function get the ascii value of each character, we find the total sum of string t 
        for char in t:
            sum_t += ord(char)
        # we find the difference and return that character using chr function
        return chr(sum_t - sum_s)

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")