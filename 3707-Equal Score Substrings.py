# Leetcode Problem 3707: Equal Score Substrings
# https://leetcode.com/problems/equal-score-substrings/description/
class Solution:
    def scoreBalance(self, s: str) -> bool:
        # intialize an empty hash_map to store positions of its characters in the alphabet
        hash_map = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        i = 1
        # assigning the position of each character
        for letter in letters:
            hash_map[letter] = i
            i += 1
        # convert the given string into scores for each character
        scores = [hash_map[c] for c in s]
        # find the total of the scores
        total = sum(scores)
        # initialize the left sum to 0
        left_sum = 0

        # loop through each score in scores
        for i in range(len(scores) - 1):
            # compute the left sum
            left_sum += scores[i]
            # check if the left sum is equal to the rest of the scores, if yes, return true else continue
            if left_sum == total - left_sum:
                return True
        # return false, if any of the above doesn't match
        return False

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")