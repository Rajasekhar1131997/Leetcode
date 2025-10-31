# Leetcode Problem 3692: Majority Frequency Characters
# https://leetcode.com/problems/majority-frequency-characters/description/
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        # initialize an empty hash map
        hash_map = {}
        # get the frequency of each character from the given string
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        # initialize an empty hash map to group the characters based on their frequency
        grouped = {}
        # logic to group the characters based on their frequency
        for char, freq in hash_map.items():
            if freq not in grouped:
                grouped[freq] = []
            grouped[freq].append(char)
        
        # find the max group size based on their len of characters
        max_group_size = max(len(chars) for chars in grouped.values())
        
        # now, loop through the frequency and their characters in grouped hashmap
        for freq, chars in sorted(grouped.items(), reverse = True):
            # if their length and max group size matches, return those characters by concatenating them
            if len(chars) == max_group_size:
                return ''.join(chars)

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")