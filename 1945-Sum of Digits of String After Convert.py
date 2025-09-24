# Leetcode Problem 1945: Sum of Digits of String After Convert
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # helper function to convert the given string into digit string
        def str2digit(s):
            alphabets = "abcdefghijklmnopqrstuvwxyz"
            i = 1
            hash_map = {}
            for char in alphabets:
                hash_map[char] = i
                i += 1
            string = ""
            for char in s:
                string += str(hash_map[char])
            return string
        # calling the helper function with given string
        numstring = str2digit(s)
        # we need to sum its digit repeatedly k times.
        for i in range(k):
            numstring = str(sum(int(d) for d in numstring))
        # we need to return the final integer
        return int(numstring)

print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")