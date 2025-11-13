# Leetcode Problem 451: Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/description/
class Solution:
    def frequencySort(self, s: str) -> str:
        # initialize an empty hash_map
        hash_map = {}
        # find the frequency of each character from the string
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        # using lambda, sort the key value pairs in descending order
        sorted_items = sorted(hash_map.items(), key=lambda x:x[1], reverse = True)
        # now, print the characters based on their counts
        output = [char for char, count in sorted_items for _ in range(count)]
        # return the concatenated string at the end
        return ''.join(output)

print("Time Complexity: O(N + N logN) => O(N) for limited alphabets/characters")
print("Space Complexity: O(N)")