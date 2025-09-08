# Leetcode Problem 3541: Find Most Frequent Vowel and Consonant
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/
class Solution:
    def maxFreqSum(self, s: str) -> int:
        # initialize an empty hashmap for vowels
        vowels = {}
        # initialize an empty hashmap for consonants
        consonants = {}
        # get the frequency of vowels and consonants
        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowels[char] = vowels.get(char, 0) + 1
            else:
                consonants[char] = consonants.get(char, 0) + 1
        # get the maximum frequency of vowels
        max_vowels_freq = max(vowels.values()) if vowels else 0
        # get the maximum frequency of consonants
        max_consonants_freq = max(consonants.values()) if consonants else 0
        # return the sum of max_vowels_freq and max_consonants_freq
        return max_vowels_freq + max_consonants_freq

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")