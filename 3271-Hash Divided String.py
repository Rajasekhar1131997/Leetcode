# Leetcode Problem 3271: Hash Divided String
# https://leetcode.com/problems/hash-divided-string/description/
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        # initialize an empty result list and hash_map
        result = []
        hash_map = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        # hashing the letters with their respective hash value
        for letter in letters:
            hash_map[letter] = i
            i += 1
        # find the length of given string
        n = len(s)
        # loop through the given string with substring/gap with k
        for i in range(0, n, k):
            # let the subtotal be 0
            subtotal = 0
            # loop through each substring
            for j in range(i, i+k):
                # compute the subtotal
                subtotal += hash_map[s[j]]
            # find the hashed value
            hashed_value = subtotal % 26
            # add that corresponding character of hashed value to result list
            result.append(chr(ord('a') + hashed_value))
        # return the result list by joining them
        return ''.join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")