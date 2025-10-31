# Leetcode Problem 3663: Find The Least Frequent Digit
# https://leetcode.com/problems/find-the-least-frequent-digit/description/
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        # convert the given integer to string
        string = str(n)
        # initialize an empty hash_map
        hash_map = {}
        # find the frequency of each character
        for char in string:
            hash_map[char] = hash_map.get(char, 0) + 1
        # grouping the characters based on their frequency
        grouped = {}
        for char, freq in hash_map.items():
            if freq not in grouped:
                grouped[freq] = []
            grouped[freq].append(char)
        
        # find the minimum frequency
        min_freq = min(grouped.keys())
        # get the least frequency digits in sorted order
        least_freq_digits = sorted(grouped[min_freq])
        # finally, return the 1st value from the array from the least frequency digits
        return int(least_freq_digits[0])

print("Time Complexity: O(logN)")
print("Space Complexity: O(1)")